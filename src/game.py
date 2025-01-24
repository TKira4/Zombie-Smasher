import pygame
import random
from setting import *

class Zombie:
    #Zombie xuat hien tu binh
    def __init__(self, x, y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.is_visible = False
    
    def show(self):
        self.is_visible = True
    
    def hide(self):
        self.is_visible = False
        
    def draw(self, screen):
        if self.is_visible:
            screen.blit(self.image, self.rect)
            
class Jar:
    #Binh chua dau Zombie
    def __init__(self, x, y, image, zombie):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.zombie = zombie
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.zombie.draw(screen)
        
class Gun:
    #sung
    def __init__(self, bullet_limit, sound_path):
        self.bullets = bullet_limit
        self.shoot_sound = pygame.mixer.Sound(sound_path)
        
    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            self.shoot_sound.play()
            return True
        return False
    
    def reload(self):
        self.bullets = BULLET_LIMIT