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
    def draw_object(surface, object_to_draw, x=0, y=0):

        painter = ConcretePainter()

        if isinstance(object_to_draw, SmallAsteroid) or isinstance(object_to_draw, BigAsteroid):
            asteroid_to_draw = object_to_draw
            painter.draw_asteroid(surface, asteroid_to_draw._size, x, y)

        if isinstance(object_to_draw, Character):
            painter.draw_character(surface, x)

        if isinstance(object_to_draw, Bullet):
            painter.draw_bullet(surface, x, y)

        if isinstance(object_to_draw, Ship):
            ship_to_draw = object_to_draw
            painter.draw_ship(surface, ship_to_draw._color, x, y)

        if isinstance(object_to_draw, Window):
            painter.draw_window(surface, object_to_draw._color)

        if isinstance(object_to_draw, Lines):
            painter.cdraw_lines(surface, object_to_draw._color, object_to_draw._width)


class ConcretePainter(object):

    @staticmethod
    def draw_window(surface, color):
        surface.fill(color)

    @staticmethod
    def draw_character(surface, x):
        if x == MIDDLE_X:
            pygame.draw.polygon(surface, YELLOW, CHARACTER_MID_COORD, OBJECTS_WIDTH)
        elif x == LEFT_X:
            pygame.draw.polygon(surface, YELLOW, CHARACTER_LEFT_COORD, OBJECTS_WIDTH)
        else:
            pygame.draw.polygon(surface, YELLOW, CHARACTER_RIGHT_COORD, OBJECTS_WIDTH)

    @staticmethod
    def draw_lines(surface, color, width):
        pygame.draw.line(surface, color, [WIN_WIDTH / 3, WIN_HEIGHT], [WIN_WIDTH / 3, 0], width)
        pygame.draw.line(surface, color, [WIN_WIDTH / 3 * 2, WIN_HEIGHT], [WIN_WIDTH / 3 * 2, 0], width)

    @staticmethod
    def draw_asteroid(surface, size, center_x, center_y):
        if size == "small":
            radius = SMALL_ASTEROID_RADIUS
        else:
            radius = BIG_ASTEROID_RADIUS
        pygame.draw.circle(surface, LIGHT_BLUE, (center_x, center_y), radius)

    @staticmethod
    def draw_bullet(surface, x, y):
        pygame.draw.line(surface, RED, [x, y], [x, y + BULLET_LEN], OBJECTS_WIDTH)

    @staticmethod
    def draw_ship(surface, color, x, y):
        if color == "red":
            color_to_draw = DARK_RED
        elif color == "green":
            color_to_draw = GREEN
        else:
            color_to_draw = DARK_YELLOW

        pygame.draw.rect(surface, color_to_draw, (x, y, SHIP_WIDTH, SHIP_LEN))
