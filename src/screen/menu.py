import pygame
from setting import *
from screen.shop import *
from renderer import *

menu_bg = load_background("assets/sprites/menu.png")
#menu_bg = pygame.transform.scale(menu_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

def show_menu(screen):
    while True:
        #draw_background(screen, menu_bg)
        screen.fill(WHITE)
        draw_text(screen, "Zombie Smasher", WINDOW_WIDTH // 2 - 100, 50, 48, GRAY)

        start_button = draw_button(screen, "Start Game", 250, 150, 200, 50, GREEN, DARK_GREEN)
        shop_button = draw_button(screen, "Shop", 250, 250, 200, 50, BLUE, DARK_BLUE)
        exit_button = draw_button(screen, "Exit Game", 250, 350, 200, 50, RED, DARK_RED)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "start"
                if shop_button.collidepoint(event.pos):
                    return "shop"
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()


def show_difficulty_menu(screen):
    font = pygame.font.SysFont(None, 48)
    options = [
        ("Easy (3x3)", 3),
        ("Medium (5x5)", 5),
        ("Hard (7x7)", 7),
    ]
    
    selected_difficulty = None  
    waiting_for_release = True
    
    while selected_difficulty is None:  
        screen.fill(WHITE)
        title_text = font.render("Select Difficulty", True, BLACK)
        screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 100))

        mouse_pos = pygame.mouse.get_pos()
        for i, (text, difficulty) in enumerate(options):
            render = font.render(text, True, BLACK)
            x = WINDOW_WIDTH // 2 - render.get_width() // 2 #here
            y = 200 + i * 50
            screen.blit(render, (x, y))

            if pygame.Rect(x, y, render.get_width(), render.get_height()).collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] and not waiting_for_release:  
                    pygame.time.delay(1000)  
                    selected_difficulty = difficulty  

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                waiting_for_release = False

    return selected_difficulty  
