from macros import *


class Character(object):

    _bullet_speed = MIDDLE_SPEED
    health = CHARACTER_HEALTH

    def __new__(cls):

        if not hasattr(cls, '_instance'):
            cls._instance = super(Character, cls).__new__(cls)

        return cls._instance
