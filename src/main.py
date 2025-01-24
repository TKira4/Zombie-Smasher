import pygame
import sys
from setting import *
from game import Zombie, Jar, Gun
from util import load_image, check_collision

#khoi tao game
pygame.init
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Smasher")
clock = pygame.time.Clock()

#load tai nguyen
zombie_image = "assets/sprites/zombie_head.png"
jar_image = "assets/sprites/jar.png"