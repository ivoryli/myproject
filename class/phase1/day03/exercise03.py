# star = int(input("开始值"))
# end = int(input("结束值"))
#
# while end - 1 > star:
#     star += 1
#     print(star,end = " ")

#----------------------------------------------------------------

#一张纸厚度为0.01毫米,对折多少次比8844.43米高的珠穆朗玛峰还高


thickness = 0.01 * 10 ** -3

count = 0
while thickness < 8844.43:
    count += 1
    thickness *= 2

print(count)
