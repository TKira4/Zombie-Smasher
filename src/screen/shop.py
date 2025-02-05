import pygame
from setting import *
from logic.data import *
from renderer import *

shop_bg = load_background("assets/sprites/shop.png")


def show_shop(screen):
    while True:
        screen.fill(WHITE)
        draw_text(screen, "SHOP - UPGRADE GUN", WINDOW_WIDTH // 2 - 150, 50, 48, BLACK)

        score = get_score()
        gun_level = get_gun_level()
        upgrade_cost = gun_level * 100

        draw_text(screen, f"Your Score: {score}", 100, 150, 36, BLACK)
        draw_text(screen, f"Gun Level: {gun_level}", 100, 200, 36, BLACK)
        draw_text(screen, f"Upgrade Cost: {upgrade_cost} Points", 100, 250, 36, BLACK)

        upgrade_button = draw_button(screen, "Upgrade Gun", 100, 300, 200, 50, YELLOW, DARK_GREEN)
        back_button = draw_button(screen, "Back", 100, 400, 200, 50, RED, DARK_RED)

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
                if back_button.collidepoint(event.pos):
                    return  # Quay lại menu
