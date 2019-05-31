class StudentModel:
    """
        学生数据模型类
    """

    def __init__(self, name="", age=0, score=0,id=0):
        """
            创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def __str__(self):
        return "我的名字叫:%s,年龄是:%d,成绩是:%d,编号是:%d)"%(self.name,self.age,self.score,self.id)

    def __repr__(self):
        return "StudentModel('%s',%d,%d,%d)"%(self.name,self.age,self.score,self.id)

#列表返回__repr__的值
L = [
    StudentModel("zs",18,90,0),
    StudentModel("ls",20,87,1),
    StudentModel("ff",19,98,2),
    StudentModel("ll",17,78,3)
]
print(L)
s1 = StudentModel('yy',19,100,1)
print(s1.__repr__())
s2 = eval(s1.__repr__())
print(s2)