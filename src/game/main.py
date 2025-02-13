import pygame
import sys
from .setting import *
from .game_objects.im import *
from .logic.im import *
from .screen.im import *
from .renderer import *

# Khởi tạo pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Smasher")

try:
    running = True
    game_state = "menu"
    difficulty = None  

    while running:
        if game_state == "menu":
            pygame.mouse.set_visible(True)
            selected_action = show_menu(screen)

            if selected_action == "start":
                difficulty = show_difficulty_menu(screen)
                if difficulty == "back":
                    game_state = "menu"
                else:
                    #pygame.time.delay(1000)
                    show_loading_screen(screen)
                    game_state = "playing"
            elif selected_action == "shop":
                show_shop(screen)  
            elif selected_action == "rank":
                show_leaderboard(screen)
            elif selected_action == "exit":
                running = False  

        elif game_state == "playing":
            #screen.fill(WHITE)  #xoa man hinh truoc khi ve
            #draw_background(screen, game_bg)
            score, max_combo, miss_hit = start_game(screen, difficulty)
            show_jumpscare(screen)
            insert_point_to_table(score)
            game_state = "game_over"
    
        elif game_state == "game_over":
            selected = show_game_over(screen, score, max_combo, miss_hit)
            if selected == "menu":
                game_state = "menu"
            elif selected == "playing":
                game_state = "playing"

    pygame.quit()
    # sys.exit()

except Exception as e:
    print(str(e))
    pass
