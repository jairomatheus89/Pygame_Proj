import pygame
import random

pingapng = pygame.image.load('game/assets/pinga.png')

pingaRect = pygame.Rect(random.randint(1,1280 - 50),random.randint(1,720 - 50),100,100)

pingapngSurf = pygame.transform.scale(pingapng,(pingaRect.width,pingaRect.height))