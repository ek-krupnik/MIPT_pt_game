

class Character(object):
    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(Character, cls).__new__(cls)

        return cls.instance

