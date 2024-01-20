import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('TJ CREAM')
icon = pygame.image.load('test and examples/pygame/icon.png')
pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        screen.fill((25,255,0))
        pygame.display.update()
        clock.tick(60)

