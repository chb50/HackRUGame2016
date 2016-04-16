import pygame
from ColorPallet import *
from classes import *
pygame.init()

display_width = 1000
display_height = 800

game_display = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()

#currently only prouces a white screen
def game():
    game_active = True
    while game_active:
        #create white screen
        game_display.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #quit when the exit window button is clicked
                game_active = False;
        #update display
        pygame.display.update()
        
        clock.tick(15)
    #quit pygame
    pygame.quit()

game()
