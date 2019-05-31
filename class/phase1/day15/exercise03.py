'''
   定义MyRange类
'''
# class MyRangeIterator:
#     def __init__(self,parameter):
#         '''
#         :param parameter: parameter中文意思:参数
#         '''
#         self.stop = parameter
#         self.index = 0
#
#     def __next__(self):
#         if self.index >= self.stop:
#             raise StopIteration()
#         item = self.index
#         self.index += 1
#         return item
#
# class MyRange:
#     def __init__(self,stop):
#         self.stop = stop
#
#     def __iter__(self):
#         return MyRangeIterator(self.stop)
#
# for i in MyRange(5):
#     print(i)

'''
   生成器版本
'''

class MyRange:
    def __init__(self,stop):
        self.stop = stop
    def __iter__(self):
        start = 0
        while start < self.stop:
            yield start
            start += 1

for i in MyRange(6):
    print(i)
