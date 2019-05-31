import re

s = '2019年,建国70周年'
pattern = r'\d+'

#返回包含匹配结果的迭代器
it = re.finditer(pattern,s)

# print(dir(next(it)))

for i in it:
    print(i.group())



#完全匹配,匹配字符串，如果能匹配到全部则返回字符串，匹配到的是字符串的一部分,则返回None
m = re.fullmatch(r'\w+',"hello-1973")
# print(m.group())  #报错,None ,去除 -,返回hello1973




#匹配开始位置
m = re.match(r'[A-Z]\w*','hello World')
# print(m.group())  #报错,None
m = re.match(r'[A-Z]\w*','Hello World')
print(m.group())  #Hello




#匹配第一处  s 空   S非空
m = re.search(r"\S+","好\n嗨 哟")
print(m.group())   #好