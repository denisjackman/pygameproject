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

    # ball properties 
    ball_radius = 20
    ball_color = rgb.RED
    ball_position = [400, 300]
    ball_velocity = [5, 0]
    
    gravity = 0.5
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
        # game logic goes here 
        # clear the screen
        screen.fill(rgb.BLACK)

        # update the ball 
        ball_velocity[1] += gravity
        ball_position[0] += ball_velocity[0]
        ball_position[1] += ball_velocity[1]

        # bounce of the ground 
        if ball_position[1] + ball_radius >= 600:
            # bounce and lose energy 
            ball_velocity[1] *= -0.8

        # bouce off the walls
        if ball_position[0] - ball_radius <= 0 or ball_position[0] + ball_radius >= 800:
            # reverse the horizontal velocity
            ball_velocity[0] *= -1     
        # draw the ball 

        pygame.draw.circle(screen,
                           ball_color,
                           (int(ball_position[0]),
                            int(ball_position[1])),
                            ball_radius)     
        
        # drawing logic goes here
        if ball_position[0] + ball_radius >= 780:
            ball_position[0] = 0 
            ball_velocity = [5, 0]
        elif ball_position[0] - ball_radius <= 10:
            ball_position[0] = 800
            ball_velocity = [-5, 0]

        if ball_position[1] + ball_radius >= 580:
            ball_position[1] = 0 
            ball_velocity = [5, 0]
        elif ball_position[1] - ball_radius <= 10:
            ball_position[1] = 600
            ball_velocity = [-5, 0]

        # flip the screen        
        pygame.display.flip()

    pygame.quit()

 
if __name__ == "__main__":
    main()
