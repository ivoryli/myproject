'''
   练习:手雷爆炸,可能伤害到敌人,玩家,还有可能伤害未知事物
'''
class Grenade:
    '''
       手雷类
    '''
    def burst(self,bruise_people):
        '''
           爆炸方法
        '''
        if not isinstance(bruise_people,Bruise):
            return
        bruise_people.damage()

class Bruise:
    '''
       受伤类
    '''
    def damage(self):
        '''
           受伤
        '''
        raise NotImplementedError()

class Player(Bruise):
    '''
       玩家类
    '''
    def damage(self):
        '''
           受伤
        '''
        print("player受伤")

class Enemy(Bruise):
    '''
       敌人类
    '''
    def damage(self):
        '''
           受伤
        '''
        print("ememy受伤")

g1 = Grenade()
g1.burst(Player())

