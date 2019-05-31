'''
获取时分秒算总秒数
'''

hour = int(input("输入小时："))
minute = int(input("输入分钟："))
second = int(input("输入秒数："))

print("输入的一共：" + str(hour * 60 * 60 +  minute * 60 + second) + "秒")