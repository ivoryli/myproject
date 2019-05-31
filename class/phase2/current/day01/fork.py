'''
fork函数展示
'''

import os
import time

pid = os.fork()

if pid < 0 :
    print("Create process failed")

elif pid == 0:
    time.sleep(2)
    print("The new process")
else:
    time.sleep(3)
    print("The old process")

print("Fock test over")