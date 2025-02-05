import pygame
from setting import *

def load_background(image_path):
    return pygame.image.load(image_path)

def draw_background(screen, background):
    screen.blit(background, (0, 0))

def draw_text(screen, text, x, y, font_size=36, color=BLACK):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_button(screen, text, x, y, width, height, color, hover_color):
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)

    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, hover_color, button_rect, border_radius=10)
    else:
        pygame.draw.rect(screen, color, button_rect, border_radius=10)

    draw_text(screen, text, x + 20, y + 10, 36, WHITE)
    return button_rect

def draw_ui(screen, gun, score, combo):
    pygame.draw.rect(screen, GRAY, (0, 0, 800, 50)) 
    draw_text(screen, f"Score: {score}", 20, 10, 30, BLACK)
    draw_text(screen, f"Bullets: {gun.bullets}", 300, 10, 30, BLACK)
    draw_text(screen, f"Combo: {combo}", 600, 10, 30, BLACK)
