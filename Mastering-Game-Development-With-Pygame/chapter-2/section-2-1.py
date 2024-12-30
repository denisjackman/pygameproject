''' section 1.3 '''
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
        # game logic goes here 

        # drawing logic goes here
        background = pygame.Surface(screen.get_size())
        background.fill((255, 255, 255))
        pygame.draw.rect(background,
                         (255, 0, 0),
                         (100, 100, 50, 50))
        pygame.draw.circle(background,
                           (0, 0, 255),
                           (300, 300),
                           30)
        screen.blit(background,
                    (0, 0))
        # flip the screen 
        
        pygame.display.flip()
    pygame.quit()

 
if __name__ == "__main__":
    main()
