import pygame

color = (5, 22, 26)
color1 = (109, 165, 192)
color2 = (189, 243, 255)
fontPath1 = 'Assets/fonts/static/RobotoMono-SemiBold.ttf'
fontpath2 = 'Assets/fonts/RobotoMono-Italic-VariableFont_wght.ttf'
fontpath3 = 'Assets/fonts/Poppins-BoldItalic.ttf'

# Create a surface to hold all the elements
surface = pygame.Surface((1200, 750))

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
text = subheadfont.render("Press space to visualize this algo!", True, 'black')
button1 = pygame.Rect(350, 600, 540, 90)

# Add all elements to the surface
surface.blit(heading, (40, 40))
surface.blit(text1surface, (40, 120))
surface.blit(text2surface, (40, 150))
surface.blit(text3surface, (40, 180))
surface.blit(subheadSurface, (40, 240))
pygame.draw.rect(surface, color2, (40, 300, 1120, 240))
surface.blit(rec1surface, (65, 320))
surface.blit(rec2surface, (65, 365))
surface.blit(rec21surface, (65, 395))
surface.blit(rec3surface, (65, 425))
surface.blit(rec4surface, (65, 455))
surface.blit(rec41surface, (65, 485))
pygame.draw.rect(surface, button_color1, button1)
surface.blit(text, (360, 620))