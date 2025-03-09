import pygame
import random
from actors.pingarect import pingaRect
from actors.playerrect import playerRect

pingaScore = 0

def pinga_PlayerCollision():
    global pingaScore

    if playerRect.colliderect(pingaRect):
        pingaRect.x = random.randint(1,1280 - 50)
        pingaRect.y = random.randint(1,720 - 50)
        pingaScore += 1

def get_pingaScore():
    return pingaScore
    
    
        