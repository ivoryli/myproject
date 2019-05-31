class Enemy:
    '''
       敌人
    '''
    def __init__(self,name,hp,atk,atk_speed):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_speed = atk_speed

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self,value):
        if 0 <= value <=100:
            self.__hp = value
        else:
            print("输入有误")

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def atk_speed(self):
        return self.__atk_speed

    @atk_speed.setter
    def atk_speed(self, value):
        if 0 <= value <= 10:
            self.__atk_speed = value
        else:
            print("输入有误")



#name,hp(0-100),atk,atk_speed(0-10)
e1 = Enemy("ww",90,1000,8)
e2 = Enemy("lj",100,1050,2)
e3 = Enemy("wj",84,1200,6)
e4 = Enemy("qd",96,1680,1)

print(e1.atk_speed)
print(e2.atk)
print(e3.hp)
print(e4.name)

print()

e1.atk_speed = 100
e2.atk = 1009
e3.hp = 120
e4.name = "hh"

print()

print(e1.atk_speed)
print(e2.atk)
print(e3.hp)
print(e4.name)
