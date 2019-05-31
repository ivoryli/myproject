import os


pid = os.fork()

if pid < 0:
    print("Error")

elif pid == 0:
    print("Child Process:",os.getpid())
else:
    while True:
        pass