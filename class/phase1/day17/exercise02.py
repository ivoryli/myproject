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

    def __repr__(self):
        return "Enemy(%d,%s,%d,%d,%d)"%(self.id,self.name,self.atk,self.hp,self.atk_speed)

L = [
    Enemy(100,"张三",10,50,5),
    Enemy(101,"李四",15,20,7),
    Enemy(102,"王五",5,0,2),
    Enemy(103,"莉莉",20,0,13),
    Enemy(104,"芳芳",17,30,9)
]

# 解决的问题１：
# 　　　获取敌人列表中，攻击力最小的敌人．
# 　　　使用内置高阶函数和ListHelper实现．
result = ListHelper.get_min(L,lambda e : e.atk)
print(result)
result = min(L,key = lambda e : e.atk)
print(result)

# 解决的问题２：
# 　　　根据血量对敌人列表进行降叙排列
# 　　　使用内置高阶函数和ListHelper实现．
for item in sorted(L,key = lambda e : e.hp,reverse=True):
    print(item)

ListHelper.order_by_descending(L,lambda e : e.hp)
print(L)

ListHelper.sort(L,lambda e : e.hp,reverse=True)
print(L)