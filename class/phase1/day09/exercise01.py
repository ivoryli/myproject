class Wife:
    count = 0
    def __init__(self,name,age,sex):
        self.name = name
        if 0 < age < 100:
            self.age = age
        else:
            print("!")
        self.sex = sex
        Wife.count += 1

    @classmethod
    def count_wife(cls):
        return cls.count

w1 = Wife("丽丽",18,'女')
w2 = Wife("彤彤",22,'女')
w3 = Wife("芳芳",17,'女')
w4 = Wife("小苏",-20,'女')

print(Wife.count_wife())