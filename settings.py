class Settings():

    # Настройки для экрана
    WIN_WIDTH = 800                     # Width for window
    WIN_HEIGHT = 640                    # Height for window
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)   # height and Width for all window
    BACKGROUND_COLOR = "#004400"        # Color for background(if not Background image)

    # настройки для платформ
    PLATFORM_WIDTH = 32                 # Witdh for platform
    PLATFORM_HEIGHT = 32                # Height for platform
    PLATFORM_COLOR = "#FF6262"          # Color for platform(if not Platform image)

    # настройки персонажа
    MOVE_SPEED = 5                      # Moving speed
    WIDTH = 22                          # Width for Hero
    HEIGHT = 32                         # Height for Hero
    COLOR =  "#888888"                  # Color for Hero(if not Hero image)
    JUMP_POWER = 10                     # Jump length too
    GRAVITY = 0.35                      # Power for Gravitation

    # настройки анимаци
    ANIMATION_DELAY = 1                                         # Speed changing animation per Second.
    ANIMATION_RIGHT = [('sprites/player/starset.png')]          # Animation for moving right
    ANIMATION_LEFT = [('sprites/player/starset.png')]           # Animation for moving left
    ANIMATION_JUMP_LEFT = [('sprites/player/starset.png', 1)]   # Animation for moving left with jump
    ANIMATION_JUMP_RIGHT = [('sprites/player/starset.png', 1)]  # Animation for moving right with jump
    ANIMATION_JUMP = [('sprites/player/starset.png', 1)]        # Jump animation
    ANIMATION_STAY = [('sprites/player/starset.png', 1)]        # Animation not moving