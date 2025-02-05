import pygame
from setting import *

class Jar:
    #Binh chua dau Zombie
    def __init__(self, x, y, image, zombie):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.zombie = zombie
        
    def draw(self, screen):
        self.zombie.draw(screen)
        screen.blit(self.image, self.rect)