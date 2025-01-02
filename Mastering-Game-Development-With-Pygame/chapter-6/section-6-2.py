''' section 6.2 '''
import sys 
import pygame
import random

sys.path.append("../../utils")
import rgb
import djpg

WIDTH = 800
HEIGHT = 600 
BACKGROUND_COLOR = rgb.BLACK
PARTICLE_COLOR = rgb.WHITE
PARTICLE_RADIUS = 2
NUM_PARTICLES = 100

pygame.init()
# create a game window 
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Particle System")

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = PARTICLE_RADIUS
        self.color = PARTICLE_COLOR
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-5,-1)

    def move(self):
        self.x += self.vx
        self.y += self.vy

            
    def draw(self):
        dx = int(self.x)
        dy = int(self.y)
        pygame.draw.circle(screen,
                           self.color,
                           (dx, dy),
                           self.radius)

def main():
    ''' Main Function'''
    # initialise pygame

    # set the game running flag to true
    running = True
    particles = [Particle(WIDTH // 2, HEIGHT) for _ in range(NUM_PARTICLES)]
    # run the game loop
    while running:
        # check for user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
        # drawing logic goes here
        # clear the screen
        screen.fill(BACKGROUND_COLOR)
        for particle in particles:
            particle.move()
            particle.draw()

        # flip the screen        
        pygame.display.flip()
    # close pygame
    pygame.quit()

 
if __name__ == "__main__":
    main()
