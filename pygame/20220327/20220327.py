import pygame
import sys
import random


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()  #初始化
bg = pygame.image.load("pygame/20220327/Gophers_BG_800x600.png")
bg_x = bg.get_width()
bg_y = bg.get_height()

screen = pygame.display.set_mode([bg_x, bg_y])  #設定窗口
pygame.display.set_caption("打地鼠")
sur = pygame.Surface([bg_x, bg_y])  #繪製背景容器

gophers = pygame.image.load("pygame/20220327/Gophers150.png")  #地鼠圖片

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450],
        [610, 450]]  #六個位置
tick = 0  #計數器
max_tick = 20
pos = pos6[0]  #外面記錄圓的位置
#分數
score = 0  #分數計數
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if check_click(mpos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                tick = max_tick + 1
                score += 1

    #每幀循環執行的代碼
    if tick > max_tick:
        new_pos = random.randint(0, 5)  #隨機0到5
        pos = pos6[new_pos]  #更新外部記錄的圓的位置
        tick = 0  #重置計數器
    else:  #不刷新變換的時候
        tick += 1  #增加計數器
    sur.blit(bg, (0, 0))
    sur.blit(
        gophers,
        (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))
    screen.blit(sur, (0, 0))

    score_sur = score_font.render(str(score), False, RED)  #生成計數表面
    screen.blit(score_sur, (10, 10))  #增加分數表面
    pygame.display.update()
