import pygame
from setting import *

class Zombie:
    def __init__(self, x, y, head_img, jaw_img):
        # Ảnh đầu + hàm
        self.head_image = head_img
        self.jaw_image = jaw_img
        
        self.rect = self.head_image.get_rect(topleft=(x, y))
        self.is_visible = False
        
        # Animation cho hàm
        self.jaw_offset = 0
        self.jaw_direction = 1
        self.jaw_range = 5
        self.jaw_speed = 0.2
    
    def show(self):
        self.is_visible = True
    
    def hide(self):
        self.is_visible = False
        self.jaw_offset = 0
        self.jaw_direction = 1
    
    def update(self):
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
        
        # Vẽ đầu
        screen.blit(self.head_image, self.rect)
        
        # Tính toạ độ đáy đầu
        head_bottom_x = self.rect.x + self.rect.width // 2
        head_bottom_y = self.rect.y + self.rect.height
        
        # Jaw width, height
        jw = self.jaw_image.get_width()
        jh = self.jaw_image.get_height()
        
        # Vị trí chuẩn: miệng hàm chạm đáy đầu => top hàm = đáy đầu - jh
        jaw_x = head_bottom_x - jw // 2
        jaw_y = head_bottom_y - jh
        
        # Thêm jaw_offset để hàm nhấp nhô
        # Ở đây mình coi jaw_offset là "mở" xuống, nên:
        jaw_y += self.jaw_offset
        
        # Nếu cần lệch x chút, ví dụ -3 px:
        # jaw_x -= 3
        
        # Vẽ hàm
        screen.blit(self.jaw_image, (jaw_x, jaw_y))
