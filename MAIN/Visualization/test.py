import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('Menu page')

font = pygame.font.Font('sort-search-algorithm-visualizer/MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf', 30)
font1 = pygame.font.Font('sort-search-algorithm-visualizer/MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf', 29)
font3 = pygame.font.Font('sort-search-algorithm-visualizer/MAIN/Assets/fonts/RobotoMono-Italic-VariableFont_wght.ttf', 20)

# Welcome Animation
welcome_text = "Welcome to Algorithm Visualizer"
welcome_color = (109, 165, 192)
welcome_surface = font.render("", True, welcome_color)
welcome_pos = (20, 20)

intro_text = [
    "This is an interactive app designed to bring algorithms to life through visualization. Whether",
    "you're a student, teacher, or professional, our app provides an engaging way to explore and",
    "understand various algorithms."
]

intro_color = (109, 165, 192)
intro_surfaces = [font3.render(line, True, intro_color) for line in intro_text]
intro_pos = [(20, 70 + i * 25) for i in range(len(intro_text))]

heading_text = "Sorting Algorithms"
heading_color = (109, 165, 192)
heading_surface = font.render(heading_text, True, heading_color)
heading_pos = (20, 160)

text1_text = "BUBBLE SORT"
text1_color = 'black'
text1_surface = font.render(text1_text, True, text1_color)
text1_pos = (38, 280)

text2_text = "INSERTION SORT"
text2_color = 'black'
text2_surface = font1.render(text2_text, True, text2_color)
text2_pos = (305, 280)

text3_text = "SELECTION SORT"
text3_color = 'black'
text3_surface = font1.render(text3_text, True, text3_color)
text3_pos = (579, 280)

button_color1, button_color2, button_color3 = (15, 150, 156), (15, 150, 156), (15, 150, 156)
button1 = pygame.Rect(20, 220, 250, 150)
button2 = pygame.Rect(300, 220, 250, 150)
button3 = pygame.Rect(580, 220, 250, 150)
clock = pygame.time.Clock()

welcome_animation_speed = 30
intro_animation_speed = 15
current_intro_line = 0
intro_timer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                screen = pygame.display.set_mode((1200, 750))

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button1.collidepoint(event.pos):
                    print("button clicked")

        if button1.collidepoint(pygame.mouse.get_pos()):
            button_color1 = (7, 46, 51)
        else:
            button_color1 = (15, 150, 156)

        if button2.collidepoint(pygame.mouse.get_pos()):
            button_color2 = (7, 46, 51)
        else:
            button_color2 = (15, 150, 156)

        if button3.collidepoint(pygame.mouse.get_pos()):
            button_color3 = (7, 46, 51)
        else:
            button_color3 = (15, 150, 156)

        # Update Welcome Animation
        if welcome_surface.get_width() < font.size(welcome_text)[0]:
            welcome_surface = font.render(welcome_text[:welcome_surface.get_width() // 10 + 1], True, welcome_color)

        # Update Intro Animation
        if current_intro_line < len(intro_text):
            intro_timer += 1
            if intro_timer >= intro_animation_speed:
                intro_timer = 0
                intro_surface = intro_surfaces[current_intro_line]
                current_intro_line += 1

        screen.fill((5, 22, 26))
        screen.blit(welcome_surface, welcome_pos)

        for i, line_pos in enumerate(intro_pos[:current_intro_line]):
            screen.blit(intro_surface, line_pos)

        screen.blit(heading_surface, heading_pos)
        pygame.draw.rect(screen, button_color1, button1)
        pygame.draw.rect(screen, button_color2, button2)
        pygame.draw.rect(screen, button_color3, button3)
        screen.blit(text1_surface, text1_pos)
        screen.blit(text2_surface, text2_pos)
        screen.blit(text3_surface, text3_pos)
        pygame.display.flip()
        clock.tick(60)
