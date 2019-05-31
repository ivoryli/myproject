'''
   lambda
'''

from day16.common.custom_list_tools import ListHelper

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

# def find_id(target):
#     for item in target:
#         if item.id == 101:
#             return item
#
# def find_name(target):
#     for item in target:
#         if item.id == "降龙十八掌":
#             return item
#
# def find_cd(target):
#     for item in target:
#         if item.cd > 10:
#             return item

def find_all(target,func):
    for item in target:
        if func(item):
            return item

id = find_all(L,lambda skill : skill.id == 101)
print(id)

#--------------------------------------------------------------------------------------------------

# def find_id(target,func):
#     for item in target:
#         yield item.id
#         yield xxx(item)

# def xxx(item):
#     return item.id

# def select(target,func):
#     for item in target:
#         yield func(item)
#
# for item in select(L,lambda skill : skill.id):
#     print(item)

#--------------------------------------------------------------------------------------------------

#找共性的代码
def sum_cd(target):
    result = 0
    for item in target:
        result += item.cd
    return result

def sum(target,func):
    result = 0
    for item in target:
        result += func(item)
    return result

total_cd = sum(L,lambda skill : skill.cd)
print(total_cd)
