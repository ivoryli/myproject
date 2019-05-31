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
    Enemy(102,"王五五",5,0,2),
    Enemy(103,"莉莉",20,0,13),
    Enemy(104,"芳芳",17,30,9)
]

for item in filter(lambda e : 10 < e.hp < 50,L):
    print(item)
print()

for item in map(lambda e : e.atk,L):
    print(item)
print()

for item in sorted(L,key = lambda e:e.atk):
    print(item)
print()

result = max(L,key = lambda e : len(e.name))
print(result)