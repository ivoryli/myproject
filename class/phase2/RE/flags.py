import re

s = '''Hello world
你好,北京
'''



regex = re.compile(r'\w+')
l = regex.findall(s)
print(l)  #['Hello', 'world', '你好', '北京']

#只能匹配ascii码字符
regex = re.compile(r'\w+',flags = re.A)
l = regex.findall(s)
print(l)  #['Hello', 'world']



regex = re.compile(r'[a-z]+')
l = regex.findall(s)
print(l)  #['ello', 'world']

#忽略字母大小写
regex = re.compile(r'[a-z]+',flags = re.I)
l = regex.findall(s)
print(l)  #['Hello', 'world']



regex = re.compile(r'.+')
l = regex.findall(s)
print(l)  #['Hello world', '你好,北京']

#.匹配换行
regex = re.compile(r'.+',flags = re.S)
l = regex.findall(s)
print(l)  #['Hello world\n你好,北京\n']





regex = re.compile(r'^你好')
l = regex.findall(s)
print(l)  #[]

regex = re.compile(r'world$')
l = regex.findall(s)
print(l)  #[]

# ^ $可以匹配每一行的开头结尾位置
regex = re.compile(r'^你好',flags = re.M)   #world$
l = regex.findall(s)
print(l)  #['你好']


#正则添加注释,#前一个空格，和#后的　都算注释
pattern = r"""\w+   # 第一部分
\s+   # 第二部分
\w+   # 第三部分
"""
regex = re.compile(pattern)
l = regex.findall(s)
print(l)  #[]

regex = re.compile(pattern,flags=re.X)
l = regex.findall(s)
print(l)  #['Hello world']

