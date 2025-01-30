import pygame
from setting import *

def show_shop(screen):
    font = pygame.font.SysFont(None, 48)
    back_text = font.render("Back", True, BLACK)
    back_rect = back_text.get_rect(center=(WINDOW_WIDTH // 2, 400))

    while True:
        screen.fill(WHITE)
        title_text = font.render("Shop", True, BLACK)
        screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 100))
        screen.blit(back_text, back_rect.topleft)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    return  
