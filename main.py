import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from gameObject import GameObject
from inputHandler import handle_input
from renderer import render_scene

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 1, 2, 0])  # Positional light
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])  # Ambient light color

def main():
    pygame.init()
    display = (800, 600)
    
    # Request multisample antialiasing
    pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
    pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 16)  # Or higher for more samples

    # Create display with double buffering and OpenGL support
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    glEnable(GL_MULTISAMPLE)

    # Call this function once in your setup
    setup_lighting()

    character = GameObject()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  

        # Update camera position
        camera_position = [character.position[0], character.position[1] + 6, character.position[2] + 15]
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background to white
        glLoadIdentity()
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
        gluLookAt(camera_position[0], camera_position[1], camera_position[2],  # Camera position
                  character.position[0], character.position[1], character.position[2],  # Look at point
                  0, 1, 0)  # Up vector

        handle_input(character)
        render_scene(character)

        pygame.display.flip()
        clock.tick(60)
'''
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
    glEnable(GL_DEPTH_TEST)

    character = GameObject()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0, 5, -10, 0, 0, 0, 0, 1, 0)

        render_scene(character)

        pygame.display.flip()
        pygame.time.Clock().tick(60)
'''
if __name__ == "__main__":
    main()
