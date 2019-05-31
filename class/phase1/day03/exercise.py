n = int(input("月份"))

# if 1 <= n  <= 3:
#     print("春天")
# elif 4 <= n  <= 6:
#     print("夏天")
# elif 7 <= n  <= 9:
#     print("秋天")
# elif 10 <= n  <= 12:
#     print("冬天")
# else:
#     print("请正确输入1-12")

if n < 1 or n >12:
    print("请正确输入1-12")
elif n <= 3:
    print("春天")
elif n <= 6:
    print("夏天")
elif n <= 9:
    print("秋天")
else:
    print("冬天")
