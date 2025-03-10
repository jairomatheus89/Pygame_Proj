import pygame

##### ACTORS IMPORT #####
from actors.playerrect import playerRect , lulapng, lulapngSurf
from actors.pingarect import pingaRect , pingapngSurf
import fonts

###### LOGICI IMPORTS #######
from controlls.playerControlls.controll import controll_player # player controll
from controlls.pingalogic import pinga_PlayerCollision , get_pingaScore # pingacontroll

################## vars logic #########


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ###### LOGIC RENDER $######### function,vars,etc...
    controll_player()
    pinga_PlayerCollision()

    pingaScore = get_pingaScore()

    #BLACK SCREEN BASE SURFACE
    screen.fill("black")

    ################# RENDER YOUR GAME HERE #################


    screen.blit(lulapngSurf, playerRect.topleft)

    screen.blit(pingapngSurf, pingaRect.topleft)

    screen.blit(fonts.render_score(),fonts.pingaText_rect)

    screen.blit(fonts.cheatbuttonText,fonts.cheatbuttonRect)


         ##### HIT BOXES rects ########
    #pygame.draw.rect(screen,"WHITE",playerRect,3)
    #pygame.draw.rect(screen,"RED",pingaRect,3)
    #pygame.draw.rect(screen,"YELLOW",fonts.cheatbuttonRect,3)

    #update frames
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()