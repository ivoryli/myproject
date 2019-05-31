'''
基于fork的多进程网络并发
重点代码
'''

from socket import *
import os,sys
import signal

#客户端处理函数
def handle(c):
    print("客户端地址:",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

#创建监听套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
sockfd = socket() #tcp套接字
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(10)

#僵尸进程处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen the port 8888.....")

#循坏等待客户端连接
while True:
    try:
        connfd, addr = sockfd.accept()
    except KeyboardInterrupt:
        print("服务器退出")
    except Exception as e:
        print(e)
        continue
    else:#可有可无
        #创建子进程处理客户端请求
        pid = os.fork()
        if pid == 0:
            sockfd.close()  #子进程不需要sockfd
            handle(connfd)  #具体处理客户端请求
            os._exit(0)
        #父进程实际只用来处理客户端连接
        else:
            connfd.close()  #父进程不需要connfd