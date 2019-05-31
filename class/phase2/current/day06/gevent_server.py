'''
gevent协程演示
扩展代码
'''

import gevent
from gevent import monkey
monkey.patch_all() #该语句执行要在导入socket前
from socket import *

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

#创建套接字
sockfd = socket()
sockfd.bind(("0.0.0.0",8888))
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.listen(3)

while True:
    try:
        c,addr = sockfd.accept()
        print("Connect from",addr)
        # handle(c)  #循环方案
        gevent.spawn(handle,c)  #协程方案
    except :
        sockfd.close()