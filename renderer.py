from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_cube():
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7)
    )

    glLineWidth(1.15)  # Set the line width to 2.0 pixels
    glColor3f(1, 1, 1)  # Set line color to white before glBegin

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

def draw_grid():
    grid_size = 10
    grid_step = 1
    glColor3f(0.5, 0.5, 0.5)  # Gray color for the grid lines

    # Draw horizontal lines
    for x in range(-grid_size, grid_size + 1, grid_step):
        glBegin(GL_LINES)
        glVertex3f(x, 0, -grid_size)
        glVertex3f(x, 0, grid_size)
        glEnd()

    # Draw vertical lines
    for z in range(-grid_size, grid_size + 1, grid_step):
        glBegin(GL_LINES)
        glVertex3f(-grid_size, 0, z)
        glVertex3f(grid_size, 0, z)
        glEnd()

def render_scene(character):
    #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    draw_grid()  # Draw the grid on the floor

    glPushMatrix()
    glTranslate(*character.position)
    draw_cube()
    glPopMatrix()

