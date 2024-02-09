# PyCubeMove3D

This Python application demonstrates basic 3D graphics programming by allowing a user to move a cube in a three-dimensional plane using the WASD keys. It utilizes the Pygame library for creating the application window and handling keyboard inputs, and PyOpenGL for rendering 3D graphics. This project serves as a foundational example for those interested in exploring 3D graphics programming in Python.

## Features

- Movement of a cube in 3D space using keyboard inputs (WASD keys).
- Real-time 3D rendering with basic lighting.
- Example of using Pygame and PyOpenGL together in a Python application.

## Prerequisites

Before you can run this application, you need to have Python installed on your machine. This project was developed with Python 3.8, but it should be compatible with other versions of Python 3. Additionally, you'll need to install the following libraries:

 - Pygame: For creating the window and handling events.
 - PyOpenGL: For rendering 3D graphics.

You can install these libraries using pip:

'''bash
pip install pygame PyOpenGL
'''

## Installation

Clone the repository to your local machine:

'''bash
git clone https://github.com/russellmsilva/PyCubeMove3D.git
'''

Navigate to the cloned repository directory:

'''bash
cd PyCubeMove3D
'''

Clone the repository to your local machine:

'''bash
git clone https://github.com/russellmsilva/PyCubeMove3D.git
'''

Navigate to the cloned repository directory:
'''bash
cd PyCubeMove3D
'''

## Running the Application:

To run the application, execute the main.py file:

'''bash
python main.py
'''

## How It Works

### Main File (main.py)

Serves as the entry point of the application. It initializes the game, creates a window, and contains the main game loop where the cube's movement is updated, and the scene is rendered.

### Game Object (gameObject.py)

Defines a GameObject class representing each game object (such as the cube) as an instance.

### Input Handler (inputHandler.py)

Handles keyboard inputs (WASD keys) to move the cube in the 3D space.

### Renderer (renderer.py)

Manages the rendering of the 3D environment and the cube.

## Libraries Used

    Pygame: For creating the game window and handling user inputs.
    PyOpenGL: For 3D rendering of the cube and the environment.

## Contributing

While I have developed PyCubeMove3D as a foundational project to explore 3D graphics programming with Python, Pygame, and PyOpenGL, I currently do not plan to make further changes or actively review contributions to this repository. The project is provided as-is for educational purposes, and I encourage others to fork and extend the project in their own repositories.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
