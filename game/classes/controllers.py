import pygame

class Controlls:

    class PlayersControlls:

        def __init__(self,screen,WIDTH,HEIGHT):
            self.screen = screen
            self.size_width = 40
            self.size_height = 60
            self.x_coord = (WIDTH / 2) - (self.size_width / 2)
            self.y_coord = (HEIGHT / 2) - (self.size_height / 2)


        def player(self):
            #player Rect Draw
            self.rect = (self.x_coord,self.y_coord,self.size_width,self.size_height)

            return pygame.draw.rect(self.screen,"PINK",self.rect)
            
    