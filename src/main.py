import pygame
import sys
import random
import pygame.transform

from setting import *
from game_objects.im import *
from logic.im import *
from screen.im import *

#khoi tao pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Smasher")

def main():
    running = True
    game_state = "menu"
    difficulty = 3

    while running:
        if game_state == "menu":
            difficulty = show_menu(screen)
            game_state = "playing"

        elif game_state == "playing":
            score = start_game(screen, difficulty)
            game_state = "game_over"

        elif game_state == "game_over":
            show_game_over(screen, score)
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

