# 1.使用tcp服务和客户端编程，将一个文件从客户端发送到服务端，文件类型为图片或普通文本皆可
#扩展:判断文件类型,目前server里收到的是4字节，传输文件是.jpg 4个字节的，后缀没问题，.py文件缺一个字节，生成的文件后缀会多一个字符。
#收发确认信息会导致进程错误

# from socket import *
#
# path = input("请输入文件及文件路径:")
#
# fd = open(path,"rb")
#
#
# sockfd = socket()
# server_addr = ('127.0.0.1', 8888)
# sockfd.connect(server_addr)
#
# index = path.index(".")
# path_suffix = path[index:]
# print(path_suffix)
# sockfd.send(path_suffix.encode())
#
# while True:
#     data = fd.read(1024)
#     if not data:
#         break
#     sockfd.send(data)
#
# sockfd.close()
# fd.close()

from socket import *
s = socket()
s.connect(('127.0.0.1',8888))

f = open("/home/tarena/class/phase2/pythonNet/day01/a7691515_s.jpg","rb")

while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()