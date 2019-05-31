'''
 猜数字
'''
import random

random_number = random.randint(1,100)
# g = 0
# while n != g:
#     g = int(input("猜数字"))
#     if n > g:
#         print("猜小了")
#     else:
#         print("猜大了")
#
# print("猜中了:",n)

count = 0
while count < 10:
    count += 1
    input_number = int(input("第%d次猜数字"%count))
    if input_number > random_number :
        print("猜大了")
    elif input_number < random_number:
        print("猜小了")
    else:
        print("猜对了")
        break   #不执行else

else:
    # while 结束循环执行
    print("没机会了")