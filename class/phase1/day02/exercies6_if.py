n = int(input("输入一个数:"))
if n % 2 == 0:
    print("偶数")
else:
    print("奇数")

#-------------------------------------------------------------------------

year = int(input("输入一个年份:"))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("闰年")
else:
    print("平年")