
#myself
# class StudentModel:
#     """
#          学生数据模型类
#     """
#     __id = 0
#     def __init__(self,name,age,score):
#         """
#            创建学生对象
#         :param name: 学生姓名
#         :param age: 年龄
#         :param score: 成绩
#         """
#         self.name = name
#         self.age = age
#         self.score = score
#         self.__id = self.__class__.id
#         self.__class__.__id += 1
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,value):
#         self.__name = value
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self,value):
#         self.__age = value
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self,value):
#         self.__score = value
#
#     @property
#     def id(self):
#         return self.__class__.__id
#
#     def print_self(self):
#         print(self.name,self.age)
#
#
# class StudentManagerController:
#     """
#         学生逻辑控制器
#     """
#     def __init__(self):
#         self.__stu_list = []
#
#     @property
#     def stu_list(self):
#         return self.__stu_list[:]
#
#     def add_student(self,stu):
#         #
#         self.__stu_list.append(stu)
#
#     def print_self(self):
#         for item in self.stu_list:
#             item.print_self()
#
# s1 = StudentModel("zs",18,90)
# # s1.id = 5
# print(s1.id)

# sl1 = StudentManagerController()
# sl1.add_student(StudentModel("zs",18,90))
# sl1.print_self()

#--------------------------------------------------------------------------------------------------

"""
    学生管理器系统
"""
#teacher
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


class StudentManagerController:
    """
        学生逻辑控制器
    """

    L = [
        StudentModel("zs",18,90,1),
        StudentModel("ls",19,78,2),
        StudentModel("zs",18,99,3)
    ]
    def __init__(self):
        # self.__list_stu = []
        self.__list_stu = self.L

    @property
    def list_stu(self):
        return self.__list_stu

    def add_student(self,stu):
        """
            添加新学生
        :param stu: 需要添加的学生对象
        """
        stu.id = self.__generate_id()
        self.__list_stu.append(stu)

    def __generate_id(self):
        # 生成编号的需求:新编号,比上次添加的对象编号多1.
        # if len(self.__list_stu) > 0:
        #     id = self.__list_stu[-1].id + 1
        # else:
        #     id = 1
        # return id
        return self.__list_stu[-1].id + 1 if len(self.__list_stu) > 0 else 1

    def order_by_score(self):
        '''
           成绩由低到高排序
        :return:
        '''
        new_list = sorted(self.list_stu,key = lambda stu: stu.score)
        return new_list

    def remove_student(self,id):
        '''
            按id删除学生信息
        :return:
        '''
        for item in self.list_stu:
            if id == item.id:
                self.list_stu.remove(item)
                return True
        return False

    def update_student(self,stu):
        '''
           更新学生信息
        :param stu: 更新学生信息内容
        :return: 是否更新成功
        '''
        for item in self.__list_stu:
            if stu.id == item.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        return False

# controller = StudentManagerController()
# controller.add_student(StudentModel("zs",18,85))
# controller.add_student(StudentModel("zs",18,85))
# for item in controller.list_stu:
#     print(item.id,item.name,item.age,item.score)

class StudentManagerView:
    """
       界面视图
    """
    def __init__(self):
        """
           生成一个学生逻辑控制器用来添加学生
        """
        self.__manager = StudentManagerController()

    def __input_students(self):
        """
           输入学生信息
           把学生信息加入到学生逻辑控制器中的列表中
        :return:
        """
        name = input("请输入学生姓名:")
        age = int(input("请输入学生年龄:"))
        score = int(input("请输入学生成绩:"))
        self.__manager.add_student(StudentModel(name,age,score))

    def __output_students(self,list_target):
        """
           输出学生信息
        :return:
        """
        for item in list_target:
            print("学生编号为%d的%d岁%s同学成绩是%d"%(item.id,item.age,item.name,item.score))

    def __score_sort(self):
        '''
           调用controller的排序方法
           显示排序结果
        :return:
        '''
        self.__output_students(self.__manager.order_by_score())

    def __delete_student(self):
        '''
           调用controller的删除学生信息函数
        :return:
        '''
        id = int(input("请输入你要删除的学生id:"))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        '''
           修改学生信息
        '''
        id = int(input("请输入你要修改的学生id:"))
        name = input("请输入学生姓名:")
        age = int(input("请输入学生年龄:"))
        score = int(input("请输入学生成绩:"))
        stu = StudentModel(name,age,score,id)
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __display_menu(self):
        '''
           显示菜单
        :return:
        '''
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按学生成绩由低到高显示")

    def __select_menu(self):
        """
           选择菜单
        :return:
        """
        number = int(input("请输入选项:"))
        if number == 1:
            self.__input_students()
        elif number == 2:
            self.__output_students(self.__manager.list_stu)
        elif number == 3:
            self.__delete_student()
        elif number == 4:
            self.__modify_student()
        elif number == 5:
            self.__score_sort()

    def main(self):
        """
           界面入口方法
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()


view = StudentManagerView()
view.main()