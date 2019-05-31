class Studen:
    """
       学生类
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self):
        print(self.name + "正在学习")

    def work(self):
        print(self.name + "正在工作")

#st1　悟空对象的地址
st1 = Studen("悟空",28)
st2 = Studen("八戒",29)
#通过对象地址,调用对象方法,会自动传递对象地址
st1.study()
st2.work()
