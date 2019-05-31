'''
["张三丰","无忌","赵敏"]   -----> {'赵敏': 2, '张三丰': 3, '无忌': 2}
'''

L = ["张三丰","无忌","赵敏"]
L2 = [101,102,103]
#值重复27行代码同用
# L2 = [101,102,102]


d ={item : len(item) for item in L}
print(d)   #{'赵敏': 2, '张三丰': 3, '无忌': 2}



# d2 = {}
# for i in range(len(L)):
#     d2[L[i]] = L2[i]

d2 = {L[x]: L2[x] for x in range(len(L))}
print(d2)  #{'赵敏': 102, '无忌': 102, '张三丰': 101}




# d3 = {}
# for key,value in d2.items():
#     d3[value] = key

d3 = {value : key for key,value in d2.items()}
print(d3)  #{101: '张三丰', 102: '无忌'}




#若值有重复则用下列推导式,先要生成d2 17行代码必要(值有相同)
#d2 = {'赵敏': 102, '无忌': 102, '张三丰': 101}
L3 = [(value,key) for key,value in d2.items()]
print(L3)  #[(102, '赵敏'), (102, '无忌'), (101, '张三丰')]

