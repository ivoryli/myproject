'''
   函数运用
   在控台显示矩形
'''

# def show_rectangle(x,y,char):
#     for r in range(x):
#         for c in range(y):
#             print(char,end = '')
#         print()
#
# row = int(input("需要显示矩形的行数是:"))
# col = int(input("需要显示多少列的矩形:"))
# setchar = input("矩形由什么图形组成")
# show_rectangle(row,col,setchar)

#---------------------------------------------------------------------------------

# def show_pic(row,char):
#     '''
#        打印三角形
#     :param row:  三角形高度
#     :param char: 三角形的组成字符
#     :return:
#     '''
#     for r in range(row):      #  1       2     3    4
#         for col in range(r):  #0 + 4    1+3   2+2  3+1
#             print(" ",end = "")
#         for col in range(row-r):
#             print(char,end = "")
#         print()
#
#
# hight = int(input("需要显示矩形的高度是:"))
# setchar = input("矩形由什么图形组成")
#
# show_pic(hight,setchar)

#---------------------------------------------------------------------------------
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
#
# def same(L):
#     for x in range(len(L) - 1):
#         for y in range(x + 1,len(L)):
#             if L[x] == L[y]:
#                 return True
#     return False
#
# result = same(L)
# print(result)

#---------------------------------------------------------------------------------
def is_season(n):
    if n < 1 or n >12:
        return "请正确输入1-12"
    if n <= 3:
        return "春天"
    if n <= 6:
        return "夏天"
    if n <= 9:
        return "秋天"
    return "冬天"

season = int(input("月份"))
result = is_season(season)
print(result)









