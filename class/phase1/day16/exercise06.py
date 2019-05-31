'''
可以在实际项目中，灵活运用函数式编程思想．
解决的问题：获取满足条件的最后一个对象
    获取最后一个活人
    获取攻击速度大于５的最后一个敌人

解决的问题：获取满足条件的对象总数
    获取具有生命值的对象总数
    获取攻击速度小于２０的敌人总数

解决的问题：判断列表中是否包含某个元素
    获取列表中是否具有死人
    获取列表中是否具有攻击速度大于１０的敌人
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
    #print list use
    def __repr__(self):
        return "Enemy(%d,%s,%d,%d,%d)"%(self.id,self.name,self.atk,self.hp,self.atk_speed)

L = [
    Enemy(100,"张三",10,50,5),
    Enemy(101,"李四",15,20,7),
    Enemy(102,"王五",5,0,2),
    Enemy(103,"莉莉",20,0,13),
    Enemy(104,"芳芳",17,30,9)
]

# 解决的问题：获取满足条件的最后一个对象
#     获取最后一个活人
#     获取攻击速度大于５的最后一个敌人
# result = ListHelper.first(L[::-1],lambda enemy : enemy.hp > 0)
result = ListHelper.last(L,lambda enemy : enemy.hp > 0)
print(result)
result = ListHelper.first(L[::-1],lambda enemy : enemy.atk_speed > 5)
print(result)

# 解决的问题：获取满足条件的对象总数
#     获取具有生命值的对象总数
#     获取攻击速度小于２０的敌人总数
result = ListHelper.count(L,lambda enemy : enemy.hp > 0)
print(result)
result = ListHelper.count(L,lambda enemy : enemy.atk_speed < 20)
print(result)

# 解决的问题：判断列表中是否包含某个元素
#     获取列表中是否具有死人
#     获取列表中是否具有攻击速度大于１０的敌人
result = ListHelper.include(L,lambda enemy : enemy.hp == 0)
print(result)
result = ListHelper.include(L,lambda enemy : enemy.atk_speed > 10)
print(result)

#删除所有死人
# ListHelper.del_all(L,lambda enemy : enemy.hp == 0)
# print(L)
#删除编号是101的敌人
# ListHelper.del_all(L,lambda enemy : enemy.id == 101)
# print(L)

#获取血量最大的敌人
result = ListHelper.get_max(L,lambda enemy : enemy.atk_speed)
print(result)

print(L)
ListHelper.order_by(L,lambda enemy : enemy.atk_speed)
print(L)
ListHelper.order_by_descending(L,lambda enemy : enemy.atk_speed)
print(L)