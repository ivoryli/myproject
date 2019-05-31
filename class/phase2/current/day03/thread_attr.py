'''
不能用exit，那是进程的
'''

from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

# t = Thread(target=fun)  #getName:Thread-1
t = Thread(target=fun,name = "Tarena") #getName:Tarena
t.setName("Tedu") #getName:Tedu

#线程名称
print("Thread name:",t.getName())

#线程生命周期
print("is alive:",t.is_alive())  #False

#主线程退出,分支线程也退出
t.setDaemon(True)   #运行此命令,不会print("线程属性测试")

t.start()
print("is alive:",t.is_alive())  #True
