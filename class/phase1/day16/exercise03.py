'''
   用函数式编程来嵌套
创建技能类(编号，技能名称，冷却时间，攻击力，消耗法力)
　　创建技能列表．
　　－－　定义函数：查找冷却时间为０的所有技能对象
　　－－　定义函数：查找攻击力大于５的所有技能对象
　　－－　定义函数：查找攻击力大于１０，并且不需要消耗法力的所有技能．
'''

class Skill:
    def __init__(self,id,name,cd,atk,ap):
        self.id = id
        self.name = name
        self.cd = cd
        self.atk = atk
        self.ap = ap

    def __str__(self):
        return "Skill(%d,%s,%d,%d,%d)"%(self.id,self.name,self.cd,self.atk,self.ap)

L = [
    Skill(100,"降龙十八掌", 60, 10, 5),
    Skill(101,"如来神掌", 50, 5, 15),
    Skill(102,"六脉神剑", 0, 20, 8),
    Skill(103,"一阳指", 20, 50, 15),
    Skill(104,"冷酷追击", 15, 30, 0)
]

# 　　－－　定义函数：查找冷却时间为０的所有技能对象
# def find_cd(target):
#     return (item for item in target if item.cd == 0)
#
# for item in find_cd(L):
#     print(item)
# print()
#
# # 　　－－　定义函数：查找攻击力大于５的所有技能对象
# def find_atk(target):
#     return (item for item in target if item.atk > 5)
#
# for item in find_atk(L):
#     print(item)
#
# print()
#
# # 　　－－　定义函数：查找攻击力大于１０，并且不需要消耗法力的所有技能．
# def find_atk_ap(target):
#     return (item for item in target if item.atk > 10 and item.ap == 0)
#
# for item in find_atk_ap(L):
#     print(item)


#相同点
def find_all(target,func_condition):
    return (item for item in target if func_condition(item))
#不同点
# def condition_find_cd(item):
#     return item.cd == 0
# #不同点
# def condition_find_atk(item):
#     return item.atk > 5
# #不同点
# def condition_find_atk_ap(item):
#     return item.atk > 10 and item.ap == 0

for item in find_all(L, lambda item : item.cd == 0):
    print(item)

print()

for item in find_all(L, lambda item : item.atk > 5):
    print(item)

print()

for item in find_all(L, lambda item : item.atk > 10 and item.ap == 0):
    print(item)

# from day16.common.custom_list_tools import ListHelper
# for item in ListHelper.find_all(L,condition_find_cd):
#     print(item)

