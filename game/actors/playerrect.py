import pygame

lulapng = pygame.image.load('game/assets/lula.png')

playerRect = pygame.Rect(100,100,100,100)

lulapngSurf = pygame.transform.scale(lulapng,(playerRect.width, playerRect.height))

