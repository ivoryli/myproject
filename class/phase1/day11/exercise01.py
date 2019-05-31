class Pet:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("吃")

class Dog(Pet):
    def __init__(self,name,work):
        super().__init__(name)
        self.work = work

    def look_home(self):
        print("看家")

class Bird(Pet):
    def fly(self):
        print("飞")

p1 = Pet("小王")
d1 = Dog("安安","看门口")
b1 = Bird("小凤")
#               对象,类名
print(isinstance(d1,Pet))#True
print(isinstance(d1,(Pet,Bird)))#True
print(isinstance(d1,Dog))#True
print(isinstance(p1,Dog))#False
print(issubclass(Dog,Pet))#True
print(issubclass(Dog,Dog))#True