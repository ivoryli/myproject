#从终端输入文件，进行复制

filename = input("输入文件名称(可以夹带路径):")

try:
    fd = open(filename, "rb")
except FileNotFoundError:
    print("没有该文件")
else:
    data = fd.read()

    fd.close()

try:
    point = filename.index(".")
except ValueError:
    point = None
try:
    fd = open("new%s" % filename[point:], "wb")
except FileNotFoundError:
    print("没有该文件")
else:
    fd.write(data)

    fd.close()


#teacher
# filename = input("输入文件名称(可以夹带路径):")
#
# try:
#     fd = open(filename, "rb")
# except FileNotFoundError:
#     print("没有该文件")
# else:
#     fw = open("myfile","wb")
#     while True:
#         data = fd.read(1024)
#         if not data:
#             break
#         fw.write(data)
#     fd.close()
#     fw.close()