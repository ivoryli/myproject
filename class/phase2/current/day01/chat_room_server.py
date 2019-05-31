'''
chat room
env: python3.5
socket fork 练习
'''

from socket import *
import os,sys

#服务器地址
ADDR = ("176.122.17.77",8888)
#存储用户信息
user = {}

#进入聊天室
def do_login(sockfd,name,addr):
    if name in user or "管理员" in name:
        sockfd.sendto("\n该用户已存在".encode(),addr)
        return

    sockfd.sendto(b'OK',addr)

    #通知其他人
    msg = "\n欢迎%s进入聊天室"%name
    for i in user:
        sockfd.sendto(msg.encode(),user[i])

    #将用户加入
    user[name] = addr

#聊天
def do_chat(sockfd,name,text):
    msg = "\n%s : %s"%(name,text)
    for i in user:
        if i != name:
            sockfd.sendto(msg.encode(),user[i])

#退出
def do_quit(sockfd,name):
    msg = "\n%s退出了聊天室"%name
    for i in user:
        if i != name:
            sockfd.sendto(msg.encode(),user[i])
        else:
            sockfd.sendto(b'EXIT',user[i])

    #将用户删除
    del user[name]


#接收各种客户端请求
def do_request(sockfd):
    while True:
        data,addr = sockfd.recvfrom(1024)
        msg = data.decode().split(' ')
        #区分请求类型
        if msg[0] == "L":
            do_login(sockfd,msg[1],addr)
        if msg[0] == "C":
            text = " ".join(msg[2:])
            do_chat(sockfd,msg[1],text)
        if msg[0] == "Q":
            if msg[1] not in user:
                sockfd.sendto(b'EXIT',addr)
                continue
            do_quit(sockfd,msg[1])

#创建网络连接
def main():
    #套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        return
    #发送管理员消息
    elif pid == 0:
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员消息 " + msg
            s.sendto(msg.encode(),ADDR)
    else:
        # 请求处理
        do_request(s)  # 处理客户端请求


    s.close()

if __name__ == '__main__':
    main()
