'''
父进程的fock返回值是子进程的pid
'''

import os
import time

pid = os.fork()

if pid < 0:
    print("Error")

elif pid == 0:
    # print(pid)
    time.sleep(2) #主进程退出子进程也会退出
    print("child pid :",os.getpid())
    print("Get parent pid:",os.getppid())

else:
    # print(pid)
    print("Parent pid:",os.getpid())
    print('Get child pid',pid)