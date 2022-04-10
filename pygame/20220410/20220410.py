import pygame
import sys
import random
import os
import time

os.chdir(sys.path[0])
from pygame.locals import *


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()  #初始化
bg = pygame.image.load("Gophers_BG_800x600.png")
bg_x = bg.get_width()
bg_y = bg.get_height()

screen = pygame.display.set_mode([bg_x, bg_y])  #設定窗口
pygame.display.set_caption("打地鼠")
sur = pygame.Surface([bg_x, bg_y])  #繪製背景容器

gophers = pygame.image.load("Gophers150.png")  #地鼠圖片

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450],
        [610, 450]]  #六個位置
tick = 0  #計數器
max_tick = 20
pos = pos6[0]  #外面記錄圓的位置
times = 0
times_max = 20
#分數
score = 0  #分數計數
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)

end_font = pygame.font.Font(typeface, 24)
end_sur = end_font.render(str(times), True, RED)
clock = pygame.time.Clock()

ham1 = pygame.image.load("Hammer1.png")
ham2 = pygame.image.load("Hammer2.png")
gophers = pygame.image.load("Gophers150.png")
gophers2 = pygame.image.load("Gophers2_150.png")
pygame.mixer.music.load("大叫聲.mp3")
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)  #隱藏滑鼠
mpos = (0, 0)

while True:
    clock.tick(30)
    hammer = ham2
    hitsur = gophers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            hammer = ham1
            mpos = pygame.mouse.get_pos()
            if check_click(mpos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                if times < times_max:
                    tick = max_tick + 1
                    pygame.mixer.music.play()
                    score = score + 1
                    hitsur = gophers2
        elif event.type == MOUSEMOTION:
            mpos = pygame.mouse.get_pos()
    if times > times_max:
        sur.fill((0, 0, 0))
        pygame.mouse.set_visible(True)
        end_sur = score_font.render(
            "Your score is:{}/{}".format(score, times_max), False, RED)
        screen.blit(sur, (0, 0))
        screen.blit(end_sur, (100, 100))  #增加分數表面
        pygame.display.update()
    else:  #每幀循環執行的代碼
        if tick > max_tick:
            times += 1
            new_pos = random.randint(0, 5)  #隨機0到5
            pos = pos6[new_pos]  #更新外部記錄的圓的位置
            tick = 0  #重置計數器
        else:  #不刷新變換的時候
            tick += 1  #增加計數器
        sur.blit(bg, (0, 0))
        sur.blit(hitsur, (pos[0] - hitsur.get_width() / 2,
                          pos[1] - hitsur.get_height() / 2))
        # pygame.draw.circle(sur, BLUE, mpos, 10)  #在滑鼠位置畫藍色圓
        sur.blit(hammer, (mpos[0] - hammer.get_width() / 2,
                          mpos[1] - hammer.get_height() / 2))
        screen.blit(sur, (0, 0))

        score_sur = score_font.render(str(score), False, RED)  #生成計數表面
        screen.blit(score_sur, (10, 10))  #增加分數表面
        pygame.display.update()
        if (hammer == ham1 or hitsur == gophers2):
            time.sleep(0.2)
        if score >= 15:
            sur.fill((0, 0, 255))
            pygame.mouse.set_visible(True)
            end_sur = score_font.render(
                "Your score is:{}/{}".format(score, times_max), False, RED)
            screen.blit(sur, (0, 0))
            screen.blit(end_sur, (100, 100))  #增加分數表面
            pygame.display.update()
