import pygame

color = (5, 22, 26)
color1 = (109, 165, 192)
color2 = (189, 243, 255)
fontPath1 = 'MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf'
fontpath2 = 'MAIN/Assets/fonts/RobotoMono-Italic-VariableFont_wght.ttf'
fontpath3 = 'MAIN/Assets/fonts/Poppins-BoldItalic.ttf'

# Create a surface to hold all the elements
surface = pygame.Surface((1200, 750))

# heading
fontHead = pygame.font.Font(fontPath1, 45)
heading = fontHead.render("Quick Sort", True, color1)

# opening paragraph
text1 = "QuickSort is a fast and efficient sorting algorithm that follows the divide & conquer approach"
text2 = "QuickSort's average time complexity is O(nlogn), making it efficient for large datasets."
text3 = "QuickSort's worst-case time complexity is O(n^2) with unbalanced partitions."
textFont = pygame.font.Font(fontpath2, 20)
text1surface = textFont.render(text1, True, color1)
text2surface = textFont.render(text2, True, color1)
text3surface = textFont.render(text3, True, color1)

# subheading
subheading = "Quick Sort Algorithm"
subheadfont = pygame.font.Font(fontPath1, 25)
subheadSurface = subheadfont.render(subheading, True, color1)

# rectangle text
rec1 = "In Quick Sort algorithm :"
rec2 = "• Partition: Choose a pivot element and partition the array into two sub-arrays,"
rec21 = "  placing elements less than pivot left, others right."
rec3 = "• Recursion: Recursively apply the partitioning step to the sub-arrays."
rec4 = "• Combine: No combining step is needed as the sorting is done in-place."
rec41 = "• Base Case: The recursion ends when the sub-array has zero or one element"
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