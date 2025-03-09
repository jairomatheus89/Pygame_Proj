import pygame
from controlls.pingalogic import get_pingaScore

WHITE = (255,255,255)
YELLOW = (255,255,0)

pygame.init()

font = pygame.font.Font(None, 56)

pingaText_rect = pygame.Rect( (1280/2) - 100 , 100, 100,100 )

def render_score():

    pingaScore = get_pingaScore()

    return font.render(f"Pingas:{pingaScore}",True,YELLOW)
    
    