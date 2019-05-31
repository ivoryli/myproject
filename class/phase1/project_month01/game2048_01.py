'''
   2048核心算法
'''

#-------------------------------------------------------------------------------------------------

#练习1:定义函数,将零元素移动到末尾
#20 20 --> 2200
#02 20 --> 2200


#myself ok
# def move_zero_right(L):
#     for x in range(len(L) - 1):
#         for y in range(x + 1,len(L)):
#             if L[x] == 0:
#             #若列表有不为0的元素,令第x个元素不为零
#                 L[x],L[y] = L[y],L[x]


'''
方法１:teacher
def zero_to_end(list_target):
    #将传入的列表中非零元素,拷贝到新列表中

    new_list = [x for x in list_target if x != 0]
    new_list += list_target.count(0) * [0]
    list_target[:] = new_list
'''

#teacher
def zero_to_end(list_target):
    #删除零元素,!!!!!从后往前删
    for i in range(len(list_target) - 1,-1,-1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)

#-------------------------------------------------------------------------------------------------

#练习2: 定义合并一列函数

# myself !uncertainty
# def merge(list_target):
#     zero_to_end(list_target)
#     for x in range(len(list_target) - 1):
#         if L[x] == L[x + 1]:
#             L[x] += L[x + 1]
#             L[x + 1] = 0
#     zero_to_end(list_target)

#teacher
def merge(list_target):
    zero_to_end(list_target)
    for i in range(len(list_target) - 1):
        if list_target[i] == list_target[i + 1]:
            list_target[i] += list_target[i + 1]
            list_target[i + 1] = 0
    zero_to_end(list_target)

#-------------------------------------------------------------------------------------------------

#练习3:将二维列表,以表格的格式显示在屏幕中

list01 = [#8,4,2,2    8,4,4,0
    [2,2,4,8], #4 4 8 0          0 4 4 8
    [2,4,4,8],
    [2,2,4,8],
    [2,8,4,8]
]

list02 = [
    [2,0,0,2],
    [2,2,0,0],
    [2,0,4,4],
    [4,0,0,2]
]
#myself
# def print_map(list_target):
#     for list_item in list_target:
#         for item in list_item:
#             print(item,end = " ")
#         print()

#teacher
def print_map(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c],end = " ")
        print()

# print_map(list01)

#-------------------------------------------------------------------------------------------------

#练习4:
'''
   上下左右合并
'''

#myself
# def left_list(list_target):
#     for item in list_target:
#         merge(item)

#teacher
#   左移
def move_left(map):
    for r in range(len(map)):
        merge(map[r])

# teacher
#   右移
def move_right(map):
    for r in range(len(map)):
        list_merge = map[r][::-1]
        merge(list_merge)
        map[r] = list_merge[::-1]

# --------------------------------------#
#myself
#   上下移动需要的换位
# def change_map(map):
#     L = []
#     for r in range(len(map)):
#         Lr = []
#         #0-4
#         for c in range(len(map[r])):
#             Lr.append(map[c][r])
#         L.append(Lr)
#     return L
#
# #   上移
# def move_top(map):
#     L = change_map(map)
#     move_left(L)
#     L = change_map(L)
#     return L
#
# #   下移
# def move_bottom(map):
#     L = change_map(map)
#     move_right(L)
#     L = change_map(L)
#     return L
# --------------------------------------#

#teacher
def move_up(map):
    for c in range(4):
        list_merge = []
        for r in range(4):
            list_merge.append(map[r][c])

        merge(list_merge)
        for r in range(4):
            map[r][c] = list_merge[r]


def move_down(map):
    for c in range(4):
        list_merge = []
        for r in range(3,-1,-1):
            list_merge.append(map[r][c])

        merge(list_merge)
        for r in range(3,-1,-1):
            map[r][c] = list_merge[3 - r]


#-------------------------------------------------------------------------------------------------

#测试代码

move_down(list02)
print_map(list02)
