import pygame


surface = pygame.Surface((1200, 750))
surface.fill((5, 22, 26))
color = (5, 22, 26)
color1 = (109, 165, 192)
color2 = (189, 243, 255)
fontPath1 = 'Assets/fonts/static/RobotoMono-SemiBold.ttf'
fontpath2 = 'Assets/fonts/RobotoMono-Italic-VariableFont_wght.ttf'
fontpath3 = 'Assets/fonts/Poppins-BoldItalic.ttf'

# heading
fontHead = pygame.font.Font(fontPath1, 45)
heading = fontHead.render("Bubble Sort", True, color1)

# opening paragraph
text1 = "Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent"
text2 = "elements if they are in the wrong order.This algorithm is not suitable for large data sets as"
text3 = "its average and worst-case time complexity is quite high."
textFont = pygame.font.Font(fontpath2, 20)
text1surface = textFont.render(text1, True, color1)
text2surface = textFont.render(text2, True, color1)
text3surface = textFont.render(text3, True, color1)

# subheading
subheading = "Bubble Sort Algorithm"
subheadfont = pygame.font.Font(fontPath1, 25)
subheadSurface = subheadfont.render(subheading, True, color1)

# rectangle text
rec1 = "In Bubble Sort algorithm :"
rec2 = "• Traverse from left and compare adjacent elements and the higher one is placed"
rec21 = "  at right side."
rec3 = "• In this way, the largest element is moved to the rightmost end at first. "
rec4 = "• This process is then continued to find the second largest and place it and "
rec41 = "  so on until the data is sorted."
recFont = pygame.font.Font(fontpath2, 22)
rec1surface = recFont.render(rec1, True, color)
rec2surface = recFont.render(rec2, True, color)
rec21surface = recFont.render(rec21, True, color)
rec3surface = recFont.render(rec3, True, color)
rec4surface = recFont.render(rec4, True, color)
rec41surface = recFont.render(rec41, True, color)

#button to visualize
button_color1 = (15,150,156)
text = subheadfont.render("Press space to visualize this algo!", True, 'black')
button1 = pygame.Rect(350, 600, 540, 90)

surface.fill(color)
# heading
surface.blit(heading, (40, 40 ))
# opening paragraph
surface.blit(text1surface, (40, 120 ))
surface.blit(text2surface, (40, 150 ))
surface.blit(text3surface, (40, 180 ))
# subheading
surface.blit(subheadSurface, (40, 240 ))
# rectangle
pygame.draw.rect(surface, color2, (40, 300 , 1120, 240))
# text on rectangle
surface.blit(rec1surface, (65, 320 ))
surface.blit(rec2surface, (65, 365 ))
surface.blit(rec21surface, (65, 395 ))
surface.blit(rec3surface, (65, 425 ))
surface.blit(rec4surface, (65, 455 ))
surface.blit(rec41surface, (65, 485 ))

pygame.draw.rect(surface, button_color1, button1)
surface.blit(text, (360, 620))


