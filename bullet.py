from macros import *


class Bullet(object):

    def __init__(self, direction, x=0, y=0):
        self._x = x
        self._y = y
        self._speed = BULLET_SPEED
        self._direction = direction
