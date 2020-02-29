class Settings():

    # Настройки для экрана
    WIN_WIDTH = 800                     # Width for window
    WIN_HEIGHT = 640                    # Height for window
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)   # height and Width for all window
    BACKGROUND_COLOR = "#D2B48C"        # Color for background(if not Background image)

    # настройки для платформ
    PLATFORM_WIDTH = 32                 # Witdh for platform
    PLATFORM_HEIGHT = 32                # Height for platform
    PLATFORM_COLOR = "#FF6262"          # Color for platform(if not Platform image)

    # настройки персонажа
    MOVE_SPEED = 3                      # Moving speed
    WIDTH = 24                          # Width for Hero
    HEIGHT = 32                         # Height for Hero
    COLOR =  "#888888"                  # Color for Hero(if not Hero image)
    JUMP_POWER = 10                     # Jump length too
    GRAVITY = 0.5                       # Power for Gravitation

    # настройки анимаци
    ANIMATION_DELAY = 20                                           # Speed changing animation per Second.
    ANIMATION_RIGHT = [('sprites/player/hero.png'),
                       ('sprites/player/hero2.png'),
                       ('sprites/player/hero3.png'),
                       ('sprites/player/hero4.png')]                # Animation for moving right
    ANIMATION_LEFT = [('sprites/player/herol.png'),
                      ('sprites/player/hero2l.png'),
                      ('sprites/player/hero3l.png'),
                      ('sprites/player/hero4l.png')]                # Animation for moving left
    ANIMATION_JUMP_LEFT = [('sprites/player/hero_jumpl.png', 1)]    # Animation for moving left with jump
    ANIMATION_JUMP_RIGHT = [('sprites/player/hero_jump.png', 1)]    # Animation for moving right with jump
    ANIMATION_JUMP = [('sprites/player/hero.png', 1)]               # Jump animation
    ANIMATION_STAY = [('sprites/player/hero.png', 1)]               # Standing animation
