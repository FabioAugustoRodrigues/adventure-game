import pygame
import core.input as input
from components.player import Player
from components.sprite import sprites, Sprite
from core.map import TileKind, Map
from core.camera import create_screen
from components.entity import Entity, active_objs
from components.physics import Body

pygame.init()

screen = create_screen(800, 600, "Adventure Game")

clear_color = (30, 160, 50)
running = True

player = Entity(Player(), Sprite("player.png"), Body(8, 48, 16, 16), x = 400, y = 200)

tile_kinds = [ 
    TileKind("dirt", "dirt.png", False),
    TileKind("grass", "grass.png", False),
    TileKind("water", "water.png", True),
    TileKind("wood", "wood.png", False),
]

map = Map("start.map", tile_kinds, 32)

def make_tree(x, y):
    Entity(Sprite("tree.png"), Body(16, 96, 32, 32), x = x, y = y)

make_tree(100, 100)
make_tree(200, 100)
make_tree(300, 100)
make_tree(400, 100)
make_tree(500, 100)

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
    map.draw(screen)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()

    pygame.time.delay(17)

pygame.quit()