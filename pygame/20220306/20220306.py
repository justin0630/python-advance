import pygame
import sys

pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
