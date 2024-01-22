import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200, 750))

pygame.display.set_caption("Sort-Search-Algorithm-Visualizer")
gif_path = 'C:\\Users\\Hari\\Documents\\sort-search-algorithm-visualizer\\MAIN\\Visualization\\d9egxsf-87b043c7-f5a9-49b9-8a50-7abf4f4a03b7.gif'

gif_image = pygame.image.load(gif_path)
gif_rect = gif_image.get_rect()

x, y = 100, 100
gif_rect.topleft = (x, y)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear the screen
    screen.fill((5, 22, 26))

    # Blit the GIF onto the screen
    screen.blit(gif_image, gif_rect)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)
