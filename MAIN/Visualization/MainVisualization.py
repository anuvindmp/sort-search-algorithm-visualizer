import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,750))
clock = pygame.time.Clock()
pygame.display.set_caption("Sort-Search-Algorithm-Visualizer")
gif_path = 'giphy.gif'
gif_image = pygame.image.load(gif_path)
gif_rect = gif_image.get_rect()

# Set the initial position for the image
x, y = 100, 100
gif_rect.topleft = (x, y)
# pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((5,22,26))
    pygame.display.update()
    clock.tick(60)

    