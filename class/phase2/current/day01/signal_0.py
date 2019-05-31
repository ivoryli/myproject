'''
信号方法处理僵尸
'''

import os
import signal

#处理子进程退出
# 子进程发出退出信号后父进程进行忽略
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()

if pid < 0:
    pass
elif pid == 0:
    print("Child PID: ",os.getpid())
else:
    while True:
        pass