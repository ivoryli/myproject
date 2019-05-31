'''
   运算符重载
   更多重载方法看F:\达内\phase1\第二周上课内容\03object_oriented

'''
class Vector:
    '''
      向量
    '''
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "Vector(%s)"%self.x

    def __add__(self,other):
        return Vector(self.x + other)

    def __sub__(self,other):
        return Vector(self.x - other)

    def __rmul__(self, other):
        return Vector(self.x * other)

    def __radd__(self,other):
        return Vector(self.x + other)

    def __iadd__(self,other):
        '''
           不重写idd也可以复合运算,但会创造新对象.
           重写为了id一样,在同个对象上累计.
        '''
        self.x += other
        return self

    def __lt__(self,other):
        return self.x < other

v01 = Vector(10)
v02 = v01 + 5
print(v02)
v03 = v02 - 3
print(v03)
v04 = 2 * v01
print(v04)
v05 = v02 + v01
# print(v05)
print(v05.x)
v01 += 100
print(v01)