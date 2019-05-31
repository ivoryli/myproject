L1 = [1,2]
L2 = L1
L1[0] = 100
print(L2[0])  #100

L1 = [1,2]
L2 = L1
L1[0] = [100]
print(L2[0])  #1
print(L1)

L1 = [1,2]
L2 = L1[:]  # 等同 L2=L1.copy
L1[0] = 100
print(L2[0])  #100

L1 = [1,[2,3]]
L2 = L1.copy()  # 等同 L2=L1.copy,只拷贝一层
L1[1][0] = 200
print(L2[1][0])  #200

import copy
L1 = [1,[2,3]]
#L2 = L1.深拷贝()  # 等同 L2=L1.copy,只拷贝一层
L2 = copy.deepcopy(L1)    #深拷贝把全部地址重新赋新地址
L1[1][0] = 200
print(L2[1][0])  #2