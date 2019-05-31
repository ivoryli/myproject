'''
select函数讲解
'''

from select import select
from socket import *

#做几个io用来监控
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

fd = open('log.txt',"w")

print("开始提交监控的IO")
rs,ws,xs = select([s],[fd],[])

print("rs:",rs)
print("ws:",ws)
print("xs:",xs)