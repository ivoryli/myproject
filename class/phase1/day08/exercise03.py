"""
２. 创建学生类
    －－　数据：姓名，性别，年龄，成绩．
    －－　行为：print_self()
   画出学生列表内存图
   定义函数：
        －－　定义函数，在学生列表中，根据姓名查找学生对象．
        －－　定义函数，在学生列表中，根据性别查找所有学生对象．
        －－　查找年龄大于20，成绩大于60的所有学生对象．
"""

class Student:
    def __init__(self,name,sex,age,score):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score
    def print_self(self):
        print(self.name,self.sex,self.age,self.score)

L =[
    Student("zs","男",18,90),
    Student("ww","男",18,90),
    Student("ll","女",18,90),
    Student("ss","女",22,90),
    Student("dp","男",22,90),
    Student("xm","女",18,90)
   ]

def find_for_name(list_target):
    name = input("请输入查找学生的名字:")
    for item in list_target:
        if name == item.name:
            return item

def find_for_sex(list_target):
    L = []
    sex = input("请输入查找学生的性别:")
    for item in list_target:
        if sex == item.sex:
            L.append(item)
    return L

# stu = find_for_name(L)
# stu.print_self()
stu_list = find_for_sex(L)
for x in stu_list:
    x.print_self()

print()

for item in L:
    if item.age > 20 and item.score > 60:
        item.print_self()

