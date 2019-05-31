'''
poll多路复用
次重点
linux专属
'''

# 流程:
#     导入模块
#     创建epoll对象
#     建立网络监听
#     设置关注对象及关注事件类型
#     创建epoll关注对象字典, 因为poll返回值为关注的io对象文件描述符和关注的io事件类型
#
#     while True：
#     使用变量绑定
#     epoll对象的epoll方法的返回值
#     遍历返回值
#     判断是否是套接字，是就accept，添加关注对象connfd，添加关注字典
#     判断是否是
#     EPOLLIN，是就接收信息，信息为空，取消关注，客户端套接字对象关闭，删除关注字典内的对象

from socket import *
from select import *

#创建关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

#创建epoll
ep = epoll()

#建立查找字典 {fileno:io_obj}
fdmap = {s.fileno():s}

#设置关注IO
ep.register(s,EPOLLIN | EPOLLHUP | EPOLLERR )

#循环监控IO事件发生
while True:
    events = ep.poll()  #阻塞等待IO发生
    print(events)
    #遍历列表处理IO
    for fd,event in events:
        #[(s.fileno,pollin),(c.fileno,pollhup),(c.fileno,pollin)]2,3项位置可能会换
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect From:",addr)
            #添加新的关注事件
            ep.register(c,EPOLLIN|EPOLLHUP)
            fdmap[c.fileno()] = c
        # elif event & EPOLLHUP:  #无法检测到挂起信号
        elif event & EPOLLIN:   #客户端发消息
            data = fdmap[fd].recv(1024)
            # 断开发生时data得到空, 此时pollin也会就绪
            if not data:
                print("客户端退出")
                # 描述符和对象都可以,取消关注
                ep.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]  # 从字典删除
                continue
            print(data.decode())
            fdmap[fd].send(b"OK")

# from socket import *
# from select import *
#
# ep = epoll()
#
# sockfd = socket()
# sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# sockfd.bind(('0.0.0.0',8888))
# sockfd.listen(5)
# ep.register(sockfd,EPOLLIN)
# fdmap = {sockfd.fileno():sockfd}
#
# while True:
#     try:
#         events = ep.poll()
#     except KeyboardInterrupt:
#         print("退出服务器")
#         break
#     for fd,event in events:
#         if fd == sockfd.fileno():
#             connfd,addr = sockfd.accept()
#             print("Connect from",addr)
#             ep.register(connfd,EPOLLIN)
#             fdmap[connfd.fileno()] = connfd
#         elif event & EPOLLIN:
#             data = fdmap[fd].recv(1024)
#             if not data:
#                 print("%s quie"%fdmap[fd].getsockname()[0])
#                 ep.unregister(fd)
#                 fdmap[fd].close()
#                 del fdmap[fd]
#                 continue
#             print(data.decode())
#             fdmap[fd].send(b"OK")