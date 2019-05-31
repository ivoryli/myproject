
try:
    fd = open("code","r+")
except FileExistsError as e:
    print(e)
else:
    print("打开成功")
    s = fd.read()
    print(s)
    fd.close()