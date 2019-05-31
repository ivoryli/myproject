#2.判断是否是回文   abcba

str_input =input("请输入字符串: ")
if str_input == str_input[::-1]:
    print("是回文")
else:
    print("不是回文")