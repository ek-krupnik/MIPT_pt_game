from macros import *


class Bullet(object):

    def __init__(self, x, y, direction):
        self._x = x
        self._y = y
        self._speed = BULLET_SPEED
        self._direction = direction
