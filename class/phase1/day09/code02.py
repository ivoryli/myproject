class Wife:
    def __init__(self,name,age):
        self.name = name
        #缺点:缺乏对象数据的封装,外界可以随意赋值
        self.age = age

class Wife:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

w01 = Wife("芳芳",26)
w01 = Wife("铁锤",74)


