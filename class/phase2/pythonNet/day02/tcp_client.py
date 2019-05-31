'''
TCP客户端程序
重点代码
创建,connect服务器,收发,关闭
'''

from socket import *

#创建tcp套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#发起连接
server_addr = ('176.122.17.137', 8888)
sockfd.connect(server_addr)

while True:
    send_data = input("向服务端发送消息:")
    if not send_data:
        break
    #收发消息
    sockfd.send(send_data.encode())
    data = sockfd.recv(1024)
    print("From server:",data.decode())


#关闭套接字
sockfd.close()