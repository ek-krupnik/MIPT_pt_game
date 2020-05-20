from graphics import*
import game_step


class ImageLayer(object):

    def __init__(self):
        self._children = []

    def add(self, new_object):
        if not (new_object in self._children):
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


class Painter(object):

    @staticmethod
    def draw_new_step(surface, list_objects, list_bullets):

        new_frame = ImageLayer()

        first_lay = ImageLayer()
        second_lay = ImageLayer()
        third_lay = ImageLayer()

        new_background = Window()
        new_back = ImageOfObject(new_background)

        new_line = Lines()
        first_lay.add(ImageOfObject(new_line))
        state = game_step.get_state(list_objects, list_bullets)      # update lists of objects

        list_objects = state[0]
        list_bullets = state[1]

        if state == "GAME OVER":
            print(state)
            exit()

        for image in list_objects:
            old_object = image._object
            if isinstance(old_object, Character):
                first_lay.add(image)
            elif isinstance(old_object, Bullet):
                third_lay.add(image)
            else:
                second_lay.add(image)

        # checking if need to change character coordinates
        # updating of coordinates
        # creation of new random asteroids
        # creation of exact space_ships (in depends on time - green/yellow/red)

        # character = Character()
        # new_image = ImageOfObject(character, MIDDLE_X, DOWN_Y)  # as example

        # bullet = Bullet(200, 200, "up")                         # as example
        # new_bullet = ImageOfObject(bullet, 300, 200)            # as example

        # second_lay = ImageLayer()
        # second_lay.add(new_image)

        new_frame.add(new_back)
        new_frame.add(first_lay)
        new_frame.add(second_lay)
        new_frame.add(third_lay)
        new_frame.draw(surface)

        return [list_objects, list_bullets]
