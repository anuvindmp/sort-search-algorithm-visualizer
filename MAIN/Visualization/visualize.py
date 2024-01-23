import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption("Bubble Sort Visualization")
clock = pygame.time.Clock()

# Constants
size = 50
BarWidth = 1200 // size
array = [random.randint(70, 750 - 50) for i in range(size)]

# Colors
bgColor = (5, 22, 26)
barColor = (109, 165, 192)
swapColor = (255,255, 255)

# Bubble Sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_array(arr, [j, j+1], swapColor)
                pygame.display.flip()
                pygame.time.wait(50)  


#draw the array on the screen
def draw_array(arr, swap_indices=None, color=barColor):
    screen.fill(bgColor)
    for i, height in enumerate(arr):
        rect = pygame.Rect(i * BarWidth, 750 - height, BarWidth, height)
        pygame.draw.rect(screen, color if swap_indices and i in swap_indices else barColor, rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.display.toggle_fullscreen()
    print("TEST")
    draw_array(array)
    print("TEST1")
    pygame.display.flip()
    print("TEST2")
    bubble_sort(array)
    print("TEST3")
    draw_array(array, color=swapColor)
    print("TEST4")
    pygame.display.flip()
    print("TEST5")
    pygame.time.wait(1000)
    print("TEST6")
    pygame.display.update()
    print("TEST7")
    clock.tick(250)


