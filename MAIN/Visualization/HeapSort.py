import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200, 750))
clock = pygame.time.Clock()
pygame.display.set_caption("Heap sort")
color = (5, 22, 26)
color1 = (109, 165, 192)
color2 = (189, 243, 255)
fontPath1 = 'MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf'
fontpath2 = 'MAIN/Assets/fonts/RobotoMono-Italic-VariableFont_wght.ttf'
fontpath3 = 'MAIN/Assets/fonts/Poppins-BoldItalic.ttf'

# heading
fontHead = pygame.font.Font(fontPath1, 45)
heading = fontHead.render("Heap Sort", True, color1)

# opening paragraph
text1 = "Heap sort is a comparison-based sorting algorithm that operates by first building a heap from"
text2 = "the elements and then repeatedly extracting the maximum  or minimum element from the heap and"
text3 = "rebuilding the heap until the array is sorted."
textFont = pygame.font.Font(fontpath2, 20)
text1surface = textFont.render(text1, True, color1)
text2surface = textFont.render(text2, True, color1)
text3surface = textFont.render(text3, True, color1)

# subheading
subheading = "Heap Sort Algorithm"
subheadfont = pygame.font.Font(fontPath1, 25)
subheadSurface = subheadfont.render(subheading, True, color1)

# rectangle text
rec1 = "In Heap Sort algorithm :"
rec2 = "• Heapify: Convert array into a max/min heap. Arrange elements ensuring parent"
rec21 = "  is greater than or equal to children."
rec3 = "• Extract: Repeatedly remove root and rebuild heap"
rec4 = "• Repeat: Until all elements are extracted.The last remaining heap will be in " 
rec41 = "  the form of a max heap,."
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
                    import visualize

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