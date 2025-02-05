import pygame
from ..setting import *

def show_game_over(screen, score):
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 72)
    text = font.render(f"Game Over! Score: {score}", True, BLACK)
    screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, 200))
    pygame.display.flip()
    pygame.time.wait(3000)
