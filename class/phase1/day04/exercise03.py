'''
输入字符串,显示第一,中间(奇数才有),最后一个,倒数后第3个,倒叙字符
'''

# n = input("输入一串字符")
# print(n)
# print(n[0])
# print(n[-1])
# if len(n) % 2 == 1:
#     print(n[len(n)//2])
# print(n[-1:-4:-1])
# print(n[::-1])

'''
输入一个数,打印以那是为边的矩方形
'''

n = int(input("输入一个数"))

print('*' * n)
for i in range(n-2):
    print('*' + ' '*(n-2) + '*')
print('*' * n)
