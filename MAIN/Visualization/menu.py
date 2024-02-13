import pygame
import subprocess
from sys import exit

pygame.init()
width, height = 1200, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Menu page')


## [ Constants ]

scrollable_height = 1000
scroll_speed = 30
scroll_y = 0
surface = pygame.Surface((width, scrollable_height))
font = pygame.font.Font('MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf', 30)
font1 = pygame.font.Font('MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf', 29)
font3 = pygame.font.Font('MAIN/Assets/fonts/RobotoMono-Italic-VariableFont_wght.ttf', 20)
button_color1, button_color2, button_color3 = (15, 150, 156), (15, 150, 156), (15, 150, 156)
button_color4, button_color5, button_color6, button_color7 = (15, 150, 156), (15, 150, 156), (15, 150, 156), (15, 150, 156)
button_color8, button_color9, button_color10, button_color11 = (15, 150, 156), (15, 150, 156), (15, 150, 156), (15, 150, 156)

states = {'bscheck':False, 'ischeck':False, 'sscheck':False, 'hscheck':False, 'mscheck':False, 'qscheck':False, 'rscheck':False, 'lscheck':False, 'bincheck':False, 'bfscheck':False, 'dfscheck':False}

## [ Statics ]

text = font.render("Welcome to Algorithm Visualizer", True, (109, 165, 192))
intro = font3.render("This is an interactive app designed to bring algorithms to life through visualization. Whether", True, (109, 165, 192))
intro1 = font3.render("you're a student, teacher, or professional, our app provides an engaging way to explore and", True, (109, 165, 192))
intro2 = font3.render("understand various algorithms.", True, (109, 165, 192))
heading = font.render("Sorting Algorithms", True, (109, 165, 192))
text1 = font.render("BUBBLE SORT", True, 'black')
text2 = font1.render("INSERTION SORT", True, 'black')
text3 = font1.render("SELECTION SORT", True, 'black')
text4 = font.render("HEAP SORT", True, 'black')
text5 = font.render("MERGE SORT", True, 'black')
text6 = font.render("QUICK SORT", True, 'black')
text7 = font.render("RADIX SORT", True, 'black')
heading2 = font.render("Searching Algorithms", True, (109, 165, 192))
text8 = font1.render("LINEAR SEARCH", True, 'black')
text9 = font1.render("BINARY SEARCH", True, 'black')
text10 = font1.render("BFS", True, 'black')
text11 = font1.render("DFS", True, 'black')


## [ Functions ]

def main_surface_draw():
    surface.fill((5, 22, 26))  # Fill with background color
    surface.blit(text, (20, 50 + scroll_y))
    surface.blit(intro, (20, 120 + scroll_y))
    surface.blit(intro1, (20, 145 + scroll_y))
    surface.blit(intro2, (20, 173 + scroll_y))
    surface.blit(heading, (20, 230 + scroll_y))
    pygame.draw.rect(surface, button_color1, button1)
    pygame.draw.rect(surface, button_color2, button2)
    pygame.draw.rect(surface, button_color3, button3)
    pygame.draw.rect(surface, button_color4, button4)
    pygame.draw.rect(surface, button_color5, button5)
    pygame.draw.rect(surface, button_color6, button6)
    pygame.draw.rect(surface, button_color7, button7)
    pygame.draw.rect(surface, button_color8, button8)
    pygame.draw.rect(surface, button_color9, button9)
    pygame.draw.rect(surface, button_color10, button10)
    pygame.draw.rect(surface, button_color11, button11)
    surface.blit(text1, (60, 365 + scroll_y))
    surface.blit(text2, (325, 365 + scroll_y))
    surface.blit(text3, (615, 365 + scroll_y))
    surface.blit(text4, (943, 365 + scroll_y))
    surface.blit(text5, (68, 565 + scroll_y))
    surface.blit(text6, (352, 565 + scroll_y))
    surface.blit(text7, (645, 565 + scroll_y))
    surface.blit(heading2, (20, 720 + scroll_y))
    surface.blit(text8, (49, 855 + scroll_y))
    surface.blit(text9, (335, 855 + scroll_y))
    surface.blit(text10, (705, 855 + scroll_y))
    surface.blit(text11, (1000, 855 + scroll_y))
    screen.blit(surface, (0, 0))



## [ MainLoop ]

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                screen = pygame.display.set_mode((1200, 750))

            if event.key == pygame.K_ESCAPE:
                for i in states:
                    states[i] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if scroll_y < 0:
                    scroll_y += scroll_speed
            elif event.button == 5:
                if scroll_y > -(scrollable_height - height):
                    scroll_y -= scroll_speed

            if event.button == 1:
                if button1.collidepoint(event.pos):
                    states['bscheck'] = True
                    import BubbleSortV
                    screen.blit(BubbleSortV.surface,(0,0))

            if event.button == 1:
                if button2.collidepoint(event.pos):
                    states['ischeck'] = True
                    import InsertionSort
                    screen.blit(InsertionSort.surface,(0,0))
            
            if event.button == 1:
                if button3.collidepoint(event.pos):
                    states['sscheck'] = True
                    import SelectionSort
                    screen.blit(SelectionSort.surface,(0,0))
            
            if event.button == 1:
                if button4.collidepoint(event.pos):
                    states['hscheck'] = True
                    import HeapSort
                    screen.blit(HeapSort.surface,(0,0))
            
            if event.button == 1:
                if button5.collidepoint(event.pos):
                    states['mscheck'] = True
                    import MergeSort
                    screen.blit(MergeSort.surface,(0,0))
            
            if event.button == 1:
                if button6.collidepoint(event.pos):
                    states['qscheck'] = True
                    import QuickSort
                    screen.blit(QuickSort.surface,(0,0))
            
            if event.button == 1:
                if button7.collidepoint(event.pos):
                    states['rscheck'] = True
                    import RadixSort
                    screen.blit(RadixSort.surface,(0,0))
            
            if event.button == 1:
                if button8.collidepoint(event.pos):
                    states['lscheck'] = True
                    import LinearSearch
                    screen.blit(LinearSearch.surface,(0,0))
            
            if event.button == 1:
                if button9.collidepoint(event.pos):
                    states['bincheck'] = True
                    import BinarySearch
                    screen.blit(BinarySearch.surface,(0,0))
            
            if event.button == 1:
                if button10.collidepoint(event.pos):
                    states['bfscheck'] = True
                    import BFS
                    screen.blit(BFS.surface,(0,0))
            
            if event.button == 1:
                if button11.collidepoint(event.pos):
                    states['dfscheck'] = True
                    import DFS
                    screen.blit(DFS.surface,(0,0))
        
        if states['bscheck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Bubble_visualize.py"])

        if states['ischeck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Insertion_visualize.py"])

        if states['sscheck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Selection_visualize.py"])
        
        if states['hscheck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Selection_visualize.py"])
        
        if states['mscheck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Selection_visualize.py"])
        
        if states['qscheck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Selection_visualize.py"])
        
        if states['rscheck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Selection_visualize.py"])
        
        if states['lscheck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Selection_visualize.py"])
        
        if states['bincheck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Selection_visualize.py"])
        
        if states['bfscheck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Selection_visualize.py"])
        
        if states['dfscheck'] == True :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    subprocess.Popen(["python", "MAIN/Visualization/Selection_visualize.py"])
            

        button1 = pygame.Rect(35, 310 + scroll_y, 250, 150)
        button2 = pygame.Rect(320, 310 + scroll_y, 250, 150)
        button3 = pygame.Rect(610, 310 + scroll_y, 250, 150)
        button4 = pygame.Rect(900, 310 + scroll_y, 250, 150)
        button5 = pygame.Rect(35, 510 + scroll_y, 250, 150)
        button6 = pygame.Rect(320, 510 + scroll_y, 250, 150)
        button7 = pygame.Rect(610, 510 + scroll_y, 250, 150)
        button8 = pygame.Rect(35, 800 + scroll_y, 250, 150)
        button9 = pygame.Rect(320, 800 + scroll_y, 250, 150)
        button10 = pygame.Rect(610, 800 + scroll_y, 250, 150)
        button11 = pygame.Rect(900, 800 + scroll_y, 250, 150)

        if button1.collidepoint(pygame.mouse.get_pos()):
            button_color1 = (7, 46, 51)
            text1 = font.render("BUBBLE SORT", True, 'white')
        else:
            button_color1 = (15, 150, 156)
            text1 = font.render("BUBBLE SORT", True, 'black')

        if button2.collidepoint(pygame.mouse.get_pos()):
            button_color2 = (7, 46, 51)
            text2 = font1.render("INSERTION SORT", True, 'white')
        else:
            button_color2 = (15, 150, 156)
            text2 = font1.render("INSERTION SORT", True, 'black')

        if button3.collidepoint(pygame.mouse.get_pos()):
            button_color3 = (7, 46, 51)
            text3 = font1.render("SELECTION SORT", True, 'white')
        else:
            button_color3 = (15, 150, 156)
            text3 = font1.render("SELECTION SORT", True, 'black')

        if button4.collidepoint(pygame.mouse.get_pos()):
            button_color4 = (7, 46, 51)
            text4 = font.render("HEAP SORT", True, 'white')
        else:
            button_color4 = (15, 150, 156)
            text4 = font.render("HEAP SORT", True, 'black')

        if button5.collidepoint(pygame.mouse.get_pos()):
            button_color5 = (7, 46, 51)
            text5 = font.render("MERGE SORT", True, 'white')
        else:
            button_color5 = (15, 150, 156)
            text5 = font.render("MERGE SORT", True, 'black')

        if button6.collidepoint(pygame.mouse.get_pos()):
            button_color6 = (7, 46, 51)
            text6 = font.render("QUICK SORT", True, 'white')
        else:
            button_color6 = (15, 150, 156)
            text6 = font.render("QUICK SORT", True, 'black')

        if button7.collidepoint(pygame.mouse.get_pos()):
            button_color7 = (7, 46, 51)
            text7 = font.render("RADIX SORT", True, 'white')
        else:
            button_color7 = (15, 150, 156)
            text7 = font.render("RADIX SORT", True, 'black')

        if button8.collidepoint(pygame.mouse.get_pos()):
            button_color8 = (7, 46, 51)
            text8 = font1.render("LINEAR SEARCH", True, 'white')
        else:
            button_color8 = (15, 150, 156)
            text8 = font1.render("LINEAR SEARCH", True, 'black')

        if button9.collidepoint(pygame.mouse.get_pos()):
            button_color9 = (7, 46, 51)
            text9 = font1.render("BINARY SEARCH", True, 'white')
        else:
            button_color9 = (15, 150, 156)
            text9 = font1.render("BINARY SEARCH", True, 'black')

        if button10.collidepoint(pygame.mouse.get_pos()):
            button_color10 = (7, 46, 51)
            text10 = font1.render("BFS", True, 'white')
        else:
            button_color10 = (15, 150, 156)
            text10 = font1.render("BFS", True, 'black')

        if button11.collidepoint(pygame.mouse.get_pos()):
            button_color11 = (7, 46, 51)
            text11 = font1.render("DFS", True, 'white')
        else:
            button_color11 = (15, 150, 156)
            text11 = font1.render("DFS", True, 'black')

        # Clear the surface
        surfcheck = False
        for i in states:
            if states[i] == True:
                surfcheck = True
        if surfcheck == False:
            main_surface_draw()
        pygame.display.flip()
        clock.tick(200)
