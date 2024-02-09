class GameObject:
    def __init__(self):
        self.position = [0, 0, 0]

    def move(self, dx, dy, dz):
        self.position[0] += dx
        self.position[1] += dy
        self.position[2] += dz
