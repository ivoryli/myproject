'''
    猜拳
'''


'''
  思路:
  1.设定胜利法则
  2.对比
    1)若 电脑 = 键 自己=值
         则 电脑赢
    2)若 自己 = 键 电脑=值
         则 自己赢
'''

import random

# 不建议用字典保存victory
# L = ["剪刀","石头","布"]
# victory = {
#            "石头":"剪刀",
#            "剪刀":"布",
#            "布":"石头",
#           }
#
# while True:
#     randq = L[random.randint(0,2)]
#     # randq = "布"
#     print(randq)
#
#     n = input("请出拳")
#     count = 0
#     for key,value in victory.items():
#         count += 1
#         if key == randq and value == n:
#             print("电脑赢")
#             break
#         elif key == n and value == randq:
#             print("您赢了")
#             break
#         #把胜利结果对比完,都没有人胜利
#         elif count == 3:
#             print("平局")

victory = (
            ("石头","剪刀"),
            ("剪刀","布"),
            ("布","石头"),
          )

L = []
for x in range(3):
    items = ("石头","剪刀","布")
    sys_input_item = items[random.randint(0,2)]
    print(sys_input_item)
    user_input_index = int(input("请输入整数(0代表石头,1代表剪刀,2代表布)"))
    user_input_item = items[user_input_index]


    if user_input_item == sys_input_item:
        print("平局")
        L.append(2)

    elif (user_input_item,sys_input_item) in victory:
        print("赢啦")
        L.append(3)
    else:
        print("输了")
        L.append(1)

if sum(L) >= 7:
    print("三局凉生结果:赢了")
elif sum(L) == 6:
    print("三局凉生结果:平局")
elif sum(L) < 7:
    print("三局凉生结果:输了")
