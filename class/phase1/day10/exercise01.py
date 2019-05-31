'''
   小明在招商银行取钱
'''

class Person:
    def __init__(self,name,money = 0):
        self.name = name
        self.money = money

class Bank:
    def __init__(self,name,money):
        self.name = name
        self.total_money = money

    def get_money(self,person,value):
        if self.total_money > value:
            self.total_money -= value
            person.money += value
            print("取钱成功")
        else:
            print("取钱失败")

p01 = Person("小明")
b01 = Bank("招商",90000)
b01.get_money(p01,90)
