import re

r = re.findall('-?\d+\.?\d*',"Hiolji:-123,http:80")

# \s 匹配空字符，\S 匹配非空字符
r = re.findall('\w+\s+\w+','hello    world') #['hello    world']
print(r)

r = re.findall('\S',"Hiolji:123, http:80 s") #['H', 'i', 'o', 'l', 'j', 'i', ':', '1', '2', '3', ',', 'h', 't', 't', 'p', ':', '8', '0', 's']

r = re.findall('\s',"Hiolji:123, http:80 s")  #[' ', ' ']

r = re.findall('\S+',"Hiolji:123, http:80 s")  #['Hiolji:123,', 'http:80', 's']


# \w 匹配普通字符，\W 匹配非普通字符
r = re.findall('\W?\d+',"dafda:$400,afdsads:￥400")
print(r)



# \b 表示单词边界，\B 表示非单词边界

r = re.findall(r'is',"This is a test")
print(r)
r = re.findall(r'\bis\b',"This is a test")
print(r)   #后面一个
r = re.findall(r'\Bis\b',"This is a test")
print(r)   #前面一个

r = re.findall(r'\b[A-Z]\w+',"This is a iPython")  #['This']
print(r)



# 元字符: $
# 匹配规则: 匹配目标字符串的结尾位置
r = re.findall('$\d+',"jij:$100")




#'\$\d+'会在字符串中转义,因为\$没有这个转义设定,所以原样解析,
# 正确输入:\\$\\d+ 把正确输入转为字符串，再将他作为参数传入方法(作为字符串,再一次转义)
r = re.findall('\$\d+',"jij:$100")

r = re.findall(r'\$\d+',"jij:$100")

r = re.findall(r'\$\d+/\d+',"jij:$100/200")  #['$100/200']
print(r)
r = re.findall('\$\d+\\\\\d+',"jij:$100\\200")
print(r)  #['$100\\200']
print(r[0])  #$100\200





# 贪婪模式转换为非贪婪模式,在匹配重复元字符后加 '?' 号即可
r = re.findall(r'\b.+\b',"python-007")  #贪婪模式 ['python-007']
print(r)
r = re.findall(r'\b.+?\b',"python-007")  #非贪婪模式 ['python', '-', '007']
print(r)

r = re.findall(r'\(\S+\)',"adf(asdfasd),gf(123132)")  #贪婪模式 ['(asdfasd),gf(123132)']
print(r)
r = re.findall(r'\(\S+?\)',"adf(asdfasd),gf(123132)")  #非贪婪模式  ['(asdfasd)', '(123132)']
print(r)




#正则表达式分组,可以被作为整体操作，改变元字符的操作对象

#search匹配最前的一个!!
r = re.search(r'(ab)+', "ababababab").group()
print(r)

r = re.search(r'(王|李)\w{1,3}',"王者荣耀").group()
print(r)
r = re.search(r'(王|李)\w{1,3}',"李时珍").group()
print(r)

r = re.search(r'(王|李)\w{1,3}',"王者荣耀 李时珍").group()
print(r)

#findall    ()的使用如下
r = re.findall(r'王\w{1,3}|李\w{1,3}'," 王者荣耀 李时珍")
print(r)

#?
string="abcdefg  acbdgef  abcdgfe  cadbgfe"
regex=re.compile("((\w+)\s+\w+)")
print(regex.findall(string))
# 输出：[('abcdefg  acbdgef', 'abcdefg'), ('abcdgfe  cadbgfe', 'abcdgfe')] 多个括号就会返回多个括号分别匹配到的结果（如regex）

regex1=re.compile("(\w+)\s+\w+")
print(regex1.findall(string))
#输出：['abcdefg', 'abcdgfe']  findall()返回的是括号所匹配到的结果（如regex1）




#在能匹配上的基础上获取子组信息
r = re.search(r'(https|http|ftp|file)://\S+',"https://www.baidu.com").group(0)  #https://www.baidu.com
r = re.search(r'(https|http|ftp|file)://\S+',"https://www.baidu.com").group(1)  #https
print(r)

r = re.search(r'(?P<pig>bai)+',"bai999").group('pig')
print(r)

r = re.search(r'\d{17}(\d|x)',"44010319930518541x").group(0)
print(r)




regex = re.compile(r'abcdef')
print(regex.flags)   #32   100000 默认功能
print(regex.pattern)   #'abcdef'
print(regex.groups)    #0   有几个子组   r'(ab)cdef'  1
print(regex.groupindex)  #{}
regex = re.compile(r'(?P<dog>ab)cd(?P<pig>ef)')
print(regex.groupindex)  #{'dog': 1, 'pig': 2}


