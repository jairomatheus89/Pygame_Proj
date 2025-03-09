import pygame
from player.playerrect import playerRect


speedPlayer = 10

def controll_player():

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        playerRect.x -= speedPlayer
    if keys[pygame.K_RIGHT]:
        playerRect.x += speedPlayer
    if keys[pygame.K_UP]:
        playerRect.y -= speedPlayer
    if keys[pygame.K_DOWN]:
        playerRect.y += speedPlayer
