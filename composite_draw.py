from macros import *
from graphics import*


class ImageLayer(object):

    def __init__(self):
        self._children = []

    def add(self, new_object):
        if not new_object in self._children:
            self._children.append(new_object)

    def remove(self, old_object):
        index = self._children.index(old_object)
        del self._children[index]

    def draw(self, surface):
        for lay in self._children:
            lay.draw(surface)


class ImageOfObject(object):

    def __init__(self, new_object, x=0, y=0):
        self._object = new_object
        self._x = x
        self._y = y

    def draw(self, surface):
        draw_adapter = DrawAdapter()
        draw_adapter.draw_object(surface, self._object, self._x, self._y)


def draw_new_step(surface, time):

    new_frame = ImageLayer()

    new_background = Window()
    new_back = ImageOfObject(new_background)
    new_frame.add(new_back)

    new_line = Lines()
    new_art_line = ImageOfObject(new_line)
    new_frame.add(new_art_line)

    # checking if need to change character coordinates
    # updating of coordinates
    # creation of new random asteroids
    # creation of exact space_ships (in depends on time - green/yellow/red)

    character = Character()
    new_image = ImageOfObject(character, 100, 100)

    bullet = Bullet(200, 200, "up")
    new_bullet = ImageOfObject(bullet, 300, 200)

    second_lay = ImageLayer()
    second_lay.add(new_image)
    second_lay.add(new_bullet)

    new_frame.add(second_lay)

    new_frame.draw(surface)
