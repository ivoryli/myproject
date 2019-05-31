'''
模拟http协议的服务器
'''

from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8003))      #模拟服务器，可以接收所有ip地址，相同端口就可以访问
s.listen(3)

c,addr = s.accept()   #接收浏览器请求
print("Connect from:",addr)

data = c.recv(4096)
print(data)     #请求行，请求头，空行，请求体

f = open("index.html")
str_data = "".join(f.readlines())

# str_data = '''
# <meta charset="UTF-8">   #有这句html才能显示中文
# <h1>达内Python学院欢迎你</h1>
# <p>大吉大利，今晚吃鸡</p>
# '''

#http响应格式
data = """HTTP/1.1 200 ok
Content-Type:text/html

%s
"""%str_data

c.send(data.encode())

c.close()
s.close()