from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_cube():
    # Vertices defined for a unit cube centered at origin
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1),
    )

    # Faces defined using vertex indices
    faces = (
        (0, 1, 2, 3),  # Back
        (4, 5, 1, 0),  # Right
        (7, 6, 4, 5),  # Front
        (2, 3, 6, 7),  # Left
        (1, 5, 7, 2),  # Top
        (4, 0, 3, 6),  # Bottom
    )

    glColor3f(0.8, 0.8, 1.0)  # Light blue color for faces
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(
                vertices[vertex]
            )  # Use sets of four vertices to construct each cube face
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
    draw_grid()  # Draw the grid on the floor

    glPushMatrix()  # Save the current matrix state
    glTranslate(*character.position)
    draw_cube()
    glPopMatrix()  # Restore the previous matrix state
