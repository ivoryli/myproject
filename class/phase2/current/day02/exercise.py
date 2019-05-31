'''
复制文件分上下两部分，用两个进程实现
'''

#myself
# from multiprocessing import Process
#
# ft = open("Process_copy.txt","w")
# for i in range(2050):
#     ft.write("f")
# for j in range(2050):
#     ft.write("s")
# ft.close()
#
#  a为了获取最后seek
# fd = open("Process_copy.txt", "ab+")  #open放在父进程会出问题,每一部分一定要设定seek
# part = fd.tell() // 2
# # print(part)
#
# def part1(fd,part):
#     new1 = open("new1.txt", "w")
#     fd.seek(0)
#     L = [1024,100,10,1]
#     for i in range(len(L)):
#         if part >= L[i]:
#             times = part // L[i]
#             for x in range(times):
#                 data = fd.read(L[i])
#                 # print(data)
#                 new1.write(data)
#             part -= times * L[i]
#             # print(part)
#     new1.close()
#
# def part2(fd,part):
#     new2 = open("new2.txt", "w")
#     fd.seek(part)
#     while True:
#         data = fd.read(1024)
#         if not data:
#             break
#         new2.write(data)
#     new2.close()
#
#
# p1 = Process(target=part1,args=(fd,part))
# p2 = Process(target=part2,args=(fd,part))
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
#
# fd.close()

#teacher
from multiprocessing import Process

# fd = open("Process_copy.txt")
filename = 'a7691515_s.jpg'

#获取图片大小
size = os.path.getsize(filename)

#复制上半部分
def top():
    f = open(filename,"rb")
    n = size // 2
    fw = open("new1.jpg","wb")
    fw.write(f.read(n))
    f.close()
    fw.close()

#复制下半部分
def botton():
    f = open(filename,"rb")
    fw = open("new2.jpg","wb")
    f.seek(size // 2)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

p1 = Process(target = top)
p2 = Process(target = botton)
p1.start()
p2.start()
p1.join()
p2.join()