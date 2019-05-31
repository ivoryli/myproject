'''
   for嵌套练习
'''

#
# for row in range(4):
#     for col in range(6):
#         if row % 2 == 1:
#             print("*",end = '')
#         else:
#             print("#",end = '')
#     print()
#
# print()
# print()
# print()
#
# for col in range(5):
#     print(col * "#")
#
# for r in range(4):
#     for c in range(r+1):
#         print("#",end = '')
#     print()

#---------------------------------------------------------------------------

'''
####
 ###
  ##
   #
'''

# for row in range(4):      #  1       2     3    4
#     for col in range(row):#0 + 4    1+3   2+2  3+1
#         print(" ",end = "")
#     for col in range(4-row):
#         print("#",end = "")
#     print()

#---------------------------------------------------------------------------

# L = [1,2,3,4,5,6,7,8,9,1,2,3]

#自己做
# for x in range(len(L) - 1):  #0 1 2 3 4 5
#     '''x为比较数'''
#     for y in range(x + 1,len(L)):
#         '''y为被比较数'''
#         if L[x] == L[y]:
#             print("%d有相同的"%L[x])

#老师做的,判断有没有相同的有就退出
# status = False
# for x in range(len(L) - 1):
#     if status:
#         break  #退出外层循环
#     for y in range(x + 1,len(L)):
#         if L[x] == L[y]:
#             status = True
#             print("有相同的")
#             break #只对最近一层作用

#---------------------------------------------------------------------------

'''
   排序 > 升, < 降
'''
L = [1,2,3,4,5,6,7,8,9,20,10,58,45,28]

for x in range(len(L) - 1):
    for y in range(x + 1,len(L)):
        if L[x] < L[y]:  #此处修改升降
            L[x],L[y] = L[y],L[x]

print(L)