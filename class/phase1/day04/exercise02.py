import time

t = 120

while t > 0:
    minute = t // 60
    second = t % 60
    print("时间：%02d,%02d" %(minute,second) ,end='\r')#pycharm没办法在同一行显示,文件式可以
    time.sleep(1)
    t -= 1
print("到时间了")