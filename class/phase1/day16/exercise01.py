'''
    enumerate,zip
'''

#自定义enumerate
# L = [121,22,33,44,85,96,47,82,93]
#
# def my_enumerate(target):
#     # L = []
#     for i in range(len(target)):
#         yield (i,target[i])
#     # return L
#
# for index,element in my_enumerate(L):
#     print(index,element)

#--------------------------------------------------------------------------------------------------

list01 = [101,102,103]
list02 = ["张三丰","张无忌","赵敏"]
list03 = ["A","B","C"]

# for item in zip(list01,list02):
#     print(item)

#bug:只能两个列表 应是my_zip(*args)
# def my_zip(target1,target2):
#     #sort取最短
#     sort = target2 if len(target1) > len(target2) else target1
#     for index in range(len(sort)):
#         yield (target1[index],target2[index])
#
# for item in my_zip(list01,list02):
#     print(item)

def my_zip2(*args):
    #sort取最短
    L = []
    sort = min([len(x) for x in args])
    for index in range(sort):
        for item in args:
            L.append(item[index])
        yield tuple(L)
        L.clear()

for item in my_zip2(list01,list02,list03):
    print(item)