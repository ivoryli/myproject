#　计算密集型函数 x y 传入１，１
'''
10次cpu = 17.55070 秒
10次io = 7.90563 秒

10个进程,10个cpu 用时 9.50886
10个进程,10个io 用时 7.47323

10个线程,10个cpu 用时 22.21684
10个线程,10个io 用时 8.45150
'''

import time
from threading import Thread
from multiprocessing import Process
#
def count(x,y):
    c = 0
    while c < 7000000:
        c += 1
        x += 1
        y += 1

#　io密集型
def io():
    write()
    read()

def write():
    f = open('test.txt','w')
    for i in range(1500000):
        f.write("hello world\n")
    f.close()

def read():
    f = open('test.txt')
    lines = f.readlines()
    f.close()

def count_cpu():
    for x in range(10):
        count(1,1)

def count_io():
    for i in range(10):
        io()

t1 = Thread(target=count_cpu)
times = time.time()
t1.start()
t1.join()
times = time.time() - times
print("10次cpu = %.5f 秒"%times)

t2 = Thread(target=count_io)
times = time.time()
t2.start()
t2.join()
times = time.time() - times
print("10次io = %.5f 秒"%times)
print()
#--------------------------------------------------------------------------------------------------
times = time.time()
jobs = []
for i in range(10):
    p = Process(target=count,args = (1,1))
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

times = time.time() - times
print("10个进程,10个cpu 用时 %0.5f"%times)


times = time.time()
jobs = []
for i in range(10):
    p = Process(target=io)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

times = time.time() - times
print("10个进程,10个io 用时 %0.5f"%times)
print()
#--------------------------------------------------------------------------------------------------

times = time.time()
jobs = []
for i in range(10):
    t = Thread(target=count,args = (1,1))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()

times = time.time() - times
print("10个线程,10个cpu 用时 %0.5f"%times)


times = time.time()
jobs = []
for i in range(10):
    t = Thread(target=io)
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()

times = time.time() - times
print("10个线程,10个io 用时 %0.5f"%times)