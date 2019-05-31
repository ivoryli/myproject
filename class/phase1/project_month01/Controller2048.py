'''
    逻辑处理模块
'''
"""
    ２０４８游戏
    规则：
        游戏运行，在４＊４的方格中，出现两个随机的数字．
        产生随机数的策略：10%的概率是４，90%的概率是2.
        用户移动方格（wsad）,方格内的数字按照相应规则进行合并．
        如果地图有变化(数字移动／数字合并)，再产生１个随机数．
        游戏结束：数字不能合并，也没有空白位置．
    架构：
            逻辑处理模块     　　　　　　　　　　Controller
            界面视图模块(控制台／pygame/.....)View
            数据模型模块..
            程序入口模块
    步骤：
    　　（一）逻辑处理模块 
             创建游戏核心类GameCoreController
             (1)将核心算法粘贴进来16:28
             (2)将所有参数，改为成员变量．
             (3)产生新数字
             　　　-- 计算所有空白位置(为０的位置).
                   -- 随机选择一个位置
                   -- 根据概率产生数字，存入列表的相应位置．
         （二）界面视图模块
         　　　创建游戏核心类对象
         　　　调用核心类对象的生成数字方法
            　　while True:
                  呈现界面
                  获取用户输入，调用核心类对象的移动方法．　
                  产生随机数
"""

import random
import copy
from project_month01.model import Direction

class GameCoreController:
    '''
       游戏核心控制器
    '''
    def __init__(self):
        #test.move
        # self.__map = [
        #                 [2, 0, 0, 2],
        #                 [2, 2, 0, 0],
        #                 [2, 0, 4, 4],
        #                 [4, 0, 0, 2]
        #              ]
        self.__map = [
                        [0] * 4,
                        [0] * 4,
                        [0] * 4,
                        [0] * 4
                     ]

        # test.game_over
        # self.__map = [
        #     [2, 4, 2, 4],
        #     [8, 16, 4, 32],
        #     [32, 4, 2, 64],
        #     [64, 32, 16, 0],
        # ]

        #insert_random_number for myself used
        # self.__random_list = [2,2,2,2,2,2,2,2,2,4]

    @property
    def map(self):
        return self.__map

    @map.setter
    def map(self,value):
        self.__map = value

    def __zero_to_end(self, line):
        #定义函数,将零元素移动到末尾
        for i in range(len(line) - 1, -1, -1):
            if line[i] == 0:
                del line[i]
                line.append(0)

    def __merge(self, line):
        #合并一列函数
        self.__zero_to_end(line)
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                line[i] += line[i + 1]
                line[i + 1] = 0
        self.__zero_to_end(line)

    def __move_left(self):
        #左移
        for r in range(len(self.map)):
            self.__merge(self.map[r])

    def __move_right(self):
        #右移
        for r in range(len(self.map)):
            list_merge = self.map[r][::-1]
            self.__merge(list_merge)
            self.map[r] = list_merge[::-1]

    def __move_up(self):
        #上移
        for c in range(4):
            list_merge = []
            for r in range(4):
                list_merge.append(self.map[r][c])

            self.__merge(list_merge)
            for r in range(4):
                self.map[r][c] = list_merge[r]

    def __move_down(self):
        #下移
        for c in range(4):
            list_merge = []
            for r in range(3, -1, -1):
                list_merge.append(self.map[r][c])

            self.__merge(list_merge)
            for r in range(3, -1, -1):
                self.map[r][c] = list_merge[3 - r]

    #myself
    def check_zero(self):
        L = []
        for r in range(4):
            for c in range(4):
                if self.map[r][c] == 0:
                    L.append((r,c))
        return L

    # myself
    def insert_random_number(self):
        #生成为零列表
        zero_list = self.check_zero()
        if not zero_list:
            return

        #生成随机数
            #myself
            # insert_number = random.choice(self.__random_list)
        # teacher
        insert_number = 4 if random.randint(1,10) == 1 else 2


        # print(zero_list)    #测试代码
        # print(insert_number) #测试代码

        #把随机数放进为零列表
        x,y = random.choice(zero_list)
        self.map[x][y] = insert_number

    def get_width(self):
        width = 0
        for r in range(4):
            for c in range(4):
                if width < self.map[r][c]:
                    width = self.map[r][c]
        width = len(str(width))
        return width

    def move(self,dir):
        L = copy.deepcopy(self.__map)
        if dir == Direction.up:
            self.__move_up()
        elif dir == Direction.down:
            self.__move_down()
        elif dir == Direction.left:
            self.__move_left()
        elif dir == Direction.right:
            self.__move_right()
        return not(L == self.__map)

    def is_game_over(self):
        """
            游戏是否结束
        :return:
        """
        # 1. 如果有空位置 游戏不能结束
        L = self.check_zero()
        if len(L) > 0:
            return False

        # # 2. 横向具有相同元素　游戏不能结束
        # for r in range(4):
        #     for c in range(3):
        #         if self.__map[r][c] == self.__map[r][c+1]:
        #             return False
        #
        # # 3. 竖向具有相同元素　游戏不能结束
        # for c in range(4):
        #     for r in range(3):
        #         if self.__map[r][c] == self.__map[r+1][c]:
        #             return False

        # (扩展)　2 + 3  横向同时竖向　比较是否具有相同元素
        for r in range(4):
            for c in range(3):
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[c][r] == self.__map[c + 1][r]:
                    return False

        return True  # 如果以上条件都不满足，则游戏结束

#-----------------------以下是测试代码--------------------------------------------------------

if __name__ == "__main__":
    c1 = GameCoreController()

    def print_map(L):
        for r in range(len(L.map)):
            for c in range(len(L.map[r])):
                print(L.map[r][c],end = " ")
            print()
    # c1.move_left()
    c1.insert_random_number()
    print_map(c1)