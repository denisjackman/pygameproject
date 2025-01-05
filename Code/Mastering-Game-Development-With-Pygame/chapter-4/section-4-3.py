''' section 4.3 '''
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
    box1 = pygame.Rect(300, 300, 50, 50)
    box2 = pygame.Rect(350, 350, 50, 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
        # game logic goes here 
        if box1.colliderect(box2):
            print("collision detected")        
        # drawing logic goes here
        # clear the screen
        screen.fill(rgb.BLACK)

        pygame.draw.rect(screen, rgb.RED, box1)
        pygame.draw.rect(screen, rgb.SPRING_GREEN, box2)
        # flip the screen        
        pygame.display.flip()

    pygame.quit()

 
if __name__ == "__main__":
    main()
