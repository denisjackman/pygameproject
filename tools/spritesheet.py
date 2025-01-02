''' section 6.3'''
import sys 
import pygame
import random

sys.path.append("../utils")
import rgb
import djpg

SPRITESHEET = "../assets/trixiefull.png"
WIDTH = 800
HEIGHT = 600
SPRITE_WIDTH = 96 
SPRITE_HEIGHT = 96 


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    # create a game window 
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("SpritSheet Checker")
    frame_count = 0
    # set the game running flag to true
    running = True
    frames = djpg.load_sprite_sheet(SPRITESHEET, SPRITE_WIDTH, SPRITE_HEIGHT)
    font = pygame.font.Font(None, 25)
    clock = pygame.time.Clock()

    # run the game loop
    while running:
        # check for user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    frame_count += 1
                    if frame_count > len(frames) -1 :
                        frame_count = len(frames)
                elif event.key == pygame.K_DOWN:
                    frame_count -= 1
                    if frame_count < 0:
                        frame_count = 0
        # drawing logic goes here
        # clear the screen
        screen.fill(rgb.BLACK)
        text_surface = font.render(f"{frame_count} ({len(frames)})", True, rgb.WHITE)
        screen.blit(text_surface, (50, 10))
        screen.blit(frames[frame_count], (15, 40))

        # flip the screen        
        pygame.display.flip()
    # close pygame
    pygame.quit()

 
if __name__ == "__main__":
    main()
