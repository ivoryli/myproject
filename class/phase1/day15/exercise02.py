'''
   员工管理器
'''

# class Employee:
#     def __str__(self):
#         return "Employee()"
#
# class EmployeeIterator:
#     def __init__(self,employess_list):
#         self.target = employess_list
#         self.index = 0
#
#     def __next__(self):
#         if self.index >= len(self.target):
#             raise StopIteration()
#         result = self.target[self.index]
#         self.index += 1
#         return result
#
# class EmployeeManager:
#     def __init__(self,employess):
#         self.all_employess = employess
#     def __iter__(self):
#         return EmployeeIterator(self.all_employess)
#
# manager = EmployeeManager([Employee(),Employee()])
# for item in manager:
#     print(item)

'''
   生成器版本
'''

class Employee:
    def __str__(self):
        return "Employee()"

class EmployeeManager:
    def __init__(self,employess):
        self.all_employess = employess
    def __iter__(self):
        for item in self.all_employess:
            yield item

manager = EmployeeManager([Employee(),Employee(),Employee()])
for item in manager:
    print(item)