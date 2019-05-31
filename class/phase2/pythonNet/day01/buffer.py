#缓冲区示例

# fd = open("code","w",0) #0 不允许无缓冲
# fd = open("code","w",1)   #1 行缓冲，遇到\n写入
# fd = open("code","w",12)   #>1  指定缓冲区大小(不识别)
fd = open("code","w")   #系统默认缓冲区大小

while True:
    s = input(">>")
    if not s:
        break
    fd.write(s)
    fd.flush()   #立即刷新缓冲,将内容写入磁盘
fd.close()