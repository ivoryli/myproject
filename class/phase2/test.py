import re

str1 = '<a href="http://baijiahao.baidu.com/s?id=1635002426455561415" mon="ct=1&amp;a=2&amp;c=top&amp;pn=2" target="_blank">商务部：肉蛋蔬果等生活必需品 市场供应有保障</a>'

patten = re.compile('<a href="(\S*)" .*>(.*)</a>')
result = patten.findall(str1)

print(result)