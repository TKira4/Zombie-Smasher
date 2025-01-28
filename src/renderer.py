import pygame
from setting import *

def draw_ui(screen, gun, score, combo):
    font = pygame.font.SysFont(None, 36)
    
    bullet_text = font.render(f"Bullets: {gun.bullets}", True, BLACK)
    score_text = font.render(f"Score: {score}", True, BLACK)
    combo_text = font.render(f"Combo: {combo}", True, BLACK)

    screen.blit(bullet_text, (10, 10))
    screen.blit(score_text, (10, 50))
    screen.blit(combo_text, (10, 90))
