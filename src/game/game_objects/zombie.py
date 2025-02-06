import pygame
import math
import time
import random
from ..setting import *

class Zombie:
    def __init__(self, jar_x, jar_y, jar_w, jar_h, head_img, jaw_img, helmet_imgs, dead_img):
        self.head_image = head_img
        self.jaw_image = jaw_img
        self.dead_image = dead_img
        self.helmet_images = helmet_imgs
        self.has_helmet = random.choices([True, False], weights=[0.2, 0.8], k=1)[0]
        self.helmet_stage = 0 if self.has_helmet else -1

        self.rect = self.head_image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

        self.final_x = jar_x + (jar_w // 2) - (self.width // 2)
        self.final_y = jar_y - (self.height * 17 // 20)
        self.start_y = jar_y + self.height - 10

        self.rect.topleft = (self.final_x, self.start_y)
        self.is_visible = False  
        self.is_rising = False   
        self.is_falling = False  
        self.is_invulnerable = False  

        self.rising_speed = 3
        self.falling_speed = 2
        self.spawn_time = None  

        self.jaw_offset = 0
        self.jaw_direction = 1
        self.jaw_range = 5
        self.jaw_speed = 0.2

        self.float_offset = 0  
        self.float_speed = 0.02  
        self.health = 4 if self.has_helmet else 1

    def show(self):
        if not self.is_visible:
            self.is_visible = True
            self.is_rising = True
            self.is_falling = False
            self.is_invulnerable = False
            self.rect.y = self.start_y
            self.spawn_time = time.time()

    def hide(self):
        self.is_falling = True
        self.is_invulnerable = True  

    def hit(self):
        if not self.is_invulnerable:  
            if self.health > 1:
                self.health -= 1
                if self.has_helmet:
                    self.helmet_stage += 1
                    if self.helmet_stage >= len(self.helmet_images):
                        self.has_helmet = False
            else:
                self.hide()

    def update(self):
        if self.is_visible and self.is_rising:
            self.rect.y -= self.rising_speed
            if self.rect.y <= self.final_y:
                self.rect.y = self.final_y
                self.is_rising = False  

        if self.is_visible and not self.is_rising and not self.is_falling:
            self.float_offset = math.sin((time.time() - self.spawn_time) * 2) * 5
            self.rect.y = self.final_y + self.float_offset  

            self.jaw_offset += self.jaw_direction * self.jaw_speed
            if self.jaw_offset > self.jaw_range:
                self.jaw_offset = self.jaw_range
                self.jaw_direction = -1
            elif self.jaw_offset < 0:
                self.jaw_offset = 0
                self.jaw_direction = 1

        if self.is_falling:
            self.rect.y += self.falling_speed
            if self.rect.y >= self.start_y:
                self.is_visible = False
                self.is_falling = False
                self.is_invulnerable = False
                self.jaw_offset = 0
                self.jaw_direction = 1
                self.spawn_time = None

    def draw(self, screen):
        if not self.is_visible:
            return

        if self.is_falling:
            screen.blit(self.dead_image, self.rect)
        else:
            screen.blit(self.head_image, self.rect)

        head_bottom_x = self.rect.x + self.rect.width // 2
        head_bottom_y = self.rect.y + self.rect.height

        jw = self.jaw_image.get_width()
        jh = self.jaw_image.get_height()

        jaw_x = head_bottom_x - jw // 2
        jaw_y = head_bottom_y - jh + 10
        jaw_y += self.jaw_offset  

        if not self.is_falling:
            screen.blit(self.jaw_image, (jaw_x, jaw_y))

        if self.has_helmet and self.helmet_stage < len(self.helmet_images):
            helmet_img = self.helmet_images[self.helmet_stage]
            helmet_x = self.rect.x + (self.width // 2) - (helmet_img.get_width() // 2) + 6
            helmet_y = self.rect.y - 12
            screen.blit(helmet_img, (helmet_x, helmet_y))

    def is_time_out(self):
        if self.is_visible and self.spawn_time is not None:
            return time.time() - self.spawn_time > 5
        return False
