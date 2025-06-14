import pygame

pygame.init()

pygame.display.set_caption("Adventure Game")
screen = pygame.display.set_mode((800, 600))
clear_color = (30, 160, 50)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(clear_color)

    pygame.display.flip()

pygame.quit()