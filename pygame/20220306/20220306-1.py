import pygame
import sys
import math

pygame.init()
WHITE = (255, 255, 255)
width = 640
height = 320
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("My First Game")
background = pygame.Surface((width, height))
background.fill((WHITE))

act = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            act = not (act)

    if act:
        pygame.draw.circle(background, (0, 0, 255), (400, 300), 30, 0)
        pygame.draw.rect(background, (0, 255, 0), [270, 130, 50, 35], 5)
        pygame.draw.ellipse(background, (255, 0, 0), [130, 160, 60, 35], 35)
        pygame.draw.line(background, (255, 0, 255), (280, 220), (320, 220), 3)
        pygame.draw.polygon(background, (100, 200, 45),
                            [[100, 100], [0, 100], [50, 150]], 0)
        pygame.draw.arc(background, (255, 10, 0), [100, 100, 100, 50],
                        math.radians(180), math.radians(0), 2)
    else:
        background.fill(WHITE)
    screen.blit(background, (0, 0))
    pygame.display.update()
