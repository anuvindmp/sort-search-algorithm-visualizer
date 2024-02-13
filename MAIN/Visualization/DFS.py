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
heading = fontHead.render("DFS", True, color1)

# opening paragraph
text1 = "Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible "
text2 = "along each branch before backtracking"
text3 = "• Time complexity: O(V + E)"
textFont = pygame.font.Font(fontpath2, 20)
text1surface = textFont.render(text1, True, color1)
text2surface = textFont.render(text2, True, color1)
text3surface = textFont.render(text3, True, color1)

# subheading
subheading = "DFS Algorithm"
subheadfont = pygame.font.Font(fontPath1, 25)
subheadSurface = subheadfont.render(subheading, True, color1)

# rectangle text
rec1 = "In DFS algorithm :"
rec2 = "• Start with a stack or recursion, push the starting vertex onto it, and mark it as visited"
rec21 = "• While the stack is not empty : "
rec3 = "    1. Pop a vertex."
rec4 = "    2. Visit it if unvisited."
rec41 = "    3. Push unvisited adjacent vertices onto the stack.Mark the vertex as visited"
recFont = pygame.font.Font(fontpath2, 22)
rec1surface = recFont.render(rec1, True, color)
rec2surface = recFont.render(rec2, True, color)
rec21surface = recFont.render(rec21, True, color)
rec3surface = recFont.render(rec3, True, color)
rec4surface = recFont.render(rec4, True, color)
rec41surface = recFont.render(rec41, True, color)

# button to visualize
button_color1 = (15, 150, 156)
text = subheadfont.render("Click to see this algo in action!", True, 'black')
button1 = pygame.Rect(350, 600, 520, 90)

# Blit all the elements onto the surface
surface.fill(color)
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