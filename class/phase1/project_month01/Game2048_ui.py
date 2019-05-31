from project_month01.Controller2048 import GameCoreController
from project_month01.Controller2048 import Direction
import copy
import os



class GameView:
    def __init__(self):
        self.__controller = GameCoreController()
        self.__controller.insert_random_number()
        self.__controller.insert_random_number()

    def __print_map(self):
        os.system("clear")
        fmt = '{0:{1}}'
        width = self.__controller.get_width()
        for r in range(len(self.__controller.map)):
            for c in range(len(self.__controller.map[r])):
                print(fmt.format('%d'%self.__controller.map[r][c],width),end = " ")
            #     print("%d"%self.__controller.map[r][c], end=" ")
            print()

    def __input(self):
        operation = input("w:上 s:下 a:左 d:右")
        if operation == "w":
            return self.__controller.move(Direction.up)
        elif operation == "s":
            return self.__controller.move(Direction.down)
        elif operation == "a":
            return self.__controller.move(Direction.left)
        elif operation == "d":
            return self.__controller.move(Direction.right)

    def main(self):
        self.__print_map()
        while True:
            #myself
            # self.__print_map()
            # L = copy.deepcopy(self.__controller.map)
            # self.__input()
            # if L == self.__controller.map:
            #     continue
            # self.__controller.insert_random_number()

            #refer to teacher
            if self.__input():
                self.__controller.insert_random_number()
                self.__print_map()
                if self.__controller.is_game_over():
                    print("game over")
                    break


if __name__ == "__main__":
    g1 = GameView()
    g1.main()