''' section 6.1 '''
import sys 
import pygame
from OpenGL.GL import * 
from OpenGL.GL.shaders import compileProgram
from OpenGL.GL.shaders import compileShader

sys.path.append("../../utils")
import rgb
import djpg


def main():
    ''' Main Function'''
    # initialise pygame
    pygame.init()
    # create a game window 
    screen = pygame.display.set_mode((800, 600))
    # set the game running flag to true
    running = True
    
    vertex_shader_source = """
    #version 330 core 
    layout (location = 0) in vec2 position;
    void main()
    {
        gl_Position = vec4(postion.x, position.y, 0.0, 1.0);
    }
    """
    fragment_shader_source = """
    #version 330 core
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(1.0, 0.0, 0.0, 1.0); // red color
    }
    """
    vertex_shader = compileShader(vertex_shader_source, GL_VERTEX_SHADER)
    fragment_shader = compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)
    shader_program = compileProgram(vertex_shader, fragment_shader)

    # run the game loop
    while running:
        # check for user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # handle window close event 
                running = False
        glUseProgram(shader_program)
        # drawing logic goes here

        # clear the screen

        # flip the screen        
        pygame.display.flip()
    # close pygame
    pygame.quit()

 
if __name__ == "__main__":
    main()
