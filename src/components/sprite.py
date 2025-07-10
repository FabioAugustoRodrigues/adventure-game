import pygame
from core.camera import camera
from core.engine import engine

image_path = "../content/images"

loaded = {}

class Sprite:
    def __init__(self, image):
        global sprites
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image_path + "/" + image)
            loaded[image] = self.image
        engine.drawables.append(self)

    def delete(self):
        engine.drawables.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.entity.x - camera.x, self.entity.y - camera.y))

# Load things uniquely.