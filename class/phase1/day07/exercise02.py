'''
   根据天/分钟/小时,计算总秒数
'''

def count_second(minute = 0,hour = 0,day = 0):
    return day * 86400 + hour * 3600 + minute * 60

print(count_second(1))
print(count_second(0,5))
print(count_second(3,1,6))
