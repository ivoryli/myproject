'''
获取总秒数,算几时几分几秒
'''

n = int(input("输入秒数"))

# hour = n // 3600
# minute = n % 3600 // 60
# second = n % 3600 % 60

second = n % 60 #商指的是分钟，余数是指剩下的秒数
minute = n // 60 % 60  #n//60商指的是分钟数,
hour = n // 3600

print(hour,minute,second)