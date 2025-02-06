import pygame
from ..setting import *

def show_loading_screen(screen, message="Loading..."):
    font = pygame.font.Font(None, 50)
    clock = pygame.time.Clock()

    loading_dots = 0  
    running = True
    while running:
        screen.fill(BLACK)
        
        text = font.render(message + "." * (loading_dots % 4), True, WHITE)
        screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
        
        pygame.display.update()
        pygame.time.delay(500)  
        loading_dots += 1
        
        if loading_dots >= 4:  
            running = False
        
        clock.tick(10)
