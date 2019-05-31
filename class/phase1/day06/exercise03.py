'''
   列表推导式
'''

L1 = ['香蕉','苹果','哈密瓜']
L2 = ['可乐','牛奶']

L3 = [x + y for x in L1 for y in L2]
print(L3)