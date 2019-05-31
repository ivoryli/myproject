"""
ftp 文件服务器
并发网络功能训练

1. 功能
    【1】 分为服务端和客户端，要求可以有多个客户端同时操作。
    【2】 客户端可以查看服务器文件库中有什么文件。
    【3】 客户端可以从文件库中下载文件到本地。
    【4】 客户端可以上传一个本地文件到文件库。
    【5】 使用print在客户端打印命令输入提示，引导操作
"""
"""
    1.技术点分析：
        *并发模型  多线程并发模式
        *数据传输  tcp传输
    2.结构设计
        *客户端发起请求，打印请求提示界面
        *文件传输功能封装为类
    3.功能分析
        *网络搭建
        *查看文件库信息
        *下载文件
        *上传文件
        *客户端退出
    4.协议
        L 请求列表


"""
from socket import *
from threading import Thread
import os
from time import sleep

# 全局变量
HOST = "0.0.0.0"
PORT = 8080
ADDR = (HOST, PORT)
FTP = "../Ftp/"  # 文件库路径


# 将客户端请求功能封装为类
class Ftpserver:
    def __init__(self, connfd, FTP_PATH):
        self.connfd = connfd
        self.path = FTP_PATH

    def do_list(self):
        # 获取文件列表
        files = os.listdir(self.path)
        if not files:
            self.connfd.send("该文件类别为空".encode())
            return
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
        fs = ''
        for file in files:
            if file[0] != "." and os.path.isfile(self.path + file):
                fs += file + "\n"
        self.connfd.send(fs.encode())
        # self.connfd.send(b"##")

    def do_get(self, filename):
        try:
            fd = open(self.path + filename, "rb")
        except Exception:
            self.connfd.send("文件不存在")
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        # 发送文件内容
        while True:
            data = fd.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    def do_put(self, filename):
        if os.path.exists(self.path + filename):
            self.connfd.send("该文件存在".encode())
            return
        self.connfd.send(b'OK')
        fd = open(self.path + filename, "wb")
        # 接收文件
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()


# 客户端请求函数
def handle(connfd):
    # 选择文件夹
    cls = connfd.recv(1024).decode()
    FTP_PATH = FTP + cls + '/'
    ftp = Ftpserver(connfd, FTP_PATH)
    while True:
        # 接收客户端请求
        data = connfd.recv(1024).decode()
        print(FTP_PATH, ":", data)
        # 如果客户端断开，返回data为空
        if not data or data[0] == "Q":
            return
        elif data[0] == "L":
            ftp.do_list()
        elif data[0] == "G":
            filename = data.split(" ")[-1]
            ftp.do_get(filename)
        elif data[0] == "P":
            filename = data.split(" ")[-1]
            ftp.do_put(filename)


# 网络搭建
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    print("listen the port 8888...")
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            print("退出服务程序")
            return
        except Exception as e:
            print(e)
            continue
        print("链接的客户端：", addr)
        # 创建线程处理请求
        client = Thread(target=handle, args=(connfd,))
        client.setDaemon(True)
        client.start()


if __name__ == "__main__":
    main()
