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
        pygame.draw.rect(screen,
                         (255, 0, 0),
                         (100, 100, 200, 150))
        pygame.draw.circle(screen,
                           (0, 0, 255),
                           (400, 200), 
                           50)
        vertices = [(500, 100),
                    (600, 200),
                    (450, 200)]
        pygame.draw.polygon(screen,
                            (0, 255, 0),
                            vertices)
        pygame.draw.line(screen,
                         (255 ,255, 255), 
                         (100, 100),
                         (400, 400))

        pygame.draw.line(screen,
                         (255 ,255, 255), 
                         (100, 200),
                         (400, 200),
                         width=2)

        # flip the screen 
        
        pygame.display.flip()
    pygame.quit()

 
if __name__ == "__main__":
    main()
