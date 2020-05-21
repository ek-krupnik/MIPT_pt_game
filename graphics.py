import pygame

from asteroid import *
from bullet import *
from character import *
from space_ships import *
from background_elements import *


class DrawAdapter(object):

    def __init__(self):
        # self._object = new_object
        pass

    @staticmethod
    def draw_object(image_dict, object_to_draw, x=0, y=0):

        painter = ConcretePainter()
        surface = image_dict['surface']

        if isinstance(object_to_draw, SmallAsteroid):
            first_asteroid_image = image_dict['first_asteroid_image']
            painter.draw_asteroid(surface, first_asteroid_image, x - SMALL_SIZE[0] / 2, y - SMALL_SIZE[1] / 2)

        if isinstance(object_to_draw, BigAsteroid):
            second_asteroid_image = image_dict['second_asteroid_image']
            painter.draw_asteroid(surface, second_asteroid_image, x - BIG_SIZE[0] / 2, y - BIG_SIZE[1] / 2)

        if isinstance(object_to_draw, Character):
            character_image = image_dict['character_image']
            painter.draw_character(surface, character_image, x)

        if isinstance(object_to_draw, Bullet):
            painter.draw_bullet(surface, x, y)

        if isinstance(object_to_draw, Ship):
            ship_to_draw = object_to_draw
            painter.draw_ship(surface, image_dict, ship_to_draw._color, x, y)

        if isinstance(object_to_draw, Window):
            image_space = image_dict['space_image']
            painter.draw_window(surface, image_space)

        if isinstance(object_to_draw, Lines):
            painter.draw_lines(surface, object_to_draw._color, object_to_draw._width)


class ConcretePainter(object):

    @staticmethod
    def draw_window(surface, space_image):
        surface.blit(space_image, START_COORD)

    @staticmethod
    def draw_character(surface, character_image, x):
        if x == MIDDLE_X:
            surface.blit(character_image, (MIDDLE_X - BIG_SIZE[0] / 2, DOWN_Y - BIG_SIZE[1] / 2))
        elif x == LEFT_X:
            surface.blit(character_image, (LEFT_X - BIG_SIZE[0] / 2, DOWN_Y - BIG_SIZE[1] / 2))
        else:
            surface.blit(character_image, (RIGHT_X - BIG_SIZE[0] / 2, DOWN_Y - BIG_SIZE[1] / 2))

    @staticmethod
    def draw_lines(surface, color, width):
        pygame.draw.line(surface, color, [WIN_WIDTH / 3, WIN_HEIGHT], [WIN_WIDTH / 3, 0], width)
        pygame.draw.line(surface, color, [WIN_WIDTH / 3 * 2, WIN_HEIGHT], [WIN_WIDTH / 3 * 2, 0], width)

    @staticmethod
    def draw_asteroid(surface, asteroid_image, center_x, center_y):
        surface.blit(asteroid_image, (int(center_x), int(center_y)))

    @staticmethod
    def draw_bullet(surface, x, y):
        pygame.draw.line(surface, RED, [x, y], [x, y + BULLET_LEN], OBJECTS_WIDTH)

    @staticmethod
    def draw_ship(surface, image_dict, color, x, y):
        if color == "red":
            ship_image = image_dict['red_ship']
        elif color == "green":
            ship_image = image_dict['green_ship']
        else:
            ship_image = image_dict['yellow_ship']

        surface.blit(ship_image, (x - MIDDLE_SIZE[0] / 2, y - MIDDLE_SIZE[1] / 2))
