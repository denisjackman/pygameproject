''' section 1.3 '''
import pygame 

background_colour = pygame.Color("white")
text_color = pygame.Color("black")
highlight_color = pygame.Color("red")


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
        screen.fill(background_colour)
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Hello Pygame!",
                                   True,
                                   text_color)
        screen.blit(text_surface,
                    (300, 300))

        # flip the screen 
        
        pygame.display.flip()
    pygame.quit()

 
if __name__ == "__main__":
    main()
