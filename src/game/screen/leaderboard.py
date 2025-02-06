import pygame
from ..setting import *
from ..logic.data import rankings
from ..renderer import *

leaderboard_bg = load_background("assets/sprites/leaderboard.png")
leaderboard_bg = pygame.transform.scale(leaderboard_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

def show_leaderboard(screen):
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 36)

    leaderboard = rankings()  #top 10
    back_button = pygame.Rect(50, 50, 100, 50)

    running = True
    while running:
        draw_background(screen, leaderboard_bg)
        
        title_text = font.render("Leaderboard", True, WHITE)
        screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 50))

        for i, (name, score) in enumerate(leaderboard):
            entry_text = small_font.render(f"{i+1}. {name}: {score}", True, YELLOW)
            screen.blit(entry_text, (WINDOW_WIDTH // 2 - entry_text.get_width() // 2, 150 + i * 40))

        back_button = draw_button(screen, "Back", 50, 50, 120, 50, RED, DARK_RED)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False  

        clock.tick(FPS)
