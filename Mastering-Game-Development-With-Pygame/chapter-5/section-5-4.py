''' section 5.4 '''
import sys 
import pygame

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

    player_x = 400
    player_y = 500
    player_speed = 5

    # run the game loop
    while running:
        # check for user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
            
        # game logic goes here 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
            
        # drawing logic goes here

        # clear the screen
        screen.fill(rgb.BLACK)
        pygame.draw.rect(screen,
                         rgb.RED,
                         (player_x, player_y, 50, 50))

        # flip the screen        
        pygame.display.flip()
    # close pygame
    pygame.quit()

 
if __name__ == "__main__":
    main()
