'''
 　张三　教　李四　学习python
   李四  教 张三　 玩游戏
   张三　工作　挣了８０００元
   李四　工作　挣了３０００元
'''

#myself
# class Teacher:
#     def __init__(self,name):
#         self.name = name
#
#     def teacher(self,target,subject):
#         print("%s教%s%s"%(self.name,target,subject))
#
#     def money(self,price):
#         print("%s工作挣了%d"%(self.name,price))
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,value):
#         if type(value) == str:
#             self.__name = value
#         else:
#             print("输入有误")
#
# t1 = Teacher("张三")
# t2 = Teacher("李四")
#
# t1.teacher("李四","学习python")
# t2.teacher("张三","玩游戏")
#
# t1.money(8000)
# t2.money(3000)

#--------------------------------------------------------------------------------------------------

class Person:
    def __init__(self, name):
        # 人的姓名
        self.name = name
        # 人会的所有技能
        self.__skills = []
        self.__total_money = 0

    # 只读属性
    @property
    def skills(self):
        # return self.__skills # 返回可变对象地址,意味着类外仍然可以操作可变对象
        return self.__skills[:] # 返回新的可变对象地址,意味着类外仍然操作的是新可变对象,不影响原对象.
        # 备注:每次通过切片返回新对象,都会另外开辟空间创建新对象,占用过多内存.

    # 只读属性
    @property
    def total_money(self):
        return self.__total_money


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value


    def teach(self, person_other, str_skill):
        # person_other 的技能列表,增加str_skill
        person_other.__skills.append(str_skill)
        print(self.name, "教了", person_other.name, str_skill)

    def work(self, money):
        self.__total_money += money
        print(self.name, "工作挣了", money, "元")


zs = Person("张三")
ls = Person("李四")
# 张三　教　李四　学习python
zs.teach(ls, "python")
# 李四  教 张三　 玩游戏
ls.teach(zs, "游戏")

zs.work(8000)
ls.work(4000)
