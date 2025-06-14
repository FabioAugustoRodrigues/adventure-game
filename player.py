import pygame
from sprite import Sprite
from input import is_key_pressed

class Player(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.movment_speed = 2

    def update(self):
        if is_key_pressed(pygame.K_w):
            self.y -= self.movment_speed
        if is_key_pressed(pygame.K_s):
            self.y += self.movment_speed
        if is_key_pressed(pygame.K_a):
            self.x -= self.movment_speed
        if is_key_pressed(pygame.K_d):
            self.x += self.movment_speed