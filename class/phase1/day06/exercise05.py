'''
   作业:函数的使用
'''
# 判断是否为奇数函数
# def is_odd(number):
#     # if number % 2 == 1:
#     #     return True
#     # else:
#     #     return False
#
#     #条件表达式
#     # return True if number % 2 == 1 else False
#
#     return number % 2 == 1
#
# n = int(input("请输入整数:"))
# print(is_odd(n))

#----------------------------------------------------------------------------------------

# 计算年份的月份的天数
# def month_2(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
# #向外返回值的结果,类型应该统一
# def day_of_month(month,year):
#     if month < 1 or month > 12:
#         return 0
#     if month == 2:
#         return 29 if month_2(year) else 28
#     if month in (4,6,9,11):
#         return 30
#     return 31
#
# m = int(input("请输入月份:"))
# y = int(input("请输入年份:"))
# print(day_of_month(m,y))

#----------------------------------------------------------------------------------------

# 计算列表最小值
# def list_min(list01):
#     min = list01[0]
#     for i in range(1, len(list01)):
#         if min > list01[i]:
#             min = list01[i]
#     return min
#
# print(list_min([7,9,3,4,6]))

#----------------------------------------------------------------------------------------

# 4. 定义函数，判断字符串中存在的中文字符数量．
#   中文编码范围：0x4E00   ord(字符)    0x9FA5

# def get_chinese_char_count(char):
#     total = 0
#     for i in char:
#         # if 19968 <= ord(i) <= 40869:
#         if 0x4E00 <= ord(i) <= 0x9FA5:
#             total += 1
#     return total
#
# n = input("请输入字符串:")
# print(get_chinese_char_count(n))


