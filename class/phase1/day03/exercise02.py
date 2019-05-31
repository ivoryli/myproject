n = int(input("请输入一个数"))

if n % 2:
    print("奇数")
else:
    print("偶数")

#--------------------------------------------------------------------------------

n = int(input("输入年份"))
# day = 29 if n % 4 == 0 and n % 100 != 0 or n % 400 == 0 else 28
day = 29 if not n % 4 and n % 100 or not n % 400 else 28
print(day)