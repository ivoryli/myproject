'''
   根据月份计算天数
'''

# month = int(input("请输入月份:"))
#
# if month < 1 or month > 12:
#     print("输入有误")
# elif month ==2:
#     print("28天")
# elif month in (4,6,9,11):
#     print("30天")
# else:
#     print("31天")


#方法2:
# month = int(input("请输入月份:"))
#
# if month < 1 or month > 12:
#     print("输入有误")
# else:
#     #讲每月天数存入元组
#     day_of_month =(31,28,31,30,31,30,31,31,30,31,30,31)
#     print(day_of_month[month - 1])

'''
  输入月,日.算第几天
'''

while True:
    month = int(input("请输入月份:"))
    if month < 1 or month > 12:
        print("输入有误")
        continue

    day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    day   = int(input("请输入天数:"))

    if day < 1 or day > day_of_month[month - 1]:
        print("输入正确天数")
        continue


    # 方法1:
    # total_day = 0
    # for i in range(month -1):
    #     total_day += day_of_month[i]

    # 方法2:事前不用赋值total_day = 0
    total_day = sum(day_of_month[:month - 1])

    total_day += day
    print(total_day)

