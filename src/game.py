import pygame
import core.input as input
from components.player import Player
from components.sprite import sprites, Sprite
from core.map import TileKind, Map
from core.camera import create_screen
from components.entity import Entity, active_objs
from components.physics import Body
from core.area import Area, area
from data.tile_types import tile_kinds

pygame.init()

screen = create_screen(800, 600, "Adventure Game")

clear_color = (30, 160, 50)
running = True

area = Area("start.map", tile_kinds)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)

    for a in active_objs:
        a.update()

    screen.fill(clear_color)
    area.map.draw(screen)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()

    pygame.time.delay(17)

pygame.quit()