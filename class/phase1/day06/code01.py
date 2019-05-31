'''
    集合
'''

#1.创建空集合
s01 = set()
#2.创建具有默认值的集合
s01 = {}
s02 = set('可迭代对象')

#添加
s02.add("a")
print(s02)

#删除
if "a" in s02:
    s02.remove("a")   #不存在报错

s02.discard("a")      #没有也不报错
print(s02)

#不能查找和修改

#计算
s03 = {1,2,3}
s04 = {2,3,4}
#交集
print(s03 & s04)   #{2,3}

#并集
print(s03|s04)   #{1,2,3,4}

#补集
print(s03^s04)  #{1,4}

print(s03-s04)  #{1}

print(s04 - s03) #{4}

#子集
s05 = {1,2,3}
s06 = {1,2}
re = s05 < s06 #True 说明s06　是s05 的子集
le = s05 > s06 #True 说明s05　是s06 的超集
print(re)
print(le)
#相等　不等

s08 = {1,2,3}
s09 = {1,2,3}

re = s08 == s09 #True 说明两个集合相等
print(re)

#不能增加和删除
print(frozenset([1,2,3]))
