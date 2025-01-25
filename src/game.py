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
    def __init__(self, bullet_limit, image_path, shoot_sound_path):
        self.bullets = bullet_limit  
        self.bullet_limit = bullet_limit  
        self.shoot_sound = pygame.mixer.Sound(shoot_sound_path)  
        self.hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")  
        self.image = pygame.image.load(image_path)  
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))
        self.reload_sound = pygame.mixer.Sound("assets/sound/reload.wav")

    def shoot(self):
        if self.bullets > 0:
            self.shoot_sound.play()
            self.bullets -= 1
            return True
        return False

    def play_hit_sound(self):
        self.hit_sound.play()

    def reload(self):
        self.reload_sound.play()
        self.bullets = self.bullet_limit

    def draw(self, screen):
        screen.blit(self.image, self.rect)
