import pygame
from classes.update_method import RenderClass

render = RenderClass()
clock = pygame.time.Clock()

############################

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    render.renderUpdate()


    clock.tick(30)
pygame.quit()