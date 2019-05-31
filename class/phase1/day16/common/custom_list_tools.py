"""
    针对列表的自定义工具
"""
class ListHelper:
    #例子/home/tarena/class/phase1/day16/exercise03.py
    @staticmethod
    def find_all(target,func_condition):
        """
            查找列表中满足条件的所有元素
        :param target: 列表
        :param func_condition: 条件
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值
        :return:
        """
        # for item in target:
        #     if func_condition(item):
        #         yield item
        return (item for item in target if func_condition(item))

    @staticmethod
    def first(target, func_condition):
        '''
           查找列表中满足条件的第一个元素
        :param target:
        :param func_condition:
        :return:
        '''
        for item in target:
            if func_condition(item):
                return item

    @staticmethod
    def select(target, func_condition):
        '''
           筛选列表中指定条件的数据
        :param target:
        :param func_condition:
        :return:
        '''
        for item in target:
            yield func_condition(item)

    @staticmethod
    def sum(target, func_condition):
        '''
           计算列表中指定条件的所有元素的和
        :param target:
        :param func_condition:
        :return:
        '''
        result = 0
        for item in target:
            result += func_condition(item)
        return result

    @staticmethod
    def count(target,func_condition):
        '''
            获取所有满足条件的对象总数
        :param target:
        :param func_condition:
        :return:
        '''
        count_value = 0
        for item in target:
            if func_condition(item):
                count_value += 1
        return count_value

    @staticmethod
    def last(target,func_condition):
        '''
           查找最后一个满足条件的元素
        :param target:
        :param func_condition:
        :return:
        '''
        for i in range(len(target) - 1,-1,-1):
            if func_condition(target[i]):
                return target[i]

    @staticmethod
    def include(target,func_condition):
        '''
           判断是否包含满足条件的对象
        :param target:
        :param func_condition:
        :return:
        '''
        for item in target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def del_all(target,func_condition):
        '''
           删除满足条件的所有对象
        :param target:
        :param func_condition:
        :return: 成功删除了多少个对象
        '''
        del_count = 0
        for i in range(len(target) - 1,-1,-1):
            if func_condition(target[i]):
                del target[i]
                del_count += 1
        return del_count

    @staticmethod
    def get_max(target,func_condition):
        '''
           获取指定条件最大值(第一个)
        :param target:
        :param func_condition:
        :return:
        '''
        max_target = target[0]
        for i in range(1,len(target)):
            if func_condition(max_target) < func_condition(target[i]):
                max_target = target[i]
        return max_target

    @staticmethod
    def get_min(target,func_condition):
        '''
           获取指定条件最小值(第一个)
        :param target:
        :param func_condition:
        :return:
        '''
        min_target = target[0]
        for i in range(1,len(target)):
            if func_condition(min_target) > func_condition(target[i]):
                min_target = target[i]
        return min_target

    @staticmethod
    def order_by(target,func_condition):
        '''
           按指定条件升序排列
        :param target:
        :param func_condition:
        :return:
        '''
        for r in range(len(target) - 1):
            for c in range(r + 1,len(target)):
                if func_condition(target[r]) > func_condition(target[c]):
                    target[r],target[c] = target[c],target[r]

    @staticmethod
    def order_by_descending(target,func_condition):
        '''
           按指定条件降序排列
        :param target:
        :param func_condition:
        :return:
        '''
        for r in range(len(target) - 1):
            for c in range(r + 1,len(target)):
                if func_condition(target[r]) < func_condition(target[c]):
                    target[r],target[c] = target[c],target[r]

    @staticmethod
    def sort(target,func_condition,reverse=False):
        '''
           按指定条件降序排列
        :param target:  需要排序的数据
        :param func_condition:　排序胡逻辑
        　　　　　　　　　　　　　　类型是函数
        :return:
        '''
        for r in range(len(target) - 1):
            for c in range(r + 1,len(target)):
                if reverse:
                    if func_condition(target[r]) > func_condition(target[c]):
                        target[r],target[c] = target[c],target[r]
                else:
                    if func_condition(target[r]) < func_condition(target[c]):
                        target[r],target[c] = target[c],target[r]