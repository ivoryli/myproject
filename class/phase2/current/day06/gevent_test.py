import gevent
import time

def foo(a,b):
    print("Runing foo...",a,b)
    gevent.sleep(2)
    print("Foo again")

def bar():
    print("Running bar...")
    gevent.sleep(3)
    print("Bar again")

#将函数封装为协程,遇到gevent阻塞自动运行
f = gevent.spawn(foo,1,"hello")
g = gevent.spawn(bar)


# time.sleep(2)  #普通阻塞不能执行gevent
# gevent.sleep(2)

gevent.joinall([f,g])  #等待f,g结束