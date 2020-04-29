import pygame
from macros import *
from character import *
from space_ships import *
from asteroid import *
from bullet import *


class DrawAdapter(object):

    def __init__(self):
        # self._object = new_object
        pass

    @staticmethod
    def draw_object(object_to_draw, surface, x=0, y=0):

        if isinstance(object_to_draw, SmallAsteroid) or isinstance(object_to_draw, BigAsteroid):
            asteroid_to_draw = object_to_draw
            draw_asteroid(surface, asteroid_to_draw._size, x, y)

        if isinstance(object_to_draw, Character):
            draw_character(surface)

        if isinstance(object_to_draw, Bullet):
            draw_bullet(surface, x, y)

        if isinstance(object_to_draw, Ship):
            ship_to_draw = object_to_draw
            draw_ship(surface, ship_to_draw._color, x, y)


def draw_character(surface):
    pygame.draw.polygon(surface, YELLOW, CHARACTER_COORD, OBJECTS_WIDTH)


def draw_lines(surface):
    pygame.draw.line(surface, LIGHT_GRAY, [WIN_WIDTH / 3, WIN_HEIGHT], [WIN_WIDTH / 3, 0], LINE_WIDTH)
    pygame.draw.line(surface, LIGHT_GRAY, [WIN_WIDTH / 3 * 2, WIN_HEIGHT], [WIN_WIDTH / 3 * 2, 0], LINE_WIDTH)


def draw_asteroid(surface, size, center_x, center_y):
    if size == "small":
        radius = SMALL_ASTEROID_RADIUS
    else:
        radius = BIG_ASTEROID_RADIUS
    pygame.draw.circle(surface, LIGHT_BLUE, (center_x, center_y), radius)


def draw_bullet(surface, x, y):
    pygame.draw.line(surface, RED, [x, y], [x, y + BULLET_LEN], OBJECTS_WIDTH)


def draw_ship(surface, color, x, y):
    if color == "red":
        color_to_draw = DARK_RED
    elif color == "green":
        color_to_draw = GREEN
    else:
        color_to_draw = DARK_YELLOW

    pygame.draw.rect(surface, color_to_draw, (x, y, SHIP_WIDTH, SHIP_LEN))