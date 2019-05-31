#输入某年某月某日，判断这一天是这一年的第几天？

#myself
# month_of_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# def is_leap_year(year):
#     return year % 4 ==0 and year % 100 != 0 or year % 400 == 0
#
# def get_day(year,month,day,list_target):
#     total_day = 0
#     if is_leap_year(year):
#         list_target[1] = 29
#     for item in range(month):
#         total_day += list_target[item]
#     total_day += day
#     return total_day
#
# year = int(input("请输入年份:"))
# month = int(input("请输入年份:"))
# day = int(input("请输入年份:"))
#
# print(get_day(year,month,day,month_of_day))



#teacher
year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))

sum = 0

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('data error')

sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)


