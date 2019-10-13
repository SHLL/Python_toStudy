# 详情见： https://www.bilibili.com/video/av70478439
# 补全show方法，该方法用来显示打印棋盘，简单的同过cmd页面展示程序效果
# show方法参照 ： https://blog.csdn.net/qq_42197548/article/details/85073198
class Gomoku:

    def __init__(self):
        self.g_map = [[0 for y in range(15)] for x in range(15)]        # 棋盘状态
        self.cur_step = 0   # 步数
        pass

    def move_lstep(self):
        # 玩家落子
        while True:
            try:
                pos_x = int(input('x: '))       # 接收玩家的输入
                pos_y = int(input('y: '))
                if 0 <= pos_x <= 14 and 0 <= pos_y <=14:    # 判断这个各自能否落子
                    if self.g_map[pos_x][pos_y] == 0:
                        self.g_map[pos_x][pos_y] = 1
                        self.cur_step += 1
                        return
            except ValueError:  # 玩家输入不正常的情况
                continue

    def game_result(self):
        # 判断游戏的结局，0为游戏进行中，1为玩家获胜，2为电脑获胜，3为平局
        # 1，判断是否横向连续五子
        for x in range(11):
            for y in range(11):
                if self.g_map[x-4][y] == 1 and self.g_map[x-3][y] == 1 and self.g_map[x-2][y] == 1 and self.g_map[x-1][y] == 1 and self.g_map[x][y] == 1:
                    return 1
                if self.g_map[x-4][y] == 2 and self.g_map[x-3][y] == 2 and self.g_map[x-2][y] == 2 and self.g_map[x-1][y] == 2 and self.g_map[x][y] == 2:
                    return 2
        # 2，判断是否纵向连续五子
        for x in range(11):
            for y in range(11):
                if self.g_map[x][y-4] == 1 and self.g_map[x][y-3] == 1 and self.g_map[x][y-2] == 1 and self.g_map[x][y-1] == 1 and self.g_map[x][y] == 1:
                    return 1
                if self.g_map[x][y-4] == 2 and self.g_map[x][y-3] == 2 and self.g_map[x][y-2] == 2 and self.g_map[x][y-1] == 2 and self.g_map[x][y] == 2:
                    return 2
        # 3，判断是否有左上-右下的连续五子
        for x in range(11):
            for y in range(11):
                if self.g_map[x-4][y] == 1 and self.g_map[x-3][y+1] == 1 and self.g_map[x-2][y+2] == 1 and self.g_map[x-1][y+3] == 1 and self.g_map[x][y+4] == 1:
                    return 1
                if self.g_map[x-4][y] == 2 and self.g_map[x-3][y+1] == 2 and self.g_map[x-2][y+2] == 2 and self.g_map[x-1][y+3] == 2 and self.g_map[x][y+4] == 2:
                    return 2
        # 4，判断是否有右上-左下的连续五子
        for x in range(11):
            for y in range(11):
                if self.g_map[x+4][y] == 1 and self.g_map[x+3][y+1] == 1 and self.g_map[x+2][y+2] == 1 and self.g_map[x+1][y+3] == 1 and self.g_map[x][y+4] == 1:
                    return 1
                if self.g_map[x+4][y] == 2 and self.g_map[x+3][y+1] == 2 and self.g_map[x+2][y+2] == 2 and self.g_map[x+1][y+3] == 2 and self.g_map[x][y+4] == 2:
                    return 2
        # 5， 判断是否为平局
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:   # 棋盘中还剩余的格子，不能判断为平局
                    return 0
        return 3

    def ai_move_lstep(self):
        # 电脑落子
        for x in range(15):
            for y in range(15):
                if self.g_map[x][y] == 0:
                    self.g_map[x][y] = 2
                    self.cur_step += 1
                    return

    def show(self):
        # 显示游戏内容
        # 补全show方法，该方法用来显示打印棋盘，简单的同过cmd页面展示程序效果
        pass

    def play(self):
        while True:
            self.move_lstep()       # 玩家下一步
            res = self.game_result()  # 判断游戏结果
            if res != 0:                # 如果游戏结果为“已经结束”，则显示游戏内容，并退出主循环
                self.show(res)
                return
            self.ai_move_lstep()        # 电脑下一步
            res = self.game_result()
            if res != 0:
                self.show(res)
                return
            self.show(0)



