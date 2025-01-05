''' chapter-3-3 '''
import sys
import pygame

sys.path.append("../../utils")
import rgb


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    # create a game window 
    HelloWorldColors = [rgb.BLACK, rgb.RED]
    screen = pygame.display.set_mode((320, 240))
    font = pygame.font.Font(None, 32)
    # set the game running flag to true
    running = True
    count = 0 

    # run the game loop
    while running:
        # check for user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
        count += 1            
        # clear the screen
        screen.fill(rgb.WHITE)

        # game logic goes here 
        text = font.render("Hello World", True, HelloWorldColors[count % 2])
        pygame.time.delay(1000)
        screen.blit(text,
                    ((screen.get_width() - text.get_width())/2,
                     (screen.get_height() - text.get_height())/2))
        # drawing logic goes here


        # flip the screen        
        pygame.display.flip()
    # close pygame
    pygame.quit()

 
if __name__ == "__main__":
    main()
