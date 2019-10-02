# coding=utf8
#2048游戏引擎：驱动整个2048小游戏
#1、初始化，输出界面
#2、获得控制，执行逻辑
#3、做结束判断
#4、返回逻辑开始，重复循环过程
#游戏的图形引擎功能：
#将地图人物的位置信息传送给图形引擎，去进行渲染输出整个界面
import sys
import os
import random
import itertools

class Game:
    grid = []
    controls = ["w","a","s","d"]

    def rnd_field(self):
        number = random.choice([4,2,4,2,4,2,4,2,4,2,4,2])
       x , y = random.choice([(x,y) for x, y in itertools.product([0,1,2,3],[0,1,2,3])] if self.grid(x=0,y=0)) ]



    #等于游戏的图形引擎，将地图人物的
    # 位置信息传送给图形引擎，去进行渲染输出整个界面
    #负责打印整个棋盘
    def print_screen(self):
        #清空整个屏幕
        os.system('clear')
        print('-' * 21)
        for row in self.grid:
            print('|{}|'.format("|".join([str(col or ' ').center(4) for col in row])))
            print('-' * 21)

    def logic(self,control):
        return 0, '' # 1, "You Win!"  -1,"You Lost"

    #游戏的主事件
    def Main_loop(self):
        self.grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.rnd_field()
        self.rnd_field()
        while True:
            self.print_screen()
            control = input('input w/a/s/d:')
            if control in self.controls:
                status, info = self.logic(control)
                if status:
                    print(info)
                    if input('Start another game?[Y/n]').lower() == "y":
                        break
                    else:
                        sys.exit(0)
            self.main_loop()

if __name__=="__main__":
    Game().Main_loop()



