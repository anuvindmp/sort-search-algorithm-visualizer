import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,750))
clock = pygame.time.Clock()
pygame.display.set_caption("Sort-Search-Algorithm-Visualizer")
# icon = pygame.image.load("")
# pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((5,22,26))
    pygame.display.update()
    clock.tick(60)

    