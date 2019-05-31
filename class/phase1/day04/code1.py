'''
    三引号可以隐式换行
    转义符:改变原始含义的字符 \
    "hello \"world\""
    \t table键　水平制表格
    r'' r代表取消转义如: r'c\ban\cd\p' 不会转义
    切片结束超过最大值也不会报错
    'abcde'[3:1] 空值

'''


L2 = list(range(5))
# insert 插入
L2.insert(1,"nibao")
print(L2)
# remove移除指定元素
L2.remove("nibao")
print(L2)
# del移除索引元素
del L2[4]
print(L2)
#超过自动添加,少了自动删除
L2[:2] = ['a','b','c','d']
print(L2)

L = []
for i in range(10):
    L.append(str(i))
result = ",".join(L)    #join+item
print(result)

L2 = result.split(",")
print(L2)

'''
  1.循环录入字符串,按q结束.显示出拼接后的字符串
  2.判断是否是回文   abcba
  3.一注彩票７个球
  　　前6个红色 : 1-33之间,不能重复
      最后一个篮球: 1-16 之间
    (1)  购买彩票
    (2)  随机产生一注彩票
    random.randint(1,100)
'''