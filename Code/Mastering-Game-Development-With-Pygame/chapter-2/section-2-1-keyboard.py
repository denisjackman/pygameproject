''' section 2.1 Keyboard '''
import pygame 


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    # create a game window 
    screen = pygame.display.set_mode((800, 600))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space Bar pressed")
        # game logic goes here 

        # drawing logic goes here

        # flip the screen 
        
        pygame.display.flip()
    pygame.quit()

 
if __name__ == "__main__":
    main()
