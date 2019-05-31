# class Enemy:
#     '''
#        敌人
#     '''
#     def __init__(self,name,hp,atk,atk_speed):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#         self.atk_speed = atk_speed
#
#     def print_self(self):
#         print(self.name,self.hp,self.atk,self.atk_speed)
#
# L = []
# while True:
#     n = input("请输入敌人姓名")
#     if not n:
#         break
#     ehp = int(input("请输入敌人血量"))
#     eatk = int(input("请输入敌人攻击"))
#     eatk_speed = int(input("请输入敌人攻速"))
#
#     enemy = Enemy(n,ehp,eatk,eatk_speed)
#     L.append(enemy)
#
# # for i in L:
# #     i.print_self()
# def find_enemy(L):
#     for item in L:
#         if n == item.name:
#             # print(item.name,item.hp,item.atk,item.atk_speed)
#             item.print_self()
#
# n = input("请输入敌人名字")
# find_enemy(L)
