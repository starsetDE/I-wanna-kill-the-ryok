from pygame import sprite, image
from pygame import Surface, Rect
from settings import Settings as Stg


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((Stg.PLATFORM_WIDTH,
			      Stg.PLATFORM_HEIGHT))
        # for the class "Platform" image is optional
        # self.image = image.load("sprites/ambience/platform.png")
        self.rect = Rect(x, 
                         y,
                         Stg.PLATFORM_WIDTH,
                         Stg.PLATFORM_HEIGHT)

class Grass(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("sprites/ambience/grass.png")

class Spikes(Platform):
    def __init__(self, x ,y):
        Platform.__init__(self,x ,y)
        self.image = image.load("sprites/ambience/spikes.png")

class Ground(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x ,y)
        self.image = image.load("sprites/ambience/ground.png")
