from socket import *
import os,sys

#服务器地址
ADDR = ('176.122.17.77',8888)

#发送信息
def send_msg(sockfd,name):
    while True:
        try:
            text = input("发言:")
        except KeyboardInterrupt:
            text = "quit"
        #退出聊天室
        if text == "quit":
            msg = "Q " + name
            sockfd.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")

        msg = "C %s %s"%(name,text)
        sockfd.sendto(msg.encode(),ADDR)

#接收信息
def recv_msg(sockfd):
    while True:
        data,addr = sockfd.recvfrom(2048)
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode() + '\n发言：',end = "")

#创建网络连接
def main():
    sockfd = socket(AF_INET, SOCK_DGRAM)
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    while True:
        name = input("请输入姓名:")
        msg = "L " + name
        sockfd.sendto(msg.encode(),ADDR)
        #等待回应
        data,addr = sockfd.recvfrom(1024)
        if data.decode() == "OK":
            print("lockin")
            break
        else:
            print(data.decode())

    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_msg(sockfd,name)
    else:
        recv_msg(sockfd)

if __name__ == "__main__":
    main()
