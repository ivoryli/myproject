'''
http功能演示
将网页发送给浏览器展示
'''

from socket import *

#处理浏览器的http请求
def handle(connfd):
    print("Request from",connfd.getpeername())
    request = connfd.recv(4096)   #接收http请求
    # print(request)
    #防止客户端断开
    if not request:
        return
    #将request按行分割,得到请求行
    #splitlines使用的可以是str,也可以是bytes，按空格分割
    request_line = request.splitlines()[0].decode()
    # #得到请求内容
    info = request_line.split(" ")[1]

    if info == '/':
        f = open("index.html")
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n"
        response += "\r\n"
        response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type: text/html\r\n"
        response += "\r\n"
        response += "<h1>sorry...</h1>"

    # 向浏览器发送内容
    connfd.send(response.encode())

#搭建tcp网络
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(("0.0.0.0",9000))
    sockfd.listen(3)
    print("Listen the port 9000...")
    while True:
        connfd,addr = sockfd.accept()
        handle(connfd) #处理浏览器请求
        connfd.close()

if __name__ == "__main__":
    main()