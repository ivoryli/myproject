# re.sub(pattern, repl, string, count=0)
# pattern : 正则中的 模式字符串。
# repl : 替换 的字符串，也可为一个函数。
# string : 要 被查找 替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

import re

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释  $到结尾
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容 '\D' 任意非数字类型
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)