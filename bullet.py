from macros import *


class Bullet(object):

    def __init__(self, direction, hit=0):
        self.speed = BULLET_MIDDLE_SPEED
        self.direction = direction         # up / down
        self.hit = hit

