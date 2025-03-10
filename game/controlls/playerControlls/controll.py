import pygame
from actors.playerrect import playerRect
from actors.pingarect import pingaRect


speedPlayer = 10

def controll_player():

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and playerRect.x > 0:
        playerRect.x -= speedPlayer
    if keys[pygame.K_RIGHT] and playerRect.x < 1280 - playerRect.width:
        playerRect.x += speedPlayer
    if keys[pygame.K_UP] and playerRect.y > 0:
        playerRect.y -= speedPlayer
    if keys[pygame.K_DOWN] and playerRect.y < 720 - playerRect.height:
        playerRect.y += speedPlayer

    if keys[pygame.K_l]:
        pingaRect.y = playerRect.y
        pingaRect.x = playerRect.x

