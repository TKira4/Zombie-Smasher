import pygame
from setting import *

def show_menu(screen):
    font = pygame.font.SysFont(None, 48)
    options = [
        ("Easy (3x3)", 3),
        ("Medium (5x5)", 5),
        ("Hard (7x7)", 7),
    ]
    
    while True:
        screen.fill(WHITE)
        title_text = font.render("Zombie Smasher", True, BLACK)
        screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 100))

        #chon do kho bang chuot
        mouse_pos = pygame.mouse.get_pos()
        for i, (text, difficulty) in enumerate(options):
            render = font.render(text, True, BLACK)
            x = WINDOW_WIDTH // 2 - render.get_width() // 2
            y = 200 + i * 50
            screen.blit(render, (x, y))

            if pygame.Rect(x, y, render.get_width(), render.get_height()).collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:  
                    return difficulty

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()