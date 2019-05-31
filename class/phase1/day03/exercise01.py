# n = input("季节")
#
# if n == '春':
#     print("1,2,3")
# elif n == '夏':
#     print("4,5,6")
# elif n == '秋':
#     print("7,8,9")
# elif n == '冬':
#     print("10,11,12")
# else:
#     print("请输入正确季度")

#-----------------------------------------
'''
输入月份得天数
'''

# n = int(input("输入月份"))
#
# if n < 1 or n > 12:
#     print("请输入正确月份")
#
# elif n == 2:
#     print("28")
#
# elif n == 4 or n == 6 or n == 9 or n ==11:
#     print("30")
#
# else:
#     print("31")

#------------------------------------------------

n1 = 8
n2 = 6
n3 = 10
n4 = 5

n = 0
if n < n1:
    n = n1

if n < n2:
    n = n2

if n < n3:
    n = n3

if n < n4:
    n = n4

print(n)
