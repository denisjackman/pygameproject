''' section 1.3 '''
import sys 
import pygame
import random

sys.path.append("../../utils")
import rgb
import djpg


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    # create a game window 
    screen = pygame.display.set_mode((800, 600))
    # set the game running flag to true
    running = True

    # run the game loop
    while running:
        # check for user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
            
        # game logic goes here 

        # drawing logic goes here

        # clear the screen
        screen.fill(rgb.BLACK)

        # flip the screen        
        pygame.display.flip()
    # close pygame
    pygame.quit()

 
if __name__ == "__main__":
    main()
