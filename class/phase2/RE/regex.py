import re

s = "Levi:1994,Sunny:1993"
pattern = r'(\w+):(\d+)'  #[('Levi', '1994'), ('Sunny', '1993')]
# pattern = r'(\w+):\d+'  #['Levi', 'Sunny']
# pattern = r'\w+:\d+'  #['Levi:1994', 'Sunny:1993']


#re模块调用
l = re.findall(pattern,s)
print(l)

#compile对象调用
regex = re.compile(pattern)
#0,12是目标字符串下标范围
l = regex.findall(s,0,12)
print(l)


#split 使用正则表达式匹配内容,切割目标字符串
s = 'hello world how are you   L-body'
l = re.findall(r'\b\w+?\b',s)
print(l)   #['hello', 'world', 'how', 'are', 'you', 'L', 'body']
l = re.split(r'[^\w]+',s)
print(l)  #['hello', 'world', 'how', 'are', 'you', 'L', 'body']
l = re.split(r'[\W]+',s)
print(l)  #['hello', 'world', 'how', 'are', 'you', 'L', 'body']



#sub使用一个字符串替换正则表达式匹配到的内容
s = 'time: 2019/10/12'

ns = re.sub(r'/','-',s)
print(ns)   #time: 2019-10-12
ns = re.sub(r'/','-',s,1)
print(ns)   #time: 2019-10/12
ns = re.subn(r'/','-',s)
print(ns)   #('time: 2019-10-12', 2)   替换了两次

