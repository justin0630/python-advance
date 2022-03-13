import pygame
import sys
import math
import random


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
background = pygame.image.load("pygame/20220313/snow.jpg")
width = background.get_width()
height = background.get_height()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Game")

typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render('Start', True, BLACK)
tit_w = title.get_width()
tit_h = title.get_height()

act = False

x_site = random.randrange(0, width)
y_site = random.randrange(-10, -1)
radius = random.randint(4, 6)
x_shift = random.randint(-5, 5)
clock = pygame.time.Clock()
count = 0
while True:
    if count <= 10:
        count += 1
    else:
        count = 0
        x_shift = random.randint(-5, 5)
    clock.tick(40)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                act = not (act)

    screen.blit(background, (0, 0))
    screen.blit(title, (0, 0))
    if act == True:
        title = font.render('Start', True, BLACK)
    else:
        title = font.render('Stop', True, BLACK)
        pygame.draw.circle(screen, WHITE, (x_site, y_site), radius)
        x_site += x_shift
        y_site += radius

        if y_site > height or x_site > width:
            y_site = random.randrange(-10, -1)
            x_site = random.randrange(0, width)
    pygame.display.update()
