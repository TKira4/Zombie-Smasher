import pygame
from ..setting import *

class Zombie:
    #Zombie xuat hien tu binh
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.is_visible = False
    
    def show(self):
        self.is_visible = True
    
    def hide(self):
        self.is_visible = False
        
    def draw(self, screen):
        if self.is_visible:
            screen.blit(self.image, self.rect)