import pygame
from ..setting import *
from .shop import *
from ..renderer import *
from src.auth_server.service.store_reader import email_reader

menu_bg = load_background("assets/sprites/menu.png")
menu_bg = pygame.transform.scale(menu_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

email = email_reader().split('@')[0]

def get_email():
    return email

def email_scan():
    global email
    def email_change():
        global email
        email = email_reader().split('@')[0]

    import time
    import threading
    while True:
        try:
            email_change()
        except:
            pass
        time.sleep(3)

def show_menu(screen):
    import threading
    threading.Thread(target=email_scan).start()

    while True:
        draw_background(screen, menu_bg)
        #screen.fill(WHITE)
        draw_text(screen, "Zombie Smasher", WINDOW_WIDTH // 2 - 125, 50, 48, GRAY)
        draw_text(screen, "Hello", WINDOW_WIDTH // 2 - 125, 85, 25, WHITE)
        draw_text(screen, f"{get_email()}", WINDOW_WIDTH // 2 - 75, 85, 25, YELLOW)
        start_button = draw_button(screen, "Start Game", WINDOW_WIDTH // 2 -125, 150, 200, 50, GREEN, DARK_GREEN)
        shop_button = draw_button(screen, "Shop", WINDOW_WIDTH // 2 - 125, 250, 200, 50, BLUE, DARK_BLUE)
        leaderboard_button = draw_button(screen, "Ranks", WINDOW_WIDTH // 2 - 125, 350, 200, 50, YELLOW, DARK_GRAY)
        exit_button = draw_button(screen, "Exit Game", WINDOW_WIDTH // 2 - 125, 450, 200, 50, RED, DARK_RED)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "start"
                elif shop_button.collidepoint(event.pos):
                    return "shop"
                elif leaderboard_button.collidepoint(event.pos):
                    return "rank"
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                
                    exit()


def show_difficulty_menu(screen):
    font_size = 48
    options = [
        ("Easy (3x3)", 3),
        ("Medium (4x4)", 4),
        ("Hard (5x5)", 5),
    ]

    selected_difficulty = None
    waiting_for_release = True

    while selected_difficulty is None:
        #screen.fill(WHITE)
        draw_background(screen, menu_bg)
        draw_text(screen, "Select Difficulty", WINDOW_WIDTH // 2 - 125, 100, font_size, LIGHT_GRAY)

        mouse_pos = pygame.mouse.get_pos()
        buttons = []
        
        for i, (text, difficulty) in enumerate(options):
            x = WINDOW_WIDTH // 2 - 125
            y = 200 + i * 80
            button = draw_button(screen, text, x, y, 250, 60, LIGHT_GRAY, DARK_GRAY, BLACK)
            buttons.append((button, difficulty))

        back_button = draw_button(screen, "Back to Menu", WINDOW_WIDTH // 2 - 125, 450, 250, 60, RED, DARK_RED)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                waiting_for_release = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not waiting_for_release:
                for button, difficulty in buttons:
                    if button.collidepoint(event.pos):
                        pygame.time.delay(300)
                        selected_difficulty = difficulty
                if back_button.collidepoint(event.pos):
                    pygame.time.delay(300)
                    return "back"

    return selected_difficulty
