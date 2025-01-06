''' chapter-3-7 '''
import sys
import pygame

sys.path.append("../../utils")
import rgb


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("resources/shortbeep.mp3")
    time = pygame.time
    # create a game window 
    HelloWorldColors = [rgb.BLACK, rgb.RED]
    screen = pygame.display.set_mode((320, 240))
    font = pygame.font.Font(None, 32)
    # set the game running flag to true
    running = True
    count = 0 
    oneSecondMarkReached = False
    lastTime = 0
    mouse_pos = None
    # run the game loop
    while running:
        # clear the screen
        screen.fill(rgb.WHITE)
        if oneSecondMarkReached:
            count += 1
        # check for user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

        # game logic goes here 
        text = font.render("Hello World", True, HelloWorldColors[count % 2])
        pygame.time.delay(1000)
        sx = int((screen.get_width() - text.get_width())/2 - 10)
        sy = int((screen.get_height() - text.get_height())/2 - 10 )
        tx = int((screen.get_width() - text.get_width())/2)
        ty = int((screen.get_height() - text.get_height())/2)
        tw = text.get_width() + 20
        th = text.get_height() + 20
        if mouse_pos != None:
            px = mouse_pos[0] - 16
            py = mouse_pos[1] - 16 
        else:
            px = screen.get_width()/2 - 16
            py = (screen.get_height()- text.get_height())/2 - 60


        # drawing logic goes here
        screen.blit(pygame.image.load("resources/smiley.png"),
                    (px, py))

        pygame.draw.rect(screen,
                         rgb.BLACK,
                         (sx, sy, tw, th))
        screen.blit(text,
                    (tx, ty))
        if oneSecondMarkReached:
            # play the sound 
            pygame.mixer.music.play()
        
        # flip the screen        
        pygame.display.flip()
        oneSecondMarkReached = False
        currentTime = time.get_ticks()
        if currentTime - lastTime > 1000:
            lastTime = currentTime
            oneSecondMarkReached = True
    # close pygame
    pygame.quit()

 
if __name__ == "__main__":
    main()
