import pygame
from components.sprite import Sprite
from core.input import is_key_pressed
from core.camera import camera
from components.entity import active_objs
from components.physics import Body

class Player:
    def __init__(self):
        self.movment_speed = 2
        active_objs.append(self)

    def update(self):
        previous_x = self.entity.x
        previous_y = self.entity.y

        body = self.entity.get(Body)
        sprite = self.entity.get(Sprite)

        if is_key_pressed(pygame.K_w):
            self.entity.y -= self.movment_speed
        if is_key_pressed(pygame.K_s):
            self.entity.y += self.movment_speed
        if not body.is_position_valid():
            self.entity.y = previous_y

        if is_key_pressed(pygame.K_a):
            self.entity.x -= self.movment_speed
        if is_key_pressed(pygame.K_d):
            self.entity.x += self.movment_speed
        if not body.is_position_valid():
            self.entity.x = previous_x

        camera.x = self.entity.x - camera.width/2 + sprite.image.get_width()/2
        camera.y = self.entity.y - camera.height/2 + sprite.image.get_height()/2