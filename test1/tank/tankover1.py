#添加音效
#音效暂定格式为：
#         music = Music('image/tankG1.mp3')
#         music.play()
#       直接添加至需要调用的位置即可
#加载我方坦克
import pygame,time,random
from pygame.sprite import Sprite
SCREEN_WIDTH=700
SCREEN_HEIGHT=500
BG_COLOR=pygame.Color(0,0,0)
TEXT_COLOR=pygame.Color(255,0,0)
#定义一个基类
class BaseItem(Sprite):
    def __init__(self,color,width,height):
        #Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

class MainGame():
    window=None
    my_tank=None
    #存储敌方坦克的列表
    enemyTankList = []
    #定义地方坦克的数量
    enemyTankCount = 5
    #存储我方子弹的列表
    myBulletList=[]
    #存储敌方子弹的列表
    enemyBulletList=[]
    #存储爆炸效果的列表
    explodeList=[]
    #存储墙壁的列表
    WallList = []
    def __init__(self):
        pass
    #开始游戏
    def startGame(self):
        #加载主窗口
        #初始化窗口
        pygame.display.init()
        #设置窗口的大小及显示
        MainGame.window=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        #初始化我方坦克
        self.createMyTank()
        #初始化敌方坦克并添加到列表中
        self.createEnemyTank()
        #初始化墙壁
        self.createWall()
        #设置窗口标题
        pygame.display.set_caption('坦克大战1.03')
        #添加音乐
        self.playMusic()
        #使窗口始终显示|刷新
        while True:
            #使坦克移动的速度频率降低
            time.sleep(0.02)
            #给窗口设置填充颜色
            MainGame.window.fill(BG_COLOR)
            #获取事件
            self.getEvent()
            #绘制文字
            MainGame.window.blit(self.getTextSuface('敌方坦克剩余数量%d'%len(MainGame.enemyTankList)),(10,10))
            MainGame.window.blit(self.getTextSuface('T复活、G墙壁修复（全损）、V、敌方坦克回复'),(10,25))
            #调用坦克显示的方法
            #判断我方坦克是否存活
            self.blitMyTank()
            #循环遍历敌方坦克列表，展示敌方坦克
            self.blitEnemyTank()
            #循环历遍显示我方坦克的子弹
            self.blitMyBullet()
            #循环历遍显示敌方坦克的子弹
            self.blitEnemyBullet()
            #循环遍历爆炸列表，展示爆炸效果
            self.blitExplode()
            #循环遍历Wall列表，展示墙壁
            self.blitWall()
            #调用坦克移动的方法
            #如果坦克的移动开关是True则移动
            pygame.display.update()

    #播放音乐的方法
    def playMusic(self):
        # 创建music对象
        music = Music('image/tankG1.mp3')
        # 播放音乐
        music.play()

    #显示我方坦克的方法
    def blitMyTank(self):

        # 判断我方坦克是否存活
        if MainGame.my_tank and MainGame.my_tank.live:
            MainGame.my_tank.displayTank()
        else:  # 删除我方坦克
            del MainGame.my_tank
            MainGame.my_tank = None

            # 调用坦克移动的方法
            # 如果坦克的移动开关是True则移动
        if MainGame.my_tank and MainGame.my_tank.live:
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()
                # 调用检测是否发生碰撞的方法
                MainGame.my_tank.thitWall()
                # 检测我方坦克是否与敌方坦克发生碰撞
                MainGame.my_tank.myTank_hit_enemyTank()



    #循环遍历敌方坦克列表，展示敌方坦克
    def blitEnemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            #判断当前敌方坦克是否存活
            if enemyTank.live:
                enemyTank.displayTank()
                enemyTank.randMove()
                #调用检测是否与墙壁碰撞的方法
                enemyTank.thitWall()
                #检测是否与我方坦克碰撞
                enemyTank.enemyTank_hit_myTank()
                # 发射子弹
                enemyBullet = enemyTank.shot()
                # 判断地方子弹是否是None，如果不为None则添加到地方子弹列表中
                if enemyBullet:
                    # 将敌方子弹存储到敌方子弹列表
                    MainGame.enemyBulletList.append(enemyBullet)
            else:
                #从敌方坦克列表中移除
                MainGame.enemyTankList.remove(enemyTank)

    def blitExplode(self):
        for explode in MainGame.explodeList:
            #判断是否或者
            if explode.live:
                #展示
                explode.displayExplode()
            else:
                #在爆炸列表中移除
                MainGame.explodeList.remove(explode)

    #历遍墙壁列表，调用显示的方法
    def blitWall(self):
        for wall in MainGame.WallList:
            if wall.live:
                #调用墙壁显示的方法
                wall.displayWall()
            else:
                #从列表移除
                MainGame.WallList.remove(wall)

    #遍历我方子弹列表，调用显示的方法
    def blitMyBullet(self):
        for myBullet in MainGame.myBulletList:
            #判断当前的子弹状态是否存活，是则显示及移动
            if myBullet.live:
                myBullet.displayBullet()
                # 调用子弹的移动方法
                myBullet.move()
                #调用检测我方坦克是否与敌方坦克发生碰撞
                myBullet.myBullet_hit_enemyTank()
                #检测我方子弹是否与墙壁碰撞
                myBullet.hitWall()

            #否则在列表里删除
            else:
                MainGame.myBulletList.remove(myBullet)

    #历遍敌方子弹，调用显示的方法
    def blitEnemyBullet(self):
        for enemyBullet in MainGame.enemyBulletList:
            if enemyBullet.live:
                enemyBullet.displayBullet()
                enemyBullet.move()
                #调用敌方子弹与我方坦克碰撞的方法
                enemyBullet.enemyBullet_hit_myTank()
                #检测地方子弹是否与墙壁接触
                enemyBullet.hitWall()
            else:
                MainGame.enemyBulletList.remove(enemyBullet)

    #初始敌方坦克的方法，并且添加到敌方坦克列表中
    def createEnemyTank(self):
        top=100
        #循环生成敌方坦克
        for i in range(MainGame.enemyTankCount):
            left = random.randint(0,600)
            speed = random.randint(1,4)
            enemy = EnemyTank(left,top,speed)
            MainGame.enemyTankList.append(enemy)

    #创建墙壁的方法
    def createWall(self):
        #初始化墙壁
        for i in range(5):
            wall=Wall(i*160,220)
            #将墙壁添加到墙壁列表中
            MainGame.WallList.append(wall)

    #创建我方坦克的方法
    def createMyTank(self):
        MainGame.my_tank = MyTank(317, 323)


    #结束游戏
    def endGame(self):
        print('退出事件成功')
        exit()


    #左上角文字的绘制
    def getTextSuface(self,text):
        #初始化字体模块
        pygame.font.init()
        #查看所有的字体
        #print(pygame.font.get_fonts())
        #获取字体Fontd对象
        font = pygame.font.SysFont('kaiti',18)
        #绘制文字信息
        textSurface=font.render(text,True,TEXT_COLOR)
        return textSurface
    #获取事件
    def getEvent(self):
        #获取所有事件
        eventList=pygame.event.get()
        #遍历事件
        for event in eventList:
            #判断按下的键是关闭还是键盘按下
            #如果触发的是退出，关闭窗口
            if event.type == pygame.QUIT:
                self.endGame()

            if event.type == pygame.KEYDOWN:
                #当坦克不存在死亡时
                if not MainGame.my_tank:
                    #判断按下的键位，让坦克重生
                    if event.key == pygame.K_t:
                        #坦克重生（调用创建坦克的方法）
                        self.createMyTank()
                #刷新敌方坦克的存在状态
                if not MainGame.enemyTankList:
                    if event.key == pygame.K_v:
                        self.createEnemyTank()

                #刷新墙壁的存在状态
                if not MainGame.WallList:
                    if event.key == pygame.K_g:
                        self.createWall()

                if MainGame.my_tank and MainGame.my_tank.live:
                    # 判断触发的键位
                    if event.key == pygame.K_LEFT:
                        # 切换方向
                        MainGame.my_tank.direction = 'L'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print('左')
                    elif event.key == pygame.K_RIGHT:
                        MainGame.my_tank.direction = 'R'
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print('右')
                    elif event.key == pygame.K_UP:
                        MainGame.my_tank.direction = 'U'
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print('上')
                    elif event.key == pygame.K_DOWN:
                        MainGame.my_tank.direction = 'D'
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print('下')
                    elif event.key == pygame.K_SPACE:
                        # 创建我方发射的子弹
                        # 如果当前我方子弹列表的大小 小于等于3时候在可以创建
                        if len(MainGame.myBulletList) < 3:
                            myBullet = Bullet(MainGame.my_tank)
                            MainGame.myBulletList.append(myBullet)
                            print("pa")


            #松开方向键停止修改Stop的状态值
            if event.type == pygame.KEYUP:
                    #判断松开的按键具体是哪个按键
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        if MainGame.my_tank and MainGame.my_tank.live:
                            MainGame.my_tank.stop = True



class Tank(BaseItem):
    #添加坦克距离左边left和上边top
    def __init__(self,left,top):
        #保存加载的图片
        self.images={
            'U':pygame.image.load('image/tankU.gif'),
            'D':pygame.image.load('image/tankD.gif'),
            'L':pygame.image.load('image/tankL.gif'),
            'R':pygame.image.load('image/tankR.gif')
        }
        #方向
        self.direction='U'
        #根据但钱图片的方向回去图片
        self.image=self.images[self.direction]
        #根据图片获取区域
        self.rect=self.image.get_rect()
        #设置区域的left和top
        self.rect.left=left
        self.rect.top=top
        #速度 决定移动的快慢
        self.speed=5
        #坦克移动的开关
        self.stop=True
        #是否存活
        self.live=True
        #新增属性原坐标
        self.oldLeft=self.rect.left
        self.oldTop=self.rect.top

    #移动
    def move(self):
        #移动 后记录移动后坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
        #判断坦克的方向来进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < SCREEN_WIDTH:
                self.rect.left += self.speed

    #射击
    def shot(self):
        return Bullet(self)

    def stay(self):
        self.rect.left=self.oldLeft
        self.rect.top=self.oldTop

    #检测坦克是否与墙壁发生碰撞
    def thitWall(self):
        for wall in MainGame.WallList:
            if pygame.sprite.collide_rect(self,wall):
                #将坐标设置为移动之前的坐标
                self.stay()

    #展示坦克的方法
    def displayTank(self):
        #获取展示的对象
        self.image=self.images[self.direction]
        #调用blit方法展示
        MainGame.window.blit(self.image,self.rect)

    #我方坦克
class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank, self).__init__(left,top)

    # 检测我方坦克与敌方坦克发生碰撞
    def myTank_hit_enemyTank(self):
        # 循环遍历敌方坦克列表
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(self, enemyTank):
                self.stay()

    #敌方坦克
class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        #调用父类的初始化方法
        super(EnemyTank, self).__init__(left,top)
        #加载敌方坦克图片集
        self.images={
            'U':pygame.image.load('image/enemyU.png'),
            'D':pygame.image.load('image/enemyD.png'),
            'L':pygame.image.load('image/enemyL.png'),
            'R':pygame.image.load('image/enemyR.png')
        }
        #方向，随机生成敌方坦克的方向
        self.direction = self.randDirection()
        #根据方向获取图片
        self.image=self.images[self.direction]
        #区域
        self.rect=self.image.get_rect()
        #对left和top进行赋值
        self.rect.left=left
        self.rect.top=top
        #速度
        self.speed=speed
        #移动开关键
        self.flag=True
        # 增加一个步数变量
        self.step = 60

    #检测敌方坦克与我方坦克碰撞的方法
    def enemyTank_hit_myTank(self):
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(self,MainGame.my_tank):
                self.stay()

    #随机生成敌方坦克的方向
    def randDirection(self):
        num = random.randint(1,4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'


    #敌方坦克随机移动的方法
    def randMove(self):
        if self.step <= 0 :
            #修改方向
            self.direction = self.randDirection()
            #让步数复位
            self.step=60
        else:
            self.move()
            #让步数递减
            self.step -= 1

    #重写shot()方法
    def shot(self):
        #随机生成100以内的数
        num=random.randint(1,100)
        if num < 4:
            return Bullet(self)




#子弹类
class Bullet(BaseItem):
    def __init__(self,tank):               #与403相似结构
        #加载图片
        self.image=pygame.image.load('image/enemymissile.png')
        #坦克的方向决定子弹的方向
        self.direction = tank.direction
        #获取区域
        self.rect = self.image.get_rect()
        #子弹的left，top与方向有关
        if self.direction == 'U':
            self.rect.left=tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top=tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left=tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top=tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left=tank.rect.left - self.rect.width/2 - self.rect.width/2
            self.rect.top=tank.rect.top + tank.rect.width/2 - self.rect.width/2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top=tank.rect.top + tank.rect.width /2 -self.rect.width/2
        #子弹的速度
        self.speed=6
        #子弹的状态,是否碰到墙壁,如果是则修改此状态
        self.live = True


    #移动
    def move(self):
        if self.direction == 'U':
            if self.rect.top>0:
                self.rect.top -= self.speed
            else:
                #修改子弹状态
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width <SCREEN_WIDTH:
                self.rect.left += self.speed
            else:
                # 修改子弹状态
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height <SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                # 修改子弹状态
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                # 修改子弹状态
                self.live = False

    #子弹是否碰撞墙壁
    def hitWall(self):
        #循环遍历墙壁列表取出墙壁的对象
        for wall in MainGame.WallList:
            if pygame.sprite.collide_rect(self,wall):
                #让子弹消失，修改子弹的生存状态live
                self.live=False
                #墙壁生命值减小
                wall.hp-=1
                if wall.hp<=0:
                    #修改墙壁的生存状态
                    wall.live=False
                    #在墙壁消失时，添加爆炸效果
                    explode = Explode(wall)
                    MainGame.explodeList.append(explode)

    #显示子弹的方法
    def displayBullet(self):
        #将图片suface加载到窗口
        MainGame.window.blit(self.image,self.rect)



    #我方子弹与地方坦克的碰撞
    def myBullet_hit_enemyTank(self):
        #循环遍历敌方坦克列表,判断是否发生碰撞
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(enemyTank,self):
                #修改敌方坦克和我方子弹的状态
                enemyTank.live=False
                self.live=False
                #创建爆炸对象
                explode=Explode(enemyTank)
                #将爆炸对象添加到爆炸列表中
                MainGame.explodeList.append(explode)

        # 敌方子弹与我方坦克的碰撞

    def enemyBullet_hit_myTank(self):
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank, self):
                # 产生爆炸对象
                explode = Explode(MainGame.my_tank)
                # 将爆炸对象添加到爆炸列表中
                MainGame.explodeList.append(explode)
                # 修改敌方子弹与我防坦克的状态
                self.live = False
                MainGame.my_tank.live = False

class Wall():
    def __init__(self,left,top):
        #加载图片
        self.image=pygame.image.load('image/well.png')
        #获取墙壁的区域
        self.rect=self.image.get_rect()
        #设置位置left,top
        self.rect.left=left
        self.rect.top=top
        #是否存活
        self.live=True
        #设置生命值
        self.hp = 3

    #展示墙壁的方法
    def displayWall(self):
        MainGame.window.blit(self.image,self.rect)

class Explode():
    def __init__(self,tank):  #此处需要将tank参数添加,否则会报错 见324行相似   Explode类与Bullet类相似
        #爆炸的位置如何决定
        self.rect = tank.rect
        #用images列表存储爆炸效果图
        self.images=[
            pygame.image.load('image/blast1.png'),
            pygame.image.load('image/blast2.png'),
            pygame.image.load('image/blast3.png'),
            pygame.image.load('image/blast4.png'),
            pygame.image.load('image/blast5.png')
        ]
        self.step=0
        self.image=self.images[self.step]
        #是否活着
        self.live=True


    #展示爆炸效果的方法
    def displayExplode(self):
        if self.step<len(self.images):
            # 根据索引获取爆炸对象
            self.image = self.images[self.step]
            self.step += 1
            #添加到主窗口
            MainGame.window.blit(self.image,self.rect)
        else:
            #修改存活状态
            self.live=False
            self.step=0

class Music():
    def __init__(self,filename):
        self.filename=filename
        #初始化音乐混合器
        pygame.mixer.init()
        #加载音乐
        pygame.mixer.music.load(self.filename)
    #播放音乐
    def play(self):
        pygame.mixer.music.play()


if __name__ =='__main__':
    MainGame().startGame()
    #MainGame.getTextSuface("")


