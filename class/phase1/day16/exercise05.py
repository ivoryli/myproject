'''
准备：
　　－－　创建敌人类（编号／姓名／攻击力／血量／攻击速度．．．）
　　－－　创建敌人列表
练习：
　　 1. 查找所有死人.
    2. 查找编号是101的敌人
    3. 查找所有活人.
    4. 计算所有敌人攻击力总和
    5. 查找所有攻击速度在５－－１０之间的敌人
    6. 查找所有敌人的姓名
'''

from day16.common.custom_list_tools import ListHelper

class Enemy:
    def __init__(self,id,name,atk,hp,atk_speed):
        self.id = id
        self.name = name
        self.atk = atk
        self.hp = hp
        self.atk_speed = atk_speed

    def __str__(self):
        return "Enemy(%d,%s,%d,%d,%d)"%(self.id,self.name,self.atk,self.hp,self.atk_speed)

L = [
    Enemy(100,"张三",10,50,5),
    Enemy(101,"李四",15,20,7),
    Enemy(102,"王五",5,0,2),
    Enemy(103,"莉莉",20,0,13),
    Enemy(104,"芳芳",17,30,9)
]

# 　　 1. 查找所有死人.
for item in ListHelper.find_all(L,lambda enemy : enemy.hp == 0):
    print(item)
print()

#     2. 查找编号是101的敌人
target = ListHelper.first(L,lambda enemy : enemy.id == 101)
print(target)
print()

#     3. 查找所有活人.
for item in ListHelper.find_all(L, lambda enemy : enemy.hp > 0):
    print(item)
print()

#     4. 计算所有敌人攻击力总和
result = ListHelper.sum(L,lambda enemy : enemy.atk)
print(result)
print()

#     5. 查找所有攻击速度在５－－１０之间的敌人
for item in ListHelper.find_all(L,lambda enemy : 5 <= enemy.atk_speed <= 10):
    print(item)
print()

#     6. 查找所有敌人的姓名
for item in ListHelper.select(L,lambda enemy : enemy.name):
    print(item)