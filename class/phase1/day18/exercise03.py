'''
   为学生的学习方法,添加新功能(统计执行时间)
'''

#teacher
# def print_execute_time(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         stop = time.time()
#         total_time = stop - start
#         print(total_time)
#         return result
#     return wrapper

def total_time(func):
    total_time = 0
    def wrapper(*args,**kwargs):
        nonlocal total_time
        start = time.time()
        func(*args,**kwargs)
        stop = time.time()
        total_time += stop - start
        return total_time
    return wrapper

import time

class Student:
    def __init__(self,name):
        self.name = name

    @total_time
    def stay(self):
        print("开始学习了")
        time.sleep(2) #模拟学习两秒

s1 = Student("zs")
times = s1.stay()
print(times)
times = s1.stay()
print(times)