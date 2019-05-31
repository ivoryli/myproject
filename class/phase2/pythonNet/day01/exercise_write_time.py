# 每隔1秒向文件test.txt中写入一行数据，格式如下
# 1.2019 - 7 - 30 12: 12:12
# 2.2019 - 7 - 30 12: 12:13
# 3.2019 - 7 - 30 12: 12:19
# .....
# 2.该程序无限循环，ctrl - c退出
# 3.当重启程序时，内容会继续向下写，序号能够接上之前的

#myself  no good
# import time
# fd = open("test.txt","r+")
#
# data = fd.readlines()
# if data:
#     #myself bug:多于一位就出错
#     #有一种方法split拿第一个元素
#     # head = int(data[-1][0]) + 1
#     head = len(data) + 1
# else:
#     head = 1
#
# while True:
#     L = []
#     for item in time.localtime(time.time())[:3]:
#         L.append(str(item))
#     str1 = "-".join(L)
#     L = []
#     for item in time.localtime(time.time())[3:6]:
#         L.append(str(item))
#     str2 = "-".join(L)
#
#     wdata = "%s %s %s\n"%(str(head),str1,str2)
#     fd.write(wdata)
#     head += 1
#     time.sleep(1)
#
# fd.close()

#李玉辉
# import time
# fo=open('test.txt','a+')
# fo.seek(0,0)
# len_num = len(fo.readlines())
# count = len_num if len_num else 0
# while True:
#     count+=1
#
#     fo.writelines(['%d.\t'%(count),time.strftime('%Y %m %d %H:%M:%S',time.localtime()),'\n'])
#     time.sleep(1)
#     fo.flush()
# fo.close()

#teacher
import time
f = open('test.txt','a+')

f.seek(0)

n = 1
for line in f:
    n += 1

while True:
    time.sleep(1)
    s = "%d. %s\n"%(n,time.ctime())
    f.write(s)
    f.flush()
    n += 1
