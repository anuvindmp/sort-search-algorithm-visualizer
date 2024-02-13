def Handler(event,states):
    import pygame
    from sys import exit
    scrollable_height = 1000
    scroll_speed = 30
    scroll_y = 0
    height = 750
    font = pygame.font.Font('MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf', 30)
    font1 = pygame.font.Font('MAIN/Assets/fonts/static/RobotoMono-SemiBold.ttf', 29)
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
        if event.button == 1:
            if button1.collidepoint(event.pos):
                states['bscheck'] = True
                import BubbleSortV
                screen.blit(BubbleSortV.surface,(0,0))
        
        if event.button == 1:
            if button2.collidepoint(event.pos):
                states['ischeck'] = True
                import InsertionSort
                screen.blit(BubbleSortV.surface,(0,0))

    
        if event.button == 4:
            if scroll_y < 0:
                scroll_y += scroll_speed
        elif event.button == 5:
            if scroll_y > -(scrollable_height - height):
                scroll_y -= scroll_speed

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

    return states, scroll_y, 