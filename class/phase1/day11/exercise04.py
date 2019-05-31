'''
1. 定义父类:武器,数据:攻击力,行为:购买(所有子类都一样).攻击(不知道怎么攻击)
   定义子类:枪,数据:射速,行为:攻击
   定义子类:手雷,数据:爆炸范围,行为:攻击
   创建相应对象,调用相应方法.
   画出内存图
'''

class Weapon:
    '''
       武器类
    '''
    def __init__(self,atk):
        self.atk = atk

    def buy(self):
        print("购买")

    def attack(self):
        raise NotImplementedError()

class Gun(Weapon):
    '''
       枪类
    '''
    def __init__(self,atk,atk_speed):
        super().__init__(atk)
        self.speed = atk_speed

    def attack(self):
        print("攻击")


class Grenade(Weapon):
    '''
       手雷类
    '''
    def __init__(self, atk,scope):
        '''
        :param atk: 攻击力
        :param scope: 爆炸范围
        '''
        super().__init__(atk)
        self.scope = scope

    def attack(self):
        print("攻击")

gun1 = Gun(100,20)
g = Grenade(200,6)
gun1.buy()
g.attack()