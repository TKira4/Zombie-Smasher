import pygame
from setting import *
from logic.data import *

def show_shop(screen):
    font = pygame.font.SysFont(None, 48)
    
    while True:
        screen.fill(WHITE)
        title_text = font.render("SHOP - UPGRADE GUN", True, BLACK)
        screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 50))

        score = get_score()
        gun_level = get_gun_level()  
        upgrade_cost = gun_level * 100

        score_text = font.render(f"Your Score: {score}", True, BLACK)
        level_text = font.render(f"Gun Level: {gun_level}", True, BLACK)
        upgrade_text = font.render(f"Upgrade Cost: {upgrade_cost} Points", True, BLACK)
        
        screen.blit(score_text, (100, 150))
        screen.blit(level_text, (100, 200))
        screen.blit(upgrade_text, (100, 250))

        upgrade_button = pygame.Rect(100, 300, 200, 50)
        pygame.draw.rect(screen, GREEN, upgrade_button)
        button_text = font.render("Upgrade Gun", True, BLACK)
        screen.blit(button_text, (110, 310))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if upgrade_button.collidepoint(event.pos):
                    if upgrade_gun():
                        print("Gun Upgraded!")
                    else:
                        print("Not enough points!")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Thoát shop
