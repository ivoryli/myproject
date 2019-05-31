

# 正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。


import re

# print(re.match('abc', 'abc.runoob.com').group())
# # print(re.search('run', 'wc.runoob.com'))

# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# ()括号内表group的一个对象(对象与对象用空格分开),group(0)==group()
line = "Cats are smarter than dogs"
#     group(1)  group(2) group(3)


# line = "jifads are nihao wobuhao keyi"



matchObj = re.match( r'(.*) are (.*?) (.*?) .*', line, re.M|re.I)
#                   group(1) group(2) group(3)

if matchObj :
    # matchObj是一个对象
    # print(matchObj)
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.group(3) : ", matchObj.group(3))


# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。