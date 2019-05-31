'''
UDP客户端程序
重点代码
创建,收发,关闭
'''

from socket import *

#创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#服务器地址
HOST = '127.0.0.1'
PORT = 9876
ADDR = (HOST,PORT)

#收发消息
while True:
    send_data = input("Msg>>")
    if not send_data:
        break
    sockfd.sendto(send_data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("From server:",msg.decode())

#关闭套接字
sockfd.close()