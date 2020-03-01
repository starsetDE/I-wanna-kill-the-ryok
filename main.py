import pygame
from pygame import Surface, Color
from player import Player
from settings import Settings as Stg
from levels import *
from camera import Camera, camera_configure
import time
from level_reader import level_reader

def main():
    pygame.init()                                   # Initialization pygame
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/game_music.mp3")
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode(Stg.DISPLAY)   # Creating new window
    pygame.display.set_caption("I wanna kill the Ryok")

    # bg = Surface((Stg.WIN_WIDTH,Stg.WIN_HEIGHT))  # Creating background
    # bg.fill(Color(Stg.BACKGROUND_COLOR))          # Filling background only color


    # Loading image for background and creating background
    bg = pygame.image.load("sprites/ambience/background8x6.png")

    hero = Player(48, 48)                           # Initialization Hero
    left = right = False                            # If not press key <- o ->
    up = False                                      # If not press key up_arrow

    entities = pygame.sprite.Group()                # Here find all entities(platform and other)

    platforms = []                                  # All Platforms append here

    entities.add(hero)                              # Adding Hero

    timer = pygame.time.Clock()                     # Timer for Frame Per Second

    x=y=0                                           # Coordinates for Hero

    level_reader(level, x ,y, entities, platforms)  # Creating level

    total_level_witdh = len(level[0])*Stg.PLATFORM_WIDTH

    total_level_height = len(level)*Stg.PLATFORM_HEIGHT

    camera = Camera(camera_configure,
                    total_level_witdh,
                    total_level_height)

    while 1:                                        # General loop for programm
        timer.tick(60)
        for e in pygame.event.get():                # Event handling
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
               left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
               right = True

            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
               right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False

        screen.blit(bg, (0,0))                      # Each iteration print background
        camera.update(hero)                         # Change camera position from character
        hero.update(left, right, up, platforms)     # Handling event for Hero

        for e in entities:
            screen.blit(e.image, camera.apply(e))   # Print each element for entities
        pygame.display.update()                     # Flashing and displaying all changes to the screen
        

if __name__ == "__main__":
    main()
