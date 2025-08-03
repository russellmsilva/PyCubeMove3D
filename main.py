import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from gameObject import GameObject
from inputHandler import handle_input
from renderer import render_scene


# This function enables OpenGL lighting and sets the light position and color.
# It is called once during the setup phase of the application.
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
    pygame.display.gl_set_attribute(
        pygame.GL_MULTISAMPLESAMPLES, 16
    )  # Or higher for more samples

    # Create display with double buffering and OpenGL support
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_MULTISAMPLE)

    # Set up lighting (this is called only once)
    setup_lighting()
    glEnable(GL_COLOR_MATERIAL)  # Enable color material to use glColor for lighting
    glColorMaterial(
        GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE
    )  # Set material properties

    character = GameObject()

    clock = pygame.time.Clock()

    pygame.display.set_caption("3D Cube Movement")

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # The camera is positioned above the character and looks down at it.
        camera_position = [
            character.position[0],
            character.position[1] + 6,
            character.position[2] + 15,
        ]
        look_at = [
            character.position[0],
            character.position[1],
            character.position[2],
        ]
        up_vector = [0, 1, 0]  # Up vector for the camera

        # Clear the screen and set the background color
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background to white
        glLoadIdentity()
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

        # Set the camera position and orientation
        gluLookAt(
            camera_position[0],
            camera_position[1],
            camera_position[2],
            look_at[0],
            look_at[1],
            look_at[2],
            up_vector[0],
            up_vector[1],
            up_vector[2],
        )

        handle_input(character)  # Handle input to move the character
        render_scene(character)  # Render the scene with the character

        pygame.display.flip()  # Swap the buffers to display the rendered frame
        clock.tick(60)  # Limit the frame rate to 60 FPS


if __name__ == "__main__":
    main()
