import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200, 750))
clock = pygame.time.Clock()
pygame.display.set_caption("Merge sort")
color = (5, 22, 26)
color1 = (109, 165, 192)
color2 = (189, 243, 255)
fontPath1 = 'MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf'
fontpath2 = 'MAIN/Assets/fonts/RobotoMono-Italic-VariableFont_wght.ttf'
fontpath3 = 'MAIN/Assets/fonts/Poppins-BoldItalic.ttf'

# heading
fontHead = pygame.font.Font(fontPath1, 45)
heading = fontHead.render("Merge Sort", True, color1)

# opening paragraph
text1 = "Merge sort is a popular and efficient comparison-based sorting algorithm that divides the"
text2 = "input array into two halves, sorts each half recursively, and then merges the sorted halves"
text3 = "to produce a single sorted array"
textFont = pygame.font.Font(fontpath2, 20)
text1surface = textFont.render(text1, True, color1)
text2surface = textFont.render(text2, True, color1)
text3surface = textFont.render(text3, True, color1)

# subheading
subheading = "Merge Sort Algorithm"
subheadfont = pygame.font.Font(fontPath1, 25)
subheadSurface = subheadfont.render(subheading, True, color1)

# rectangle text
rec1 = "In Merge Sort algorithm :"
rec2 = "• Divide: Split the array into two halves recursively until each sub-array contains "
rec21 = "  only one element."
rec3 = "• Conquer (Sort): Merge adjacent sub-arrays while sorting them."
rec4 = "• Merge: Compare and merge two sub-arrays into one sorted sub-array."
rec41 = "• Combine: After all sub-arrays are merged, the array is fully sorted."
recFont = pygame.font.Font(fontpath2, 22)
rec1surface = recFont.render(rec1, True, color)
rec2surface = recFont.render(rec2, True, color)
rec21surface = recFont.render(rec21, True, color)
rec3surface = recFont.render(rec3, True, color)
rec4surface = recFont.render(rec4, True, color)
rec41surface = recFont.render(rec41, True, color)

#button to visualize
button_color1 = (15,150,156)
text = subheadfont.render("Click to see this algo in action!", True, 'black')
button1 = pygame.Rect(350, 600, 520, 90)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                screen = pygame.display.set_mode((1200,750))

        if button1.collidepoint(pygame.mouse.get_pos()):
            button_color1 = (7,46,51)
            text = subheadfont.render("Click to see this algo in action!", True, 'white')
        else:
            button_color1 = (15,150,156)
            text = subheadfont.render("Click to see this algo in action!", True, 'black')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button1.collidepoint(event.pos):
                    import MAIN.Visualization.Insertion_visualize as Insertion_visualize

    screen.fill(color)
    # heading
    screen.blit(heading, (40, 40 ))
    # opening paragraph
    screen.blit(text1surface, (40, 120 ))
    screen.blit(text2surface, (40, 150 ))
    screen.blit(text3surface, (40, 180 ))
    # subheading
    screen.blit(subheadSurface, (40, 240 ))
    # rectangle
    pygame.draw.rect(screen, color2, (40, 300 , 1120, 240))
    # text on rectangle
    screen.blit(rec1surface, (65, 320 ))
    screen.blit(rec2surface, (65, 365 ))
    screen.blit(rec21surface, (65, 395 ))
    screen.blit(rec3surface, (65, 425 ))
    screen.blit(rec4surface, (65, 455 ))
    screen.blit(rec41surface, (65, 485 ))

    pygame.draw.rect(screen, button_color1, button1)
    screen.blit(text, (360, 620))
    pygame.display.update()
    clock.tick(200)
