import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200,750))
clock = pygame.time.Clock()
pygame.display.set_caption("Bubble sort")


fontPath1 = 'MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf'
fontHead = pygame.font.Font(fontPath1, 35)
text = fontHead.render("BUBBLE SORT",True, (109,165,192))





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((5,22,26))

    screen.blit(text, (50, 50))
    pygame.display.update()
    clock.tick(60)


