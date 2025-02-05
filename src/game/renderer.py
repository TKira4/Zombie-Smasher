import pygame
from .setting import *

def load_background(image_path):
    return pygame.image.load(image_path)

def draw_background(screen, background):
    screen.blit(background, (0, 0))

def draw_text(screen, text, x, y, font_size=36, color=BLACK):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_button(screen, text, x, y, width, height, color, hover_color, text_color=WHITE):
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)

    current_color = hover_color if button_rect.collidepoint(mouse_pos) else color
    pygame.draw.rect(screen, current_color, button_rect, border_radius=10)

    pygame.draw.rect(screen, BLACK, button_rect, 3, border_radius=10)

    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    return button_rect

def draw_ui(screen, gun, score, combo):
    pygame.draw.rect(screen, GRAY, (0, 0, 800, 50)) 
    draw_text(screen, f"Score: {score}", 20, 10, 30, BLACK)
    draw_text(screen, f"Bullets: {gun.bullets}", 300, 10, 30, BLACK)
    draw_text(screen, f"Combo: {combo}", 600, 10, 30, BLACK)
