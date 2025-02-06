import pygame
import random
from ..setting import *
from ..renderer import *

def show_jumpscare(screen):
    jumpscare_image = load_background("assets/sprites/jumpscare.png")
    jumpscare_image = pygame.transform.scale(jumpscare_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    scare_sound = pygame.mixer.Sound("assets/sound/bonnie.mp3")  
    scare_sound.set_volume(0.2)  

    screen.fill(BLACK)
    pygame.display.update()
    pygame.time.delay(100)

    draw_background(screen, jumpscare_image)
    scare_sound.play()
    pygame.display.update()
    
    pygame.time.delay(random.randint(1000, 2000))
