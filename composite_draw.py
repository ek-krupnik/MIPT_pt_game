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
        self.object = new_object
        self.x = x
        self.y = y

    def draw(self, image_dict):
        draw_adapter = DrawAdapter()
        draw_adapter.draw_object(image_dict, self.object, self.x, self.y)


class Painter(object):

    @staticmethod
    def draw_new_step(image_dict, list_objects, list_bullets):

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

        if state == "GAME OVER : health" or state == "GAME OVER : broken":
            print(state)
            return "Game over"

        for image in list_objects:
            old_object = image.object
            if isinstance(old_object, Character):
                first_lay.add(image)
            elif isinstance(old_object, Bullet):
                third_lay.add(image)
            else:
                second_lay.add(image)

        new_frame.add(new_back)
        new_frame.add(first_lay)
        new_frame.add(second_lay)
        new_frame.add(third_lay)
        new_frame.draw(image_dict)

        return [list_objects, list_bullets]
