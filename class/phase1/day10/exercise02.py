'''
    使用面向对象思想,写出下列场景:
    玩家(攻击力)攻击敌人,敌人受伤(血量)后掉血,还可能死亡(播放动画).
    敌人(攻击力)攻击力攻击玩家,玩家(血量)受伤后碎屏,还可能死亡(游戏结束).
'''

#myself bug:受伤方式(减血,死亡等)没相对应的做在类里
# class Player:
#     def __init__(self,name,atk,hp):
#         self.name = name
#         self.atk = atk
#         self.hp = hp
#
#     def attack(self, subject):
#         subject.hp -= self.atk
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def atk(self):
#         return self.__atk
#
#     @atk.setter
#     def atk(self, value):
#         self.__atk = value
#
#     @property
#     def hp(self):
#         return self.__hp
#
#     @hp.setter
#     def hp(self, value):
#         self.__hp = value
#         if self.__hp <= 0:
#             print("死亡,游戏结束")
#
# class Enemy:
#     def __init__(self, name, atk, hp):
#         self.name = name
#         self.atk = atk
#         self.hp = hp
#
#     def attack(self, subject):
#         subject.hp -= self.atk
#         print("碎屏")
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def atk(self):
#         return self.__atk
#
#     @atk.setter
#     def atk(self, value):
#         self.__atk = value
#
#     @property
#     def hp(self):
#         return self.__hp
#
#     @hp.setter
#     def hp(self, value):
#         self.__hp = value
#         if self.__hp <= 0:
#             print("死亡,播放动画")
#
# p1 = Player("玩家1",20,5)
# e1 = Enemy("敌人1",5,20)
#
# p1.attack(e1)
# print(e1.hp)
# p1.attack(e1)
# print(e1.hp)
#
# e1.attack(p1)
# print(p1.hp)

#--------------------------------------------------------------------------------------------------

class Player:
    """
        玩家类
    """
    def __init__(self,hp,atk):
        self.atk = atk
        self.hp = hp

    def attack(self,enemy):
        print("打死你")
        # 调用敌人受伤方法(敌人负责定义受伤逻辑)
        enemy.damage(self.atk)

    def damage(self,value):
        self.hp -= value
        print("玩家受伤啦,屏幕碎啦")
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家死亡,游戏结束")


class Enemy:
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk

    def damage(self,value):
        self.hp -= value
        print("受伤啦")
        if self.hp <= 0:
            self.__death()

    def attack(self,player):
        print("打死你")
        player.damage(self.atk)

    def __death(self):
        print("死啦,播放动画")


p01 = Player(100,50)
e01 = Enemy(60,10)
# 玩家打敌人
p01.attack(e01)
# p01.attack(e01)
e01.attack(p01)
