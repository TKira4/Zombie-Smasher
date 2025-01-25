import pygame
import sys
import random
from setting import *
from game import Zombie, Jar, Gun
from util import load_image, check_collision

#khoi tao game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Smasher")
clock = pygame.time.Clock()

#load tai nguyen
zombie_image = "assets/sprites/zombie_head.png"
jar_image = "assets/sprites/jar.png"
gun = Gun(BULLET_LIMIT, "assets/sprites/gun.png", "assets/sound/8bit_gunloop_explosion.wav")

#luu trang thai dau
game_state = "menu" #cac states gom menu, playing, game_over, shop
difficulty = 3
score = 0
combo = 0

#display menu
def show_menu():
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 48)
    title_text = font.render("Zombie Smasher", True, BLACK)
    screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 100))
    
    #chon do kho
    easy_text = font.render("1. Easy (3x3)", True, BLACK)
    medium_text = font.render("2. Medium (5x5)", True, BLACK)
    hard_text = font.render("3. Hard (7x7)", True, BLACK)
    
    screen.blit(easy_text, (WINDOW_WIDTH // 2 - easy_text.get_width() // 2, 200))
    screen.blit(medium_text, (WINDOW_WIDTH // 2 - medium_text.get_width() // 2, 250))
    screen.blit(hard_text, (WINDOW_WIDTH // 2 - hard_text.get_width() // 2, 300))
    
    pygame.display.flip()
    
#tao binh va zombie
def create_jars(n):
    jars = []
    for i in range(n):
        for j in range(n):
            x, y = 150 + j * (JAR_SIZE + 10), 100 + i * (JAR_SIZE + 10)
            zombie = Zombie(x, y, zombie_image)
            jar = Jar(x, y, jar_image, zombie)
            jar.append(jar)
    return jar

#game loop
running = True
jars = []
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #chon do kho
        if event.type == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = 3
                    jars = create_jars(difficulty)
                if event.key == pygame.K_2:
                    difficulty = 5
                    jars = create_jars(difficulty)
                if event.key == pygame.K_3:
                    difficulty = 7
                    jars = create_jars(difficulty)
                game_state = "playing"
        
        #logic game
        elif game_state == "playing":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gun.shoot():
                    hit = False
                    for jar in jars:
                        if jar.zombie.is_visible and check_collision(event.pos, jar.zombie.rect):
                            jar.zombie.hide()
                            hit = True
                            gun.play_hit_sound()
                            score += 10 + combo * COMBO_MULTIPLIER
                            combo += 1
                            break
                    if not hit:
                        combo = 0
        
        if game_state == "menu":
            show_menu()
        
        #cap nhat game object
        elif game_state =="playing":
            for jar in jars:
                jar.zombie.show() if random.random() < 0.01 else None
                jar.draw(screen)
                
            font = pygame.font.SysFont(None, 36)
            bullet_text = font.render(f"Bullets: {gun.bullets}", True, BLACK)
            score_text = font.render(f"Score: {score}", True, BLACK)
            combo_text = font.render(f"Combo: {combo}", True, BLACK)
            screen.blit(bullet_text, (10, 10))
            screen.blit(score_text, (10, 50))
            screen.blit(combo_text, (10, 90))
            
            #kiem tra dan
            if gun.bullets <= 0:
                gun.reload()
                
        gun.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
        
pygame.quit()
sys.exit()
        
        

