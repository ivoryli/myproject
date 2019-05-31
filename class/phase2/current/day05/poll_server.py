'''
poll多路复用
次重点
'''

from socket import *
from select import *

#创建关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

#创建poll
p = poll()

#建立查找字典 {fileno:io_obj}
fdmap = {s.fileno():s}

#设置关注IO
p.register(s,POLLIN | POLLERR |POLLHUP)

#循环监控IO事件发生
while True:
    events = p.poll()  #阻塞等待IO发生
    # print(events)
    #遍历列表处理IO
    for fd,event in events:
        #[(s.fileno,pollin),(c.fileno,pollhup),(c.fileno,pollin)]2,3项位置可能会换
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect From:",addr)
            #添加新的关注事件
            p.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()] = c
        # elif event & POLLHUP:  #无法检测到挂起信号
        elif event & POLLIN:   #客户端发消息
            data = fdmap[fd].recv(1024)
            # 断开发生时data得到空, 此时pollin也会就绪
            if not data:
                print("客户端退出")
                # 描述符和对象都可以,取消关注
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]  # 从字典删除
                continue
            print(data.decode())
            fdmap[fd].send(b"OK")