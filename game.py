import pygame
import input
from player import Player
from sprite import sprites, Sprite
from map import TileKind, Map
from camera import create_screen
from entity import Entity, active_objs
from physics import Body

pygame.init()

screen = create_screen(800, 600, "Adventure Game")

clear_color = (30, 160, 50)
running = True

player = Entity(Player(), Sprite("images/player.png"), Body(8, 48, 16, 16), x = 400, y = 200)

tile_kinds = [ 
    TileKind("dirt", "images/dirt.png", False),
    TileKind("grass", "images/grass.png", False),
    TileKind("water", "images/water.png", True),
    TileKind("wood", "images/wood.png", False),
]

map = Map("maps/start.map", tile_kinds, 32)

def make_tree(x, y):
    Entity(Sprite("images/tree.png"), Body(16, 96, 32, 32), x = x, y = y)

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