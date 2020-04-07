

class Character(object):
    def __new__(cls):

        if not hasattr(cls, '_instance'):
            cls._instance = super(Character, cls).__new__(cls)

        return cls._instance
