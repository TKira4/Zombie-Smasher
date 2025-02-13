import pygame
from ..renderer import *
from ..setting import *

game_over_bg = load_background("assets/sprites/game_over.png")
game_over_bg = pygame.transform.scale(game_over_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
def show_game_over(screen, score, max_combo, miss_hit):
    #screen.fill(WHITE)
    pygame.mouse.set_visible(True)
    draw_background(screen, game_over_bg)
    draw_text(screen, f"Score: {score}", 50, 50, 36, WHITE)
    draw_text(screen, f"Max_combo: {max_combo}", 250, 50, 36, RED)
    draw_text(screen, f"Miss_hit: {miss_hit}", 550, 50, 36, YELLOW)
    
    replay_button = draw_button(screen, "Replay", 150, 450, 150, 50, WHITE, LIGHT_GRAY, BLACK)
    menu_button = draw_button(screen, "Home", 350, 450, 150, 50, WHITE, LIGHT_GRAY, BLACK)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if replay_button.collidepoint(event.pos):
                    return "playing"
            elif menu_button.collidepoint(event.pos):
                    return "menu"
    
    # pygame.time.wait(3000)
