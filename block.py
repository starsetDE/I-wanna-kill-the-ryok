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

class HitBox(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x ,y)
        self.image = Surface((1, 1))
        self.rect = Rect(x, y, 1, 1)

class Spikes(Platform):
    def __init__(self, x ,y):
        Platform.__init__(self,x ,y)
        self.image = image.load("sprites/ambience/spikes.png")
        self.rect = self.image.get_rect(topleft=(x, y))

class Ground(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x ,y)
        self.image = image.load("sprites/ambience/ground.png")
