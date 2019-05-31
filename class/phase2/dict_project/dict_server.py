'''
dict服务端
处理请求逻辑
'''
from socket import *
from multiprocessing import Process
from time import sleep
import signal
import sys

from operation_db import *

#全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

#查询历史记录
def do_query_history_server(c,db,data):
    name = data.split(" ")[1]
    history_list = db.query_history(name)
    print(history_list)
    if not history_list:
        c.send(b'Fail')
        return
    else:
        c.send(b'OK')
        sleep(0.1)
        for i in history_list:
            #i ----> (name,word,time)
            msg = "%s   %s   %s"%i
            c.send(msg.encode())
            sleep(0.1)   #防止沾包
        c.send(b"##")


#处理查单词
def do_query_server(c,db,data):
    tmp = data.split(" ")
    name = tmp[1]
    word = tmp[2]

    #插入历史记录
    db.insert_history(name,word)

    #查单词   没有查到返回None
    explain = db.query(word)
    if not explain:
        c.send("没有找到该单词!".encode())
    else:
        msg = "%s : %s"%(word,explain)
        c.send(msg.encode())


#处理注册
def do_register_server(c,db,data):
    tmp = data.split(" ")
    name = tmp[1]
    passwd = tmp[2]

    if db.register(name,passwd):
        c.send(b"OK")
    else:
        c.send(b"Fail")


#处理登录
def do_login_server(c,db,data):
    tmp = data.split(" ")
    name = tmp[1]
    passwd = tmp[2]

    if db.login(name,passwd):
        c.send(b"OK")
    else:
        c.send(b"Fail")


#处理客户端请求
def do_request(c,db):
    db.create_cursor()  #生成游标   db.cur
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(),":",data)
        if not data or data[0] == "E":
            c.close()
            sys.exit("客户端退出")
        elif data[0] == "R":
            do_register_server(c,db,data)
        elif data[0] == "L":
            do_login_server(c,db,data)
        elif data[0] == "Q":
            do_query_server(c,db,data)
        elif data[0] == "H":
            do_query_history_server(c,db,data)

#网络连接
def main():
    #创建数据库链接对象
    db = Database()

    #创建tcp套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    #等待客户端链接
    print("Listen the port 8888")
    while True:
        try:
            c,addr = sockfd.accept()
            print('Connect from',addr)
        except KeyboardInterrupt:
            db.close()
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        #创建子进程
        p = Process(target=do_request,args=(c,db))
        p.daemon = True
        p.start()

if __name__ == "__main__":
    main()