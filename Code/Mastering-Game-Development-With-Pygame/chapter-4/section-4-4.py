''' section 4.4 '''
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
    player_health = 100 
    font = pygame.font.Font(None, 36)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_health += 1
                elif event.key == pygame.K_DOWN:
                    player_health -= 1
        if player_health > 100:
            player_health = 100
        if player_health < 0:
            player_health = 0 
            
        # game logic goes here 
        # drawing logic goes here
        # clear the screen
        screen.fill(rgb.BLACK)
        text_surface = font.render(f'{player_health}', True, rgb.WHITE)
        screen.blit(text_surface, (50, 25))

        pygame.draw.rect(screen, rgb.RED, (50, 50, player_health, 20))
        # flip the screen        
        pygame.display.flip()

    pygame.quit()

 
if __name__ == "__main__":
    main()
