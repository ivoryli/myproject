#广播发送

from socket import *
from time import sleep

#广播地址
dest = ("176.122.17.255",9999)

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("".encode(),dest)

s.close()