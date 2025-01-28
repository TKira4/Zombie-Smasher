import pygame
import random

from setting import *
from game_objects.im import *
from logic.util import check_collision
from renderer import draw_ui
#logic chinh cua game
def start_game(screen, difficulty):
    clock = pygame.time.Clock()
    
    #load tai nguyen
    gun = Gun(BULLET_LIMIT, "assets/sprites/gun.png", "assets/sound/8bit_gunloop_explosion.wav")
    zombie_image = pygame.image.load("assets/sprites/zombie_head.png")
    jar_image = pygame.image.load("assets/sprites/jar.png")

    #scale img
    zombie_image = pygame.transform.scale(zombie_image, (ZOMBIE_WIDTH, ZOMBIE_HEIGHT))
    jar_image = pygame.transform.scale(jar_image, (JAR_WIDTH, JAR_HEIGHT))

    #tao binh voi do kho
    jars = create_jars(difficulty, zombie_image, jar_image)

    #inital state
    score = 0
    combo = 0
    running = True
    last_shoot_time = pygame.time.get_ticks()

    #vong lap chinh
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return score

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
                            #ban trung zombie se update time
                            last_shoot_time = pygame.time.get_ticks()
                            break
                    if not hit:
                        combo = 0

            #nap dan bang phim R
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                gun.reload()
                
        #sung di chuyen theo chuot
        gun.update_pos(pygame.mouse.get_pos())

        #zombie xuat hien tu binh
        for jar in jars:
            if random.random() < 0.01:
                jar.zombie.show()
            jar.draw(screen)

        #kiem tra trang thai reload
        gun.update_reload()

        if pygame.time.get_ticks() - last_shoot_time > 5000:
            return score  

        gun.draw(screen)

        draw_ui(screen, gun, score, combo)

        pygame.display.flip()
        clock.tick(FPS)

#tao binh
def create_jars(n, zombie_image, jar_image):
    jars = []
    for i in range(n):
        for j in range(n):
            x, y = 150 + j * (JAR_SIZE + 10), 100 + i * (JAR_SIZE + 10)
            zombie = Zombie(x, y, zombie_image)
            jar = Jar(x, y, jar_image, zombie)
            jars.append(jar)
    return jars
