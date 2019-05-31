#1.循环录入字符串,按q结束.显示出拼接后的字符串
L = []
LS = []
while True:
    str1 = input("请输入字符串")
    if str1 == 'q':
        break
    L.append(str1)

str_result = " ".join(L)
print(str_result)

LS = str_result.split(" ")
print(LS)