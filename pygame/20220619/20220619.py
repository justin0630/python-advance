#===載入套件開始===
import pygame
import sys
import os

os.chdir(sys.path[0])
from pygame.locals import *
import random

#===初始化設定開始===

BLOCK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()

clock = pygame.time.Clock()

act = False
bg_x = 800
bg_y = 600
bg_size = (bg_x, bg_y)
pygame.display.set_caption(u"打磚塊遊戲")
screen = pygame.display.set_mode(bg_size)

#===球設定開始===
ball_x = 400
ball_y = 300
ball_radius = 8
ball_diameter = ball_radius * 2
ball_color = WHITE
dx = 8
dy = -8


def ball_update(win):
    global ball_x, ball_y
    global dx, dy

    ball_x += dx
    ball_y += dy

    if (ball_x > bg_x - ball_diameter or ball_x < ball_diameter):
        dx = -dx
    if (ball_y > bg_y - ball_diameter or ball_y < ball_diameter):
        dy = -dy

    pygame.draw.circle(win, ball_color, [ball_x, ball_y], ball_radius)


while True:
    for event in pygame.event.get():
        '''離開遊戲'''
        if event.type == pygame.QUIT:
            sys.exit()
    '''清除畫面'''
    '''更新磚塊'''
    '''顯示磚塊數量'''
    '''顯示板子'''
    '''更新球'''
    ball_update(screen)
    '''更新畫面'''
    pygame.display.update()
    clock.tick(60)
