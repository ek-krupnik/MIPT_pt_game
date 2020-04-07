from abc import abstractmethod


class Ship(object):

    def __init__(self):
        setattr(self, "_health", 0)
        setattr(self, "_color", "none")
        setattr(self, "_weapon", False)
    #     setattr(self, "_speed", 10)

    def set_health(self, data):
        self._health = data

    def set_color(self, data):
        self._color = data

    def set_weapon(self, data):
        self._weapon = data


class ShipBuilder(object):

    @abstractmethod
    def create():
        pass


class ShipBuilderA(ShipBuilder):

    def create() -> Ship:
        product = Ship()
        product.set_health(100)
        product.set_color("green")
        return product


class ShipBuilderB(ShipBuilder):

    def create() -> Ship:
        product = Ship()
        product.set_health(200)
        product.set_color("yellow")

        return product


class ShipBuilderC(ShipBuilder):

    def create() -> Ship:
        product = Ship()
        product.set_health(200)
        product.set_color("red")
        product.set_weapon(True)

        return product


class Shipyard(object):

    def construct_ship(self, ship_type) -> Ship:

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
