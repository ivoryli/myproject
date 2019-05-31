'''
   表示层
'''
from Student_project_model import StudentModel
from Student_project_bll import StudentManagerController

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
        age = self.__get_age()
        score = self.__get_score()
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
        # id = int(input("请输入你要删除的学生id:"))
        id = self.__get_id()
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        '''
           修改学生信息
        '''
        id = self.__get_id()
        name = input("请输入学生姓名:")
        age = self.__get_age()
        score = self.__get_score()
        stu = StudentModel(name,age,score,id)
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")


    #可尝试用一个函数代替这３个函数
    def __get_age(self):
        while True:
            try:
                age = int(input("请输入年龄:"))
            except ValueError:
                print("年龄输入有误(请输入0-120之间)")
                continue

            if 0 <= age <= 120:
                return age

            print("年龄输入有误(请输入0-120之间)")

    def __get_score(self):
        while True:
            try:
                score = int(input("请输入成绩:"))
            except ValueError:
                print("成绩输入有误(请输入0-100之间)")
                continue

            if 0 <= score <= 100:
                return score

            print("成绩输入有误(请输入0-100之间)")

    def __get_id(self):
        while True:
            try:
                id = int(input("请输入id:"))
            except ValueError:
                print("id输入有误,请输入整数")
                continue

            for item in self.__manager.list_stu:
                if id == item.id:
                    return id

            print("id输入有误(没有该id的学生)")

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
