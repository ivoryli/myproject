class GraphicManager:
    '''
       图形管理器
    '''
    L =[]
    def calculate(self,graph):
        '''
           存每个图形面积
        :param graph:
        :return:
        '''
        if not isinstance(graph,Graph):
            print("传入的不是图形")
            return
        self.L.append(graph.area())
        return self.L

class Graph:
    '''
       图形类
    '''
    def area(self):
        '''
           计算面积
        '''
        raise NotImplementedError()

class Circular(Graph):
    '''
       圆形
    '''
    def __init__(self,radius):
        '''

        :param radius:半径
        '''
        self.r = radius

    def area(self):
        return self.r ** 2 *3.14

class Rectangle(Graph):
    '''
       矩形
    '''
    def __init__(self,length,width):
        '''

        :param length: 长
        :param width:  宽
        '''
        self.l = length
        self.w = width

    def area(self):
        return self.l * self.w

class Triangle(Graph):
    def __init__(self,bottom,hight):
        '''

        :param bottom: 底
        :param hight:  高
        '''
        self.b = bottom
        self.h = hight

    def area(self):
        return (self.b * self.h) / 2

c1 = Circular(3)
r1 = Rectangle(2,2)
ca = GraphicManager()
ca.calculate(c1)
ca.calculate(r1)
for i in ca.L:
    print(i)
print(sum(ca.L))

t1 = Triangle(4,2)
ca.calculate(t1)
print(sum(ca.L))

