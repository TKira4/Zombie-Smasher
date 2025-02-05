import pygame
from setting import *

class Gun:
    def __init__(self, bullet_limit, image_path, shoot_sound_path):
        self.bullets = bullet_limit  
        self.bullet_limit = bullet_limit  
        self.shoot_sound = pygame.mixer.Sound(shoot_sound_path)  
        self.hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")  
        self.image = pygame.image.load(image_path)  
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50))
        self.reload_sound = pygame.mixer.Sound("assets/sound/reload.wav")
        self.is_reloading = False
        self.reload_start_time = 0
        self.shoot_sound.set_volume(0.3)  
        self.hit_sound.set_volume(1)    
        self.reload_sound.set_volume(0.5) 
        
        pygame.mouse.set_visible(False) #an con tro chuot
        
    def shoot(self):
        if self.bullets > 0 and not self.is_reloading:
            self.shoot_sound.play()
            self.bullets -= 1
            return True
        return False

    def play_hit_sound(self):
        self.hit_sound.play()

    def reload(self):
        if not self.is_reloading:
            self.reload_sound.play()
            self.is_reloading = True
            self.reload_start_time = pygame.time.get_ticks()
            
    def update_reload(self):
        if self.is_reloading:
            current_time = pygame.time.get_ticks()
            if current_time - self.reload_start_time >= 1500:
                self.bullets = BULLET_LIMIT
                self.is_reloading = False
                
    def update_pos(self, mouse_pos):
        self.rect.center = mouse_pos
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        

