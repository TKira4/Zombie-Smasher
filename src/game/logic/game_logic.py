import pygame
import random

from ..renderer import *
from  ..logic.data import *
from ..setting import *
from ..game_objects.im import *
from .util import check_collision
from ..renderer import draw_ui
#logic chinh cua game

game_bg = load_background("assets/sprites/game.png")
game_bg = pygame.transform.scale(game_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

def start_game(screen, difficulty):
    clock = pygame.time.Clock()
    global zombie_head_image, zombie_jaw_image, jar_image, zombie_helmet_images
    
    new_size = WINDOW_WIDTH // (difficulty+4)

    gun = Gun(BULLET_LIMIT + get_gun_level() // 5, "assets/sprites/aimGun.png", "assets/sound/8bit_gunloop_explosion.wav")
    zombie_head_image = pygame.image.load("assets/sprites/zombie_head.png")
    zombie_jaw_image = pygame.image.load("assets/sprites/zombie_jaw.png")
    zombie_helmet_images = [
        pygame.image.load("assets/sprites/Zombie_football_helmet.png"),
        pygame.image.load("assets/sprites/Zombie_football_helmet2.png"),
        pygame.image.load("assets/sprites/Zombie_football_helmet3.png")
    ]
    jar_image = pygame.image.load("assets/sprites/jar.png")

    zombie_head_image = pygame.transform.scale(zombie_head_image, (new_size * zombie_head_image.get_width() // 100, new_size * zombie_head_image.get_height() // 100))
    zombie_jaw_image = pygame.transform.scale(zombie_jaw_image, (new_size * zombie_jaw_image.get_width() // 100, new_size * zombie_jaw_image.get_height() // 100))
    zombie_helmet_images = [pygame.transform.scale(img, (new_size * img.get_width() // 100, new_size * img.get_height() // 100)) for img in zombie_helmet_images]
    jar_image = pygame.transform.scale(jar_image, (new_size, new_size))

    jars = create_jars(difficulty, new_size)

    score = 0
    combo = 0
    running = True

    max_combo = 0
    miss_hit = 0
    while running:
        #screen.fill(WHITE)
        draw_background(screen, game_bg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return score

            if event.type == pygame.MOUSEBUTTONDOWN:
                if gun.shoot():
                    hit = False
                    for jar in jars:
                        if jar.zombie.is_visible and check_collision(event.pos, jar.zombie.rect):
                            jar.zombie.hit()
                            hit = True
                            gun.play_hit_sound()
                            score += 10 + combo * COMBO_MULTIPLIER
                            combo += 1
                            break
                    if not hit:
                        combo = 0
                        miss_hit += 1

            max_combo = max(max_combo, combo)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                gun.reload()
                
        gun.update_pos(pygame.mouse.get_pos())

        for jar in jars:
            jar.zombie.update()
            if random.random() < 0.001:
                jar.zombie.show()
            if jar.zombie.is_time_out():
                add_point(score)
                data = load_data()
                return score, max_combo, miss_hit
            jar.draw(screen)

        gun.update_reload()
        gun.draw(screen)
        draw_ui(screen, gun, score, combo)

        pygame.display.flip()
        clock.tick(FPS)   


#tao binh
def create_jars(n, size):
    jars = []
    padding = 10  #khoang cach giua cac binh`

    start_x = (WINDOW_WIDTH - (n * (size + padding))) // 2  # Can giua
    start_y = 100  

    for i in range(n):
        for j in range(n):
            x = start_x + j * (size + padding)  
            y = start_y + i * (size + padding)  

            zombie = Zombie(x, y, size, size, zombie_head_image, zombie_jaw_image, zombie_helmet_images)
            jar = Jar(x, y, jar_image, zombie)
            jars.append(jar)

    return jars


