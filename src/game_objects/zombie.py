import pygame
from setting import *

class Zombie:
    def __init__(self, jar_x, jar_y, jar_w, jar_h, head_img, jaw_img):
        self.head_image = head_img
        self.jaw_image = jaw_img

        self.rect = self.head_image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

        self.final_x = jar_x + (jar_w // 2) - (self.width // 2)
        self.final_y = jar_y - (self.height * 17 // 20)

        self.start_y = jar_y + self.height - 10

        self.rect.topleft = (self.final_x, self.start_y)
        self.is_visible = False  
        self.is_rising = False   

        self.rising_speed = 3

        self.jaw_offset = 0
        self.jaw_direction = 1
        self.jaw_range = 5
        self.jaw_speed = 0.2

    def show(self):
        if not self.is_visible:
            self.is_visible = True
            self.is_rising = True
            self.rect.y = self.start_y

    def hide(self):
        self.is_visible = False
        self.is_rising = False
        self.jaw_offset = 0
        self.jaw_direction = 1

    def update(self):
        if self.is_visible and self.is_rising:
            self.rect.y -= self.rising_speed
            if self.rect.y <= self.final_y:
                self.rect.y = self.final_y
                self.is_rising = False  

        if self.is_visible:
            self.jaw_offset += self.jaw_direction * self.jaw_speed
            if self.jaw_offset > self.jaw_range:
                self.jaw_offset = self.jaw_range
                self.jaw_direction = -1
            elif self.jaw_offset < 0:
                self.jaw_offset = 0
                self.jaw_direction = 1

    def draw(self, screen):
        if not self.is_visible:
            return

        screen.blit(self.head_image, self.rect)

        head_bottom_x = self.rect.x + self.rect.width // 2
        head_bottom_y = self.rect.y + self.rect.height

        jw = self.jaw_image.get_width()
        jh = self.jaw_image.get_height()

        jaw_x = head_bottom_x - jw // 2
        jaw_y = head_bottom_y - jh + 10  
        jaw_y += self.jaw_offset  

        screen.blit(self.jaw_image, (jaw_x, jaw_y))
