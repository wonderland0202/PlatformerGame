import pygame.sprite

class menuButton():
    def __init__(self, x, y, width, height):
        super().__init__()

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.textPos = (self.width / 2, self.height / 2)
        self.textColour = (255, 255, 255)

        self.bgColour(255,255,255,)