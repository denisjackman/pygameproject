''' section 2.1 mouse '''
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("left mouse button pressed")
                else:
                    print(f"{event.button} pressed")
        # game logic goes here 

        # drawing logic goes here

        # flip the screen 
        
        pygame.display.flip()
    pygame.quit()

 
if __name__ == "__main__":
    main()
