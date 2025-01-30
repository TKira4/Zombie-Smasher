import pygame
import sys

from setting import *
from game_objects.im import *
from logic.im import *
from screen.im import *

# Khởi tạo pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Smasher")

def main():
    try:
        running = True
        game_state = "menu"
        difficulty = None  

        while running:
            if game_state == "menu":
                selected_action = show_menu(screen)

                if selected_action == "start":
                    game_state = "select_difficulty"
                    difficulty = show_difficulty_menu(screen)
                    pygame.time.delay(1000)
                    game_state = "playing"
                elif selected_action == "shop":
                    show_shop(screen)  
                elif selected_action == "exit":
                    running = False  

            elif game_state == "playing":
                score = start_game(screen, difficulty)
                game_state = "game_over"
        
            elif game_state == "game_over":
                show_game_over(screen, score)
                game_state = "menu"  

        pygame.quit()
        sys.exit()

    except Exception as e:
        import time
        time.sleep(10)
        pass

if __name__ == "__main__":
    main()
