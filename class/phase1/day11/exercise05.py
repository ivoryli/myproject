'''
2. 一家公司,有如下几种岗位:
    普通员工:底薪
    程序员:底薪 + 项目分红
    销售员:底薪 + 销售额
   定义员工管理器,记录所有员工,提供计算总薪资方法.
   要求:增加新岗位,员工管理器代码不做修改.
   体会:依赖倒置

增加需求:
'''
class StaffManager:
    '''
       员工管理器
    '''
    def __init__(self):
        self.__all_staffs = []

    def add_staff(self,staff):
        '''
           添加员工
        :param staff:员工类型
        '''
        if not isinstance(staff,Staff):
            return
        #在员工管理器中添加 员工个人薪资
        self.__all_staffs.append(staff)

    def total_salary(self):
        '''
           计算管理器内的员工总薪资
        :return: total 总薪资
        '''
        total = 0
        for item in self.__all_staffs:
            total += item.personage_salary()
        return total

class Staff:
    '''
       员工类
    '''
    def __init__(self,basic_salary):
        '''
        :param basic_salary: 底薪
        '''
        self.bs = basic_salary

    def personage_salary(self):
        '''
        :return: 个人薪资
        '''
        return self.bs

class Programmer(Staff):
    '''
       程序员类
    '''
    def __init__(self,basic_salary,project_distribution):
        '''
        :param basic_salary:  底薪
        :param project_distribution:   项目分红
        '''
        super().__init__(basic_salary)
        self.pd = project_distribution

    def personage_salary(self):
        # return self.bs + self.pd
        #扩展重写
        #若往后可能做底薪操作,
        #例:   这个月业绩好加10%
        #super可以一次性改不用每个员工都该
        return super().personage_salary() + self.pd

class Salesman(Staff):
    '''
       销售员
    '''
    def __init__(self,basic_salary,salary):
        '''
        :param basic_salary:  底薪
        :param salary:   销售额
        '''
        super().__init__(basic_salary)
        self.salary = salary

    def personage_salary(self):
        # return self.bs + self.salary
        return super().personage_salary() + self.salary


manager = StaffManager()
s1 = Staff(2000)
s2 = Programmer(4000,4000)
s3 = Salesman(3000,2500)
manager.add_staff(s1)
manager.add_staff(s2)
manager.add_staff(s3)
print(manager.total_salary())
manager.add_staff(" ")
print(manager.total_salary())

