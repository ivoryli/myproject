fd = open("code","r+")

fd.write("hello world")
# fd.flush()
fd.seek(0,0)   #第二个参数,解决偏移量问题，0头，1当前位置，2末尾
data = fd.read()
print(data)  #没显示，偏移量到尾部，没有内容可读取
fd.close()