from pygame import *
from settings import Settings as Stg
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
