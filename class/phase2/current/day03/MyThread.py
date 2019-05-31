from threading import Thread
from time import sleep,ctime

class MyThread(Thread):
    #myself
    # def __init__(self,target=None,name=None,
    #              args=(), kwargs=None ):
    #     super(self.__class__, self).__init__()
    #     self._target = target
    #     self._args = args
    #     self._kwargs = kwargs
    #     self._name = str(name)

    #teacher
    def __init__(self,target = None,args = (),kwargs = {},name = 'tedu'):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.name = name

    def run(self):
        self.target(*self.args,**self.kwargs)

#--------------------------------------------------------------------------------------------------
# 通过完成上面MyThread类让整个程序可以正常执行
# 当调用start时player作为一个线程功能函数执行
# 注意，函数的名称和参数并不确定,player只是测试函数
#--------------------------------------------------------------------------------------------------

def player(sec,song):
    for i in range(2):
        print("Playing %s:%s"%(song,ctime()))
        sleep(sec)

t = MyThread(target = player,args = (3,),kwargs = {'song':'凉凉'},name = 'happy')

t.start()
t.join()