'''
套接字非阻塞示例
'''

from socket import *
from time import sleep,ctime

#日志文件
f = open("log.txt","a+")

sockfd = socket()
sockfd.bind(("0.0.0.0",8888))
sockfd.listen(3)

#设置套接字为非阻塞
# sockfd.setblocking(False)

#超时检测
sockfd.settimeout(3)

while True:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept()
    except (BlockingIOError,timeout) as e:
        #每隔两秒写入一条日志
        sleep(2)
        f.write("%s : %s\n"%(ctime(),e))
        f.flush()
    else:
        data = connfd.recv(1024)
        print(data)