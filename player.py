import pygame
from sprite import Sprite
from input import is_key_pressed
from camera import camera
from entity import active_objs

class Player:
    def __init__(self):
        self.movment_speed = 2
        active_objs.append(self)

    def update(self):
        sprite = self.entity.get(Sprite)
        if is_key_pressed(pygame.K_w):
            self.entity.y -= self.movment_speed
        if is_key_pressed(pygame.K_s):
            self.entity.y += self.movment_speed
        if is_key_pressed(pygame.K_a):
            self.entity.x -= self.movment_speed
        if is_key_pressed(pygame.K_d):
            self.entity.x += self.movment_speed
        camera.x = self.entity.x - camera.width/2 + sprite.image.get_width()/2
        camera.y = self.entity.y - camera.height/2 + sprite.image.get_height()/2