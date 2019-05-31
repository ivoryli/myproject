# myself,往文件写名字老师版也是有一大串\0x00

# from socket import *
# import struct
#
# sockfd = socket(AF_INET,SOCK_DGRAM)
# st = struct.Struct('i16sif')
# fd = open("student_info.txt",'w')
#
# server_addr = ('0.0.0.0',9000)
# sockfd.bind(server_addr)
# data,addr = sockfd.recvfrom(1024)
# data = st.unpack(data)
#
# for item in data:
#     if type(item) is bytes:
#         fd.write(item.decode() + " ")
#     else:
#         fd.write(str(item) + " ")
# fd.write("\n")
# fd.close()

from socket import *
import struct

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))

# 　确定数据结构
st = struct.Struct("i32sif")

# 　打开文件
f = open('student.txt', 'a')

while True:
    data, addr = s.recvfrom(1024)
    # 　数据解析
    data = st.unpack(data)

    # 　整理写入内容
    info = "%d  %s  %d  %.2f\n"%(\
        data[0],data[1].decode(), data[2], data[3])

    f.write(info)

f.close()
s.close()
