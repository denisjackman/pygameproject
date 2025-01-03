''' section 6.5'''
import sys 
import pygame
import random

sys.path.append("../../utils")
import rgb
import djpg

WIDTH = 800
HEIGHT = 600 
BACKGROUND_COLOR = rgb.BLACK
BUTTON_COLOR = rgb.GREEN
DOOR_COLOR = rgb.RED
BUTTON_SIZE = (50, 50)
DOOR_SIZE = (100, 200)


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    # create a game window 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Interactive Environment Example")
    # set the game running flag to true
    running = True
    
    button_position = (100, 300)
    door_position = (600, 200)
    button_pressed = False
    button_rect = pygame.Rect(button_position, BUTTON_SIZE)
    door_rect = pygame.Rect(door_position, DOOR_SIZE)
    # run the game loop
    while running:
        # check for user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    button_pressed = True
                if door_rect.collidepoint(event.pos):
                    button_pressed = False

        # drawing logic goes here
        # clear the screen
        screen.fill(BACKGROUND_COLOR)

        
        pygame.draw.rect(screen,
                         BUTTON_COLOR if not button_pressed else rgb.MEDIUM_GREEN,
                         button_rect)
        
        if button_pressed:
            pygame.draw.rect(screen,
                             DOOR_COLOR,
                             door_rect)
        # flip the screen        
        pygame.display.flip()
    # close pygame
    pygame.quit()

 
if __name__ == "__main__":
    main()
