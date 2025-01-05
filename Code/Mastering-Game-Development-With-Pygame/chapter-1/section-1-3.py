''' section 1.3 '''
import pygame 


def update_game_state():
    ''' game logic goes here '''
    debug = False
    lives = 3
    if debug:
        print(lives)


def draw_game_screen():
    ''' draw the game screen '''
    debug = False
    if debug:
        print("drawing the screen")


def keyboard_event():
    ''' keyboard pressed '''
    print("keyboard key pressed")


def mouse_event():
    ''' Mouse used'''
    print("Mouse used")


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
            elif event.type == pygame.KEYDOWN:
                # handle a key press
                if event.key == pygame.K_SPACE:
                    keyboard_event()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # handle a mouse button event 
                if event.button == 1:
                    # handle a mouse button press 
                    mouse_event()
        # game logic goes here 
        update_game_state()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print("going left")
        if keys[pygame.K_RIGHT]:
            print("going right")
        # drawing logic goes here
        draw_game_screen()
        # flip the screen 
        pygame.display.flip()
    pygame.quit()

 
if __name__ == "__main__":
    main()
