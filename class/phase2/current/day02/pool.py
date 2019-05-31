'''
进程池原理示例
'''

from multiprocessing import Pool
from time import sleep,ctime

#进程池事件
def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

#创建进程池
# pool = Pool(4)   #进程个数
pool = Pool()     #默认根系统内核个数一致

#向进程池添加事件
for i in range(20):
    msg = "Hello %d"%i
    r = pool.apply_async(func = worker,args = (msg,))  #返回函数事件对象
    # print(r)  #<multiprocessing.pool.ApplyResult object at 0x7fa2f351e7b8>
#关闭进程池   #先关闭，但进程还在执行，直到join把进程池中的进程全部回收
pool.close()

#回收进程池
pool.join()

print(r.get())  #获取事件函数返回值