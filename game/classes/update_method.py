import pygame
from classes.controllers import Controlls



class RenderClass:

    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
    
    def renderUpdate(self):

        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))

        #instantiation player and logic
        playerObj = Controlls().PlayersControlls(self.screen,self.WIDTH,self.HEIGHT)


        self.screen.fill((0,0,0))

        ##############################################
        # RENDER AREA #

        playerObj.player()







        # FINISH RENDER AREA ##
        #############################################
        pygame.display.flip()
        