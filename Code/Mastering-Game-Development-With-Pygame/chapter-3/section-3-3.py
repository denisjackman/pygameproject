''' section 3.3 '''
import sys 
import pygame

sys.path.append("../../utils")
import rgb


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    # create a game window 
    screen = pygame.display.set_mode((800, 600))
    running = True
    font = pygame.font.Font('../../fonts/halfelven.ttf', 36)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
        # game logic goes here 
        screen.fill(rgb.BLACK)
        text_surface = font.render("Hello, Pygame!", True, rgb.WHITE)
        screen.blit(text_surface, (300, 300))
        # drawing logic goes here

        # flip the screen        
        pygame.display.flip()
    pygame.quit()

 
if __name__ == "__main__":
    main()
