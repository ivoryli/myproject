from socket import *
import sys,time

#具体功能
class FtpClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')   #发送请求
        #等待回复
        data = self.sockfd.recv(128).decode()
        #ok表示请求成功
        if data == 'OK':
            #接受文件列表
            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用!")

    def get_file(self,file_name):
        #发送请求
        self.sockfd.send(("G " + file_name).encode())
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            new = open("./new/%s"%file_name, "wb")
            while True:
                data = self.sockfd.recv(1024)
                #服务端设置(sleep)
                if data == b'##':
                    break
                new.write(data)
            new.close()
        else:
            print(data)
        # self.sockfd.close()   #下次还要循环用

    def put_file(self,file_name):
        try:
            fd = open(file_name, "rb")
        except Exception:
            print("没有该文件")
            return

        filename = file_name.split("/")[-1]
        self.sockfd.send(('P ' + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = fd.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            fd.close()
        else:
            print(data)

#发起请求
def request(sockfd):
    ftp = FtpClient(sockfd)

    while True:
        print("\n=======命令选项=======")
        print('''
        list
      get  file
      put  file
        quit
        ''')
        cmd = input("输入命令:")
        if cmd == 'list':
            ftp.do_list()
        elif cmd[:3] == 'get':
            filename = cmd.strip().split(" ")[-1]
            ftp.get_file(filename)
        elif cmd == 'put':
            file_name = input("输入上传的文件路径及文件名:")
            ftp.put_file(file_name)
        elif cmd == 'quit':
            ftp.do_quit()
        else:
            print("没有该选项")
            continue

#网络连接
def main():
    sockfd = socket()
    #服务器地址
    addr = ('176.122.17.137', 8888)
    try:
        sockfd.connect(addr)
    except Exception:
        print("链接服务器失败")
        return
    else:
        print('''
            Data
            File
            Image
        ''')
        cls = input("请选择文件种类:")
        if cls not in ("Data","File","Image"):
            print("Sorry input Error!!")
            return
        else:
            sockfd.send(cls.encode())
            request(sockfd)  #发起具体请求

if __name__ == "__main__":
    main()