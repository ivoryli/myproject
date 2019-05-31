'''
dict客户端
发起请求,展示结果
'''

from socket import *
from getpass import getpass

ADDR = ('127.0.0.1',8888)

# 所有函数都有sockfd
sockfd = socket()
sockfd.connect(ADDR)

#查历史记录
def do_query_history_client(name):
    msg = "H %s"%name
    sockfd.send(msg.encode())
    data = sockfd.recv(128).decode()
    if data == "OK":
        while True:
            data = sockfd.recv(1024).decode()
            if data == "##":
                break
            print(data)
    else:
        print("没有该记录")

#查单词
def do_query_client(name):
    while True:
        word = input("Word:")
        if word == '##':    #结束单词查询
            break
        msg = "Q %s %s"%(name,word)
        sockfd.send(msg.encode())
        data = sockfd.recv(2048).decode()
        print(data)

#二级界面
def login(name):
    while True:
        print("""
        =======================Query=======================
        　　　1.查单词           2.历史记录             3.注销
        ====================================================
        """)
        cmd = input("输入选项:")
        if cmd == '1':
            do_query_client(name)
        elif cmd == '2':
            do_query_history_client(name)
        elif cmd == '3':
            return
        else:
            print("请输入正确命令")

#注册
def do_register_client():
    while True:
        name = input("User:")
        if not name:
            break
        passwd = getpass()
        passwd1 = getpass("Again:")
        if (" " in name) or (" " in passwd):
            print('用户名或密码不能有空格')
            continue
        if passwd != passwd1:
            print("两次密码不一致")
            continue
        msg = "R %s %s"%(name,passwd)
        #发送请求
        sockfd.send(msg.encode())
        #接受反馈
        data = sockfd.recv(128).decode()
        if data == 'OK':
            print('注册成功')
            login(name)
        else:
            print("注册失败")
        return

#登录
def do_login_client():
    name = input("User:")
    passwd = getpass()
    msg = "L %s %s"%(name,passwd)
    sockfd.send(msg.encode())
    data = sockfd.recv(128).decode()
    if data == 'OK':
        print('登录成功')
        login(name)
    else:
        print("登录失败")
    return

#创建网络链接
def main():
    while True:
        print("""
        =======================Welcome=======================
        　　　1.注册           2.登录             3.退出
        =====================================================
        """)
        cmd = input("输入选项:")
        if cmd == '1':
            do_register_client()
        elif cmd == '2':
            do_login_client()
        elif cmd == '3':
            sockfd.send(b"E")
            print("感谢使用!")
            return
        else:
            print("请输入正确命令")

if __name__ =='__main__':
    main()