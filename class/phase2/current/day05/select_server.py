'''
IO多路复用select实现多客户端通信
重点代码
'''

from socket import *
from select import select

#设置套接字为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

#设置关注IO
rlist = [s]
wlist = []
xlist = []

while True:
    #监控IO的发生
    rs,ws,xs = select(rlist,wlist,xlist)
    #遍历三个返回值列表,判断哪个IO发生
    for r in rs:
        #如果是套接字就绪则处理链接
        if r is s:
            c,addr = r.accept()
            print("Connect from:",addr)
            rlist.append(c) #加入新的关注IO,不删除对应的c,一直存在,每当有c 客户端有消息发送,select选择对应的c作为返回值
        elif r is c:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            # r.send(b'OK')
            #希望我们主动处理这个IO
            wlist.append(r)
    for w in ws:
        w.send(b'OK,THANKS')
        #不删除会一直调用
        wlist.remove(w)
    for x in xs:
        pass


# from socket import *
# from select import select
#
# sockfd = socket()
# sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# sockfd.bind(('0.0.0.0',8888))
# sockfd.listen(5)
# rlist = [sockfd]
# wlist = []
# xlist = []
#
# while True:
#     rs,ws,xs = select(rlist,wlist,xlist)
#     for r in rs:
#         if r is sockfd:
#             connfd,addr = sockfd.accept()
#             print("Connect from",addr)
#             rlist.append(connfd)
#         elif r is connfd:
#             data = r.recv(1024)
#             if not data:
#                 rlist.remove(r)
#                 r.close()
#                 continue
#             print(data.decode())
#             r.send(b"ok")