import pygame

def load_image(path, scale=None):
    image = pygame.image.load(path)
    if scale:
        image = pygame.transform.scale(image, scale)
    return image

def check_collision(point, rect):
    return rect.collidepoint(point)
        