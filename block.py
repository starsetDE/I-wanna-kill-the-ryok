from pygame import *
from settings import Settings as Stg


class Platform(sprite.Sprite):

	def __init__(self, x, y):
		sprite.Sprite.__init__(self)
		self.image = Surface((Stg.PLATFORM_WIDTH,
							  Stg.PLATFORM_HEIGHT))

		self.image = image.load("sprites/ambience/platformsprite.png")
		self.rect = Rect(x, 
						 y,
						 Stg.PLATFORM_WIDTH,
						 Stg.PLATFORM_HEIGHT)