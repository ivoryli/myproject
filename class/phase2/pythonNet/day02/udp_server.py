'''
UDP服务端套接字
重点代码
创建,绑定地址,收发,关闭
'''

from socket import *

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
server_addr = ('0.0.0.0',9876)
sockfd.bind(server_addr)

#收发消息
while True:
    data,addr = sockfd.recvfrom(1024)
    print("Connect from:",addr)
    print("收到的消息:",data.decode())
    sockfd.sendto(b"Thanks",addr)

#关闭套接字
sockfd.close()