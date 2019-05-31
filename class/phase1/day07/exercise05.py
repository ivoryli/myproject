def str_reversal(char):
    L = []
    L = char.split(" ")
    L.reverse()
    str1 = " ".join(L)
    return str1

n = input("请输入字符串:")
print(str_reversal(n))

