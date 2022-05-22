#===載入套件開始===
from turtle import begin_poly
import pygame
import sys
import os
import random

os.chdir(sys.path[0])
from pygame.locals import *
#***載入套件結束***

#===初始化設定開始===
pygame.init()
clock = pygame.time.Clock()
timer = 0
MISSILE_MAX = 200
pygame.mixer.music.load("hit.mp3")
#***初始化設定結束***

#===載入圖片開始===
img_bg = pygame.image.load("space.png")
img_sship = [
    pygame.image.load("fighter_M.png"),
    pygame.image.load("fighter_L.png"),
    pygame.image.load("fighter_R.png"),
]

img_burn = pygame.image.load("starship_burner.png")
img_emy_burn = pygame.transform.rotate(img_burn, 180)

img_weapon = pygame.image.load("bullet.png")
img_enemy = pygame.image.load("enemy1.png")
img_enemy2 = pygame.image.load("enemy2.png")
#***載入圖片結束***

#===遊戲視窗設定開始===
bg_x = img_bg.get_width()
bg_y = img_bg.get_height()
bg_size = (bg_x, bg_y)
pygame.display.set_caption("Galaxy Lancer")
screen = pygame.display.set_mode(bg_size)
#***遊戲視窗設定結束***

#===捲動背景設定開始===
roll_y = 0


def roll_bg(win):
    global roll_y
    roll_y = (roll_y + 20) % bg_y
    win.blit(img_bg, [0, roll_y - bg_y])
    win.blit(img_bg, [0, roll_y])


#===捲動背景設定結束===

#===我機設定開始===
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship[0].get_width() / 2
ss_hh = img_sship[0].get_height() / 2
burn_w, burn_h = img_burn.get_rect().size
ss_sur = img_sship[0]


def move_starship(win, key, timer):
    global ss_x, ss_y, ss_sur

    ss_sur = img_sship[0]
    if key[pygame.K_UP]:
        ss_y -= 20
        if ss_y < ss_hh:
            ss_y = ss_hh
    if key[pygame.K_DOWN]:
        ss_y += 20
        if ss_y > bg_y - ss_hh:
            ss_y = bg_y - ss_hh
    if key[pygame.K_LEFT]:
        ss_x -= 20
        ss_sur = img_sship[1]
        if ss_x < ss_wh:
            ss_x = ss_wh
    if key[pygame.K_RIGHT]:
        ss_x += 20
        ss_sur = img_sship[2]
        if ss_x > bg_x - ss_wh:
            ss_x = bg_x - ss_wh

    win.blit(img_burn, [ss_x - burn_w / 2, ss_y + burn_h + (timer % 5) * 2])
    win.blit(ss_sur, [ss_x - ss_wh, ss_y - ss_hh])


#***我機設定結束***

#===飛彈設定開始===
msl_no = 0
msl_f = [False] * MISSILE_MAX
msl_x = [0] * MISSILE_MAX
msl_y = [0] * MISSILE_MAX
msl_wh = img_weapon.get_width() / 2
msl_hh = img_weapon.get_height() / 2
msl_shift = 30


def move_missile(win, key, timer):
    global msl_f, msl_x, msl_y, msl_no
    if key[K_SPACE]:
        if timer % 5 == 0:
            if msl_f[msl_no] == False:
                msl_f[msl_no] = True
                msl_x[msl_no] = ss_x - msl_wh
                msl_y[msl_no] = ss_y - msl_hh
                msl_no += 1
                msl_no %= MISSILE_MAX

    for i in range(MISSILE_MAX):
        if msl_f[i] == True:
            msl_y[i] -= msl_shift
            win.blit(img_weapon, [msl_x[i], msl_y[i]])
        if msl_y[i] < 0:
            msl_f[i] = False


#***飛彈設定結束***

#===敵機1設定開始===
emy_f = False
emy_x = 0
emy_y = bg_y + 10
emy_wh = img_enemy.get_width() / 2
emy_hh = img_enemy.get_height() / 2
emy_shift = 5
emy_dist = int(emy_wh + emy_hh)
emy_burn_w, emy_burn_h = img_emy_burn.get_rect().size


def move_enemy(win):
    global emy_f, emy_x, emy_y, score
    if emy_y > bg_y:
        emy_f = True
        emy_x = random.randint(int(emy_wh), int(bg_x - emy_wh))
        emy_y = random.randint(int(emy_hh), int(emy_hh + 100))
    if emy_f == True:
        emy_y += emy_shift
        for n in range(MISSILE_MAX):
            if msl_f[n] == True and is_hit(emy_x, emy_y, msl_x[n], msl_y[n],
                                           emy_dist):
                pygame.mixer.music.play()
                msl_f[n] = False
                emy_f = False
                emy_y = bg_y + 10
                score += 1

        win.blit(
            img_emy_burn,
            [emy_x - emy_burn_w / 2, emy_y - (emy_burn_h + (timer % 3) * 2)])
        win.blit(img_enemy, [emy_x - emy_wh, emy_y - emy_hh])


#***敵機1設定結束***

#===敵機2設定開始===
emy2_f = False
emy2_x = 0
emy2_y = bg_y + 10
emy2_wh = img_enemy2.get_width() / 2
emy2_hh = img_enemy2.get_height() / 2
emy2_shift = 5
emy2_dist = int(emy2_wh + emy2_hh)
emy2_burn_w, emy2_burn_h = img_emy_burn.get_rect().size


def move_enemy2(win):
    global emy2_f, emy2_x, emy2_y, score
    if emy2_y > bg_y:
        emy2_f = True
        emy2_x = random.randint(int(emy2_wh), int(bg_x - emy2_wh))
        emy2_y = random.randint(int(emy2_hh), int(emy2_hh + 100))
    if emy2_f == True:
        emy2_y += emy2_shift
        for n in range(MISSILE_MAX):
            if msl_f[n] == True and is_hit(emy2_x, emy2_y, msl_x[n], msl_y[n],
                                           emy2_dist):
                pygame.mixer.music.play()
                msl_f[n] = False
                emy2_f = False
                emy2_y = bg_y + 10
                score += 1
        win.blit(img_emy_burn, [
            emy2_x - emy2_burn_w / 2, emy2_y - (emy2_burn_h + (timer % 3) * 2)
        ])
        win.blit(img_enemy2, [emy2_x - emy2_wh, emy2_y - emy2_hh])


#***敵機2設定開始***


#===碰撞偵測設定開始===
def is_hit(x1, y1, x2, y2, r):  #計算是否碰撞
    if ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) < (r * r):
        return True
    else:
        return False


#***碰撞偵測設定結束***

#===爆炸設定開始===

#***爆炸設定結束***

#===分數設定開始===
score = 0  #分數計數
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 36)


def get_score(win):
    global score, score_sur
    score_sur = score_font.render(str(score), True, [250, 0, 250])
    win.blit(score_sur, [10, 10])


#***分數設定結束***

#===保護罩設定開始===

#***保護罩設定結束***

#===主程式開始===
while True:
    clock.tick(30)
    key = pygame.key.get_pressed()
    timer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F1:
                screen = pygame.display.set_mode(bg_size, FULLSCREEN)
            elif event.key == K_ESCAPE:
                screen = pygame.display.set_mode(bg_size)
    roll_bg(screen)
    move_starship(screen, key, timer)
    move_missile(screen, key, timer)
    move_enemy(screen)
    move_enemy2(screen)
    get_score(screen)
    pygame.display.update()

#===主程式結束===
