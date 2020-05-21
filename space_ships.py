from macros import *
from abc import abstractmethod


class Ship(object):

    def __init__(self):
        setattr(self, "_health", 0)
        setattr(self, "_color", "none")
        setattr(self, "_weapon", False)
        setattr(self, "_bullet_speed", 0)
        setattr(self, "_bullet_hit", 0)

    def set_health(self, data):
        self._health = data

    def set_color(self, data):
        self._color = data

    def set_weapon(self, data):
        self._weapon = data

    def set_bullet_speed(self, data):
        self._bullet_speed = data

    def set_bullet_hit(self, data):
        self._bullet_hit = data

class ShipBuilder(object):

    @abstractmethod
    def create():
        pass


class ShipBuilderA(ShipBuilder):

    def create() -> Ship:
        product = Ship()
        product.set_health(100)
        product.set_color("green")
        product.set_weapon(True)
        product.set_bullet_hit(GREEN_BULLET_HIT)
        return product


class ShipBuilderB(ShipBuilder):

    def create() -> Ship:
        product = Ship()
        product.set_health(200)
        product.set_color("yellow")
        product.set_weapon(True)
        product.set_bullet_speed(LOW_SPEED)
        product.set_bullet_hit(YELLOW_BULLET_HIT)
        return product


class ShipBuilderC(ShipBuilder):

    def create() -> Ship:
        product = Ship()
        product.set_health(200)
        product.set_color("red")
        product.set_weapon(True)
        product.set_bullet_speed(HIGH_SPEED)
        product.set_bullet_hit(RED_BULLET_HIT)
        return product


class Shipyard(object):

    @staticmethod
    def construct_ship(ship_type) -> Ship:

        if ship_type == "A":
            builder = ShipBuilderA
            return builder.create()

        elif ship_type == "B":
            builder = ShipBuilderB
            return builder.create()

        elif ship_type == "C":
            builder = ShipBuilderC
            return builder.create()

        else:
            print ("Wrong type of ship")
