from macros import *


class Bullet(object):

    def __init__(self, direction, hit=0):
        # self._x = x
        # self._y = y
        self._speed = BULLET_MIDDLE_SPEED
        self._direction = direction         # up / down
        self._hit = hit
