# from socket import *
# import struct
#
# id = int(input("请输入学生id:"))
# name = input("请输入学生姓名:")
# age = int(input("请输入学生年龄:"))
# score = float(input("请输入学生分数:"))
#
# st = struct.Struct('i16sif')
# sockfd = socket(AF_INET,SOCK_DGRAM)
# sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# dest = ('127.0.0.1',9000)
# name = name.encode()
# data = st.pack(id,name,age,score)
# sockfd.sendto(data,dest)

from socket import *
import struct

#　接收端地址
ADDR = ('127.0.0.1',8888)

#　规定数据格式
st = struct.Struct('i32sif')

s = socket(AF_INET,SOCK_DGRAM)

while True:
    print("=================================")
    id = int(input("ID:"))
    name = input("NAME:").encode()
    age = int(input("AGE:"))
    score = float(input("SCORE:"))

    #　数据打包
    data = st.pack(id,name,age,score)

    s.sendto(data,ADDR)

s.close()
