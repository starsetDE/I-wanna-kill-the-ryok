import pygame
from pygame import *
from player import Player
from block import Platform
from settings import Settings as Stg
from levels import *

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+Stg.WIN_WIDTH / 2, -t+Stg.WIN_HEIGHT / 2

    l - min (0, 1)
    l = max(-(camera.width-Stg.WIN_WIDTH), 1)
    t = max(-(camera.height-Stg.WIN_HEIGHT), t)
    t = min(0, t)

    return Rect(l, t, w, h)

def main():
    pygame.init()                                   # Initialization pygame
    screen = pygame.display.set_mode(Stg.DISPLAY)   # Creating new window
    pygame.display.set_caption("I wanna kill the Ryok")
    bg = Surface((Stg.WIN_WIDTH,Stg.WIN_HEIGHT))    # Creating Background
    bg.fill(Color(Stg.BACKGROUND_COLOR))            # Filling background only color

    hero = Player(55, 55)                           # Initialization Hero
    left = right = False                            # If not press key <- o ->
    up = False                                      # If not press key up_arrow

    entities = pygame.sprite.Group()                # Here find all entities(platform and other)

    platforms = []                                  # All Platforms append here

    entities.add(hero)                              # Adding Hero

    timer = pygame.time.Clock()                     # Timer for Frame Per Second

    x=y=0                                           # Coordinates for Hero

    for row in level:                               # All string in level(level find in levels)
        for col in row:                             # Each symbol
            if col == "-":
                #Creating platforms, filling color and printing
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
                    
            x += Stg.PLATFORM_WIDTH                  # For each block creating platform
        y += Stg.PLATFORM_HEIGHT                     # Same, but HEIGHT
        x = 0         

    total_level_witdh = len(level[0])*Stg.PLATFORM_WIDTH

    total_level_height = len(level)*Stg.PLATFORM_HEIGHT

    camera = Camera(camera_configure,
                    total_level_witdh,
                    total_level_height)

    while 1:                                        # General loop for programm
        timer.tick(60)
        for e in pygame.event.get():                # Event handling
            if e.type == QUIT:
                exit()
            if e.type == KEYDOWN and e.key == K_LEFT:
               left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
               right = True

            if e.type == KEYUP and e.key == K_RIGHT:
               right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False

        screen.blit(bg, (0,0))                      # Each iteration print background
        hero.update(left, right, up, platforms)     # Handling event for Hero
        camera.update(hero)                         # Change camera position from character

        for e in entities:
            screen.blit(e.image, camera.apply(e))   # Print each element for entities
        pygame.display.update()                     # Flashing and displaying all changes to the screen
        

if __name__ == "__main__":
    main()