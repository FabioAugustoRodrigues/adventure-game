import pygame
from sprite import Sprite
from input import is_key_pressed
from camera import camera

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
        camera.x = self.x - camera.width/2 + self.image.get_width()/2
        camera.y = self.y - camera.height/2 + self.image.get_height()/2