from socket import *
from multiprocessing import Process
import sys
import signal

def handle(c):
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()

#创建监听套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

sockfd = socket() #tcp套接字
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(3)

#处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

# 循环等待客户端连接
while True:
    try:
        c,addr = sockfd.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue
    #创建新的线程处理客户端请求
    p = Process(target = handle,args=(c,))
    p.daemon = True  #子进程随父进程退出
    p.start()
