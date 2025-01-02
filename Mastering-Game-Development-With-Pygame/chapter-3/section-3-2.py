''' section 3.2 '''
import sys 
import pygame

sys.path.append("../../utils")
import rgb

background_colour = pygame.Color(rgb.WHITE)
text_color = pygame.Color(rgb.BLACK)
highlight_color = pygame.Color(rgb.RED)


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
        screen.fill(rgb.BLACK)
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Hello Pygame!",
                                   True,
                                   rgb.IVORY)
        pygame.draw.rect(screen,
                         rgb.YELLOW,
                         (100, 100, 200, 150))
        pygame.draw.circle(screen,
                           rgb.HONEYDEW_4,
                           (400, 300), 
                           50)
        pygame.draw.polygon(screen,
                            rgb.DIM_GRAY,
                            [(600, 100),
                             (700,200),
                             (550, 20)])

        screen.blit(text_surface,
                    (300, 300))

        # flip the screen 
        
        pygame.display.flip()
    pygame.quit()

 
if __name__ == "__main__":
    main()
