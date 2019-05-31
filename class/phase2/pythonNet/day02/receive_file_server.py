#myself
# from socket import *
#
# sockfd = socket()
#
#
# sockfd.bind(("0.0.0.0", 8888))
#
# sockfd.listen(5)
#
# print("waiting for connect......")
# connfd,addr = sockfd.accept()
#
# suffix = connfd.recv(4)
#
# fd = open("test%s"%suffix.decode(),"wb")
#
# while True:
#     data = connfd.recv(1024)
#     if not data:
#         break
#     fd.write(data)
#
# connfd.close()
# sockfd.close()
# fd.close()

from socket import *

s = socket()

s.bind(('0.0.0.0',8888))
s.listen(5)

c,addr = s.accept()
print("Connect from:",addr)

f = open("new.jpg","wb")

while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()