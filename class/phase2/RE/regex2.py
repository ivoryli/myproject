#match对象属性

import re

pattern = r'(ab)cd(?P<pig>ef)'

regex = re.compile(pattern)

#获取match对象
obj = regex.search("abcdefghi")
print(obj.group())

#属性变量
print(obj.pos)      #目标字符串开头位置
print(obj.endpos)   #目标字符串结束位置

obj = regex.search("abcdefghi",pos = 0,endpos = 7)
print(obj.pos)      #目标字符串开头位置
print(obj.endpos)   #目标字符串结束位置

print(obj.re)       #正则
print(obj.string)   #目标字符串

print(obj.lastgroup)  #最后一组名称
print(obj.lastindex)  #最后一组序号

print("--------------------------------------------------------------------------------------------")

#属性方法

print(obj.start())  #开始
print(obj.end())    #结束
print(obj.span())   #开始  结束
print(obj.groupdict())  #捕获组字典  {'pig': 'ef'}
print(obj.groups())     #子组对应内容  ('ab', 'ef')
print(obj.group())          #abcdef
print(obj.group(1))         #序列号 ab
print(obj.group('pig'))     #组名  ef
