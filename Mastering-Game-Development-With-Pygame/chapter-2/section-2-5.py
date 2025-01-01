''' section 1.3 '''
import pygame 


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    # create a game window 
    screen = pygame.display.set_mode((800, 600))
    pygame.mixer.init()
    explosion = pygame.mixer.Sound("../../assets/Explosion.mp3")
    powerup = pygame.mixer.Sound("../../assets/powerup.mp3")
    pygame.mixer.music.load("../../assets/AroundtheWorld.ogg")
    pygame.mixer.music.play(-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    explosion.play()
                elif event.key == pygame.K_RETURN:
                    powerup.play()
                elif event.key == pygame.K_UP:
                    pygame.mixer.music.pause()
                elif event.key == pygame.K_DOWN:
                    pygame.mixer.music.unpause()
        # game logic goes here 
        screen.fill((0, 0, 0))
        # drawing logic goes here

        # flip the screen 
        
        pygame.display.flip()
    pygame.quit()

 
if __name__ == "__main__":
    main()
