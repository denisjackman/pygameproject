''' section 2.1 Joystick '''
import pygame 


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    pygame.joystick.init()
    # create a game window 
    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    screen = pygame.display.set_mode((800, 600))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    print("Button 0 pressed")
                else:
                    print(f"{event.button} pressed ")
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    print(f"X-Axis montion: {event.value}")
        # game logic goes here 

        # drawing logic goes here
  
        # flip the screen 
        
        pygame.display.flip()
    pygame.quit()

 
if __name__ == "__main__":
    main()
