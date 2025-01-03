''' section 6.4'''
import sys 
import pygame
import random

sys.path.append("../../utils")
import rgb
import djpg

WIDTH = 800
HEIGHT = 600 
BACKGROUND_COLOR = rgb.BLACK
LIGHT_COLOR = (255, 255, 0)
SHADOW_COLOR = (0, 0, 0, 200)
def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    # create a game window 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2D Lighting Example")
    light_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    # set the game running flag to true
    running = True
    # run the game loop
    while running:
        # check for user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
        # drawing logic goes here
        # clear the screen
        screen.fill(BACKGROUND_COLOR)
        light_surface.fill((0, 0, 0, 0))
        pygame.draw.circle(light_surface,
                           LIGHT_COLOR,
                           (400, 300),
                           100)
        screen.blit(light_surface,
                    (0, 0),
                    special_flags=pygame.BLEND_RGB_MULT)
        pygame.draw.rect(screen,
                         SHADOW_COLOR,
                         (0, 0, WIDTH, HEIGHT))
        # flip the screen        
        pygame.display.flip()
    # close pygame
    pygame.quit()

 
if __name__ == "__main__":
    main()
