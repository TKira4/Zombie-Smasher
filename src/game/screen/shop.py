import pygame
from ..setting import *
from ..logic.data import *
from ..renderer import *

shop_bg = load_background("assets/sprites/shop.png")
shop_bg = pygame.transform.scale(shop_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

def show_shop(screen):
    message = ""  
    message_timer = 0  
    while True:
        draw_background(screen, shop_bg)
        draw_text(screen, "SHOP - UPGRADE GUN", WINDOW_WIDTH // 2 - 125, 50, 48, LIGHT_GRAY)

        score = get_point()
        gun_level = get_gun_level()
        upgrade_cost = gun_level * 100

        draw_text(screen, f"Your Score: {score}", 500, 200, 36, WHITE)
        draw_text(screen, f"Gun Level: {gun_level}", 500, 250, 36, WHITE)
        draw_text(screen, f"Upgrade Cost: {upgrade_cost} Points", 500, 300, 36, WHITE)

        upgrade_button = draw_button(screen, "Upgrade Gun", 500, 350, 200, 50, YELLOW, DARK_GREEN, BLACK)
        back_button = draw_button(screen, "Back", 25, 50, 100, 50, RED, DARK_RED, BLACK)

        if message:
            draw_text(screen, message, 475, 400, 30, YELLOW)

            if pygame.time.get_ticks() - message_timer > 2000:  
                message = ""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if upgrade_button.collidepoint(event.pos):
                    message = upgrade_gun()
                    message_timer = pygame.time.get_ticks()
                if back_button.collidepoint(event.pos):
                    return 
                
        pygame.display.flip()
