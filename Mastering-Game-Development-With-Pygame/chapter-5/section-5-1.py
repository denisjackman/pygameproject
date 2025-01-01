''' section 1.3 '''
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
    font = pygame.font.Font(None, 36)
    game_over = False
    score = 0 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
            
        # game logic goes here 
        if not game_over:
            score += 10 
            if score >= 100:
                game_over = True

        # drawing logic goes here
        # clear the screen
        screen.fill(rgb.BLACK)

        if game_over:
            text = font.render('Game Over!', True, rgb.RED)
            score_text = font.render(f'Score: {score}', True, rgb.WHITE)
            screen.blit(text, (350, 250))
            screen.blit(score_text, (370, 300))
        else:
            score_text = font.render(f'Score: {score}', True, rgb.WHITE)
            screen.blit(score_text, (10, 10))

        # flip the screen        
        pygame.display.flip()

    pygame.quit()

 
if __name__ == "__main__":
    main()
