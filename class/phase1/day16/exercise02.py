'''
   生成器表达式
'''

L = [2,3,4,6]

L1 = [x for x in L if x > 3]
print(L1)

L2 = (x for x in L if x > 3)
for item in L2:
    print(item,end = " ")