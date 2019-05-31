'''
   实例成员
'''

#__dict__显示所有 对象的属性(实例变量) 字典

class ICBC:
    meneys = 100
    def __init__(self,meney):
        self.meney = meney
        self.meneys -= meney

    @classmethod
    def print_meney(cls):
        print(cls.meneys)

i1 = ICBC(5)
# print(i1.meneys) #95
ICBC.print_meney()

i1.meneys = 50  #没进__init__

i2 = ICBC(15)
# print(i2.meneys) #85
ICBC.print_meney()