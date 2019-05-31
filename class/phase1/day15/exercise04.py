'''
   生成器函数练习
   体会:方法/函数,需要向外返回多个结果时,使用生成器函数.

'''
#
# list01 = [1,2,3,4,5,6,7,8]
#
# def is_even(target):
#     for item in target:
#         if item % 2 == 0:
#             yield item
#
# for item in is_even(list01):
#     print(item)

class Student:
    def __init__(self,name,sex,age,score):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score

    def __str__(self):
        return "Student(%s,%s,%d,%d)"%(self.name,self.sex,self.age,self.score)

list_stu = [
        Student("张无忌","男",28,82),
        Student("赵敏","女",25,95),
        Student("周芷若","女",26,88)
]

def get_woman(target):
    for item in target:
        if item.sex == "女":
            yield item

for item in get_woman(list_stu):
    print(item)

def get_score(target):
    for item in target:
        if item.score > 90:
            yield item

for item in get_score(list_stu):
    print(item)