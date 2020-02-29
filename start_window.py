import pygame
from settings import Settings as Stg
from pygame import Surface, Color
from main import main as game_start


def initialisation():
    pygame.init()
    pygame.font.init()

    font = pygame.font.SysFont('Comic Sans MS', 72)
    text = font.render('Press Enter to start the game"', False, (255, 255, 255))

    screen = pygame.display.set_mode(Stg.DISPLAY)
    pygame.display.set_caption("I wanna kill the Ryok")

    bg = Surface((Stg.WIN_WIDTH, Stg.WIN_HEIGHT))
    bg.fill(Color(255, 239, 213))
    
    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                game_start()

        screen.blit(bg, (0,0))
        screen.blit(text, (400 - text.get_width() // 2, 320 - text.get_height() // 2))
        pygame.display.update()
    
if __name__ == "__main__":
    initialisation()
