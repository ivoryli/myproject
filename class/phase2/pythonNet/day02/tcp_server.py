'''
TCP套接字服务端
重点代码
#创建,bind(可允许访问),listen,accept,收发,关闭
'''

import socket

#创建流式套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
server_ip = ('0.0.0.0', 9876)
sockfd.bind(server_ip)

#设置监听
sockfd.listen(5)

#等待处理客户端连接
while True:
    print("waiting for connect......")
    try:
        connfd,addr = sockfd.accept()
        print("Connect from:",addr)
    except KeyboardInterrupt:
        print("退出服务")
        break
    while True:
        #收发消息
        data = connfd.recv(1024)
        if not data:
            break
        print("接收到的消息:",data.decode())

        n = connfd.send(b'Receive your message')
        print("发送了%d个字节数据"%n)

    #关闭套接字
    connfd.close()
sockfd.close()
