#消息队列通信   通过消息包传递
#  在同一时刻，只能有一个进程来取值，它内部有一个锁的机制。那么另外一个进程就会阻塞一会，但是阻塞的时间非常短
#  队列能保证数据安全，同一个数据，不能被多个进程获取。

from multiprocessing import Queue,Process
from time import sleep
from random import  randint

#创建消息队列
# q = Queue(5)   自定义队列大小 5 个    Queue(maxsize = 0) 默认值是根据内存大小存放个数
#
# def request():
#     for i in range(20):
#         x = randint(0,100)
#         y = randint(0,100)
#         q.put((x,y))
#
# def handle():
#     while True:
#         sleep(0.5)
#         try:
#             x,y = q.get(timeout = 3)
#         except:
#             break
#         else:
#             print("%d + %d = %d"%(x,y,x+y))
#
# p1 = Process(target=request)
# p2 = Process(target=handle)
# p1.start()
# p2.start()
# p1.join()
# p2.join()

# import time
# from multiprocessing import Process, Queue
#
#
# def wahaha(q):
#     print(q.get())   #1  q.get()阻塞，直到主进程put(1)
#     q.put(2)  # 增加数字2
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=wahaha, args=[q, ])
#     p.start()
#     q.put(1)  # 增加数字1
#     time.sleep(0.1)
#     print(q.get())   #2  q.get()阻塞，直到子进程put(2)

# 生产者消费者模型,解决数据供需不平衡的情况
# https://www.cnblogs.com/xiao987334176/articles/9036763.html

import time
import random
from multiprocessing import Process, Queue


def producer(q, name, food):
    for i in range(5):
        time.sleep(random.random())  # 模拟生产时间
        print('{}生产了{}{}'.format(name, food, i))
        q.put('{}{}'.format(food, i))  # 放入队列


def consumer(q, name):
    while True:
        food = q.get()  # 获取队列
        if food == 'done': break  # 当获取的值为done时,结束循环
        time.sleep(random.random())  # 模拟吃的时间
        print('{}吃了{}'.format(name, food))


if __name__ == '__main__':
    q = Queue()  # 创建队列对象，如果不提供maxsize，则队列数无限制
    p1 = Process(target=producer, args=[q, '康师傅', '红烧牛肉'])
    p2 = Process(target=producer, args=[q, '郑师傅', '红烧鱼块'])
    p1.start()  # 启动进程
    p2.start()
    Process(target=consumer, args=[q, 'xiao']).start()
    Process(target=consumer, args=[q, 'lin']).start()
    p1.join()  # 保证子进程结束后再向下执行
    p2.join()
    q.put('done')  # 向队列添加一个值done
    q.put('done')

# import time
# import random
# from multiprocessing import Process, JoinableQueue
#
#
# def producer(q, name, food):
#     for i in range(5):
#         time.sleep(random.random())  # 模拟生产时间
#         print('{}生产了{}{}'.format(name, food, i))
#         q.put('{}{}'.format(food, i))
#         q.join()  # 等到所有的数据都被task_done才结束
#
#
# def consumer(q, name):
#     while True:
#         food = q.get()  # 获取队列
#         time.sleep(random.random())  # 模拟吃的时间
#         print('{}吃了{}'.format(name, food))
#         q.task_done()  # 向q.join()发送一次信号,证明一个数据已经被取走了
#
#
# if __name__ == '__main__':
#     q = JoinableQueue()  # 创建可连接的共享进程队列
#     # 生产者们:即厨师们
#     p1 = Process(target=producer, args=[q, '康师傅', '红烧牛肉'])
#     p2 = Process(target=producer, args=[q, '郑师傅', '红烧鱼块'])
#     p1.start()  # 启动进程
#     p2.start()
#     # 消费者们:即吃货们
#     c1 = Process(target=consumer, args=[q, 'xiao'])
#     c2 = Process(target=consumer, args=[q, 'lin'])
#     c1.daemon = True  # 设置守护进程
#     c2.daemon = True
#     c1.start()  # 启动进程
#     c2.start()
#     p1.join()  # 保证子进程结束后再向下执行
#     p2.join()