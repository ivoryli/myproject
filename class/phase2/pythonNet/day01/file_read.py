#文件的读取操作

#打开文件返回文件对象
fd = open("code")

#读操作
# while True:
#     data = fd.read(1)
#     if not data:
#         break
#     print("读取到的内容:",data)

# data = fd.readline(2)
# data1 = fd.readline()
# print("读取到的内容:",data)
# print("读取到的内容:",data1)

# data = fd.readlines(2)
# print("读取到的内容:",data)

for line in fd:
    print("读取到的内容:",line)

#关闭文件
fd.close()