'''
   bll　业务逻辑层
'''

#import为创学生模型列表,可省略
from phase1.day13.Student_project.Student_project_model import StudentModel

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