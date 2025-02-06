import pygame
from ..renderer import *
from ..setting import *

game_over_bg = load_background("assets/sprites/game_over.png")
game_over_bg = pygame.transform.scale(game_over_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
def show_game_over(screen, score, max_combo, miss_hit):
    #screen.fill(WHITE)
    draw_background(screen, game_over_bg)
    draw_text(screen, f"Score: {score}", 50, 50, 36, WHITE)
    draw_text(screen, f"Max_combo: {max_combo}", 250, 50, 36, RED)
    draw_text(screen, f"Miss_hit: {miss_hit}", 550, 50, 36, YELLOW)
    pygame.display.flip()
    pygame.time.wait(3000)
