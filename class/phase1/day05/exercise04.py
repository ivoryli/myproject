'''
录入字符串,打印字符串中每个字符出现的次数
'''

d = {}
str1 = input("请输入字符串:")

for s in str1:
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1

for k,v in d.items():
    print("字符%s出现了%d次"%(k,v))