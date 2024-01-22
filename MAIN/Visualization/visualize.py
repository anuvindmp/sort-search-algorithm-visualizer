import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption("Bubble Sort Visualization")
clock = pygame.time.Clock()

# Constants
ARRAY_SIZE = 50
BAR_WIDTH = 1200 // ARRAY_SIZE
ARRAY = [random.randint(70, 750 - 50) for _ in range(ARRAY_SIZE)]

# Colors
BACKGROUND_COLOR = (5, 22, 26)
BAR_COLOR = (109, 165, 192)
SWAP_COLOR = (255,255, 255)

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
                draw_array(arr, [j, j+1], SWAP_COLOR)
                pygame.display.flip()
                pygame.time.wait(50)  


# Function to draw the array on the screen
def draw_array(arr, swap_indices=None, color=BAR_COLOR):
    screen.fill(BACKGROUND_COLOR)
    for i, height in enumerate(arr):
        rect = pygame.Rect(i * BAR_WIDTH, 750 - height, BAR_WIDTH, height)
        pygame.draw.rect(screen, color if swap_indices and i in swap_indices else BAR_COLOR, rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.display.toggle_fullscreen()
    print("TEST")
    draw_array(ARRAY)
    print("TEST1")
    pygame.display.flip()
    print("TEST2")
    # Run Bubble Sort algorithm
    bubble_sort(ARRAY)
    print("TEST3")
    # Draw the final state
    draw_array(ARRAY, color=SWAP_COLOR)
    print("TEST4")
    pygame.display.flip()
    print("TEST5")
    # Wait for a key press to exit
    pygame.time.wait(1000)
    print("TEST6")
    pygame.display.update()
    print("TEST7")
    clock.tick(250)


