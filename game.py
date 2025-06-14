import pygame
import input
from player import Player
from sprite import sprites

pygame.init()

pygame.display.set_caption("Adventure Game")
screen = pygame.display.set_mode((800, 600))
clear_color = (30, 160, 50)
running = True

player = Player("images/player.png", 400, 300)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)

    player.update()

    screen.fill(clear_color)
    for s in sprites:
        s.draw(screen)
    pygame.display.flip()

    pygame.time.delay(17)

pygame.quit()