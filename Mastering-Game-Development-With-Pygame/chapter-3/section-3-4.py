''' section 1.3 '''
import sys 
import pygame

sys.path.append("../../utils")
import rgb
import djpg


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    # create a game window 
    screen = pygame.display.set_mode((800, 600))
    running = True
    font = pygame.font.Font('../../fonts/halfelven.ttf', 36)
    clock = pygame.time.Clock()
    current_frame = 0 
    frame_rate = 30 
    frames = djpg.load_sprite_sheet('../../assets/trixiefull.png', 96, 96)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
        # game logic goes here 
        screen.fill(rgb.BLACK)
        screen.blit(frames[current_frame], (300, 300))
        current_frame = (current_frame + 1) % len(frames)
        
        # drawing logic goes here

        # flip the screen        
        pygame.display.flip()
        clock.tick(frame_rate)
    pygame.quit()

 
if __name__ == "__main__":
    main()
