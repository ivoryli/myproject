# tuple01 = ("悟空","八戒","沙增","唐僧")
#
# iterator = tuple01.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
#
# dict01 = {"张三丰":101,"张无忌":102,"张敏":102}
#
# iterator = dict01.__iter__()
# while True:
#     try:
#         key = iterator.__next__()
#         # print(type(item))
#         print(key,dict01[key])
#     except StopIteration:
#         break
#
# L = []
# for key,value in dict01.items():
#     L.append((key,value))
#
# sort_list = sorted(L,key = lambda tp:tp[1])
# print(sort_list)
