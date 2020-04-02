from abc import abstractmethod


class Ship(object):

    def __init__(self):
        setattr(self, "army", 0)
        setattr(self, "color", "none")
        setattr(self, "weapon", False)

    def set_army(self, data):
        self.army = data

    def set_color(self, data):
        self.color = data

    def set_weapon(self, data):
        self.weapon = data


class ShipBuilder(object):

    @abstractmethod
    def create():
        pass


class ShipBuilderA(ShipBuilder):

    def create() -> Ship:
        product = Ship()
        product.set_army(100)
        product.set_color("green")
        return product


class ShipBuilderB(ShipBuilder):

    def create() -> Ship:
        product = Ship()
        product.set_army(200)
        product.set_army("yellow")

        return product


class ShipBuilderC(ShipBuilder):

    def create() -> Ship:
        product = Ship()
        product.set_army(200)
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

# def main():
#     my_own_factory = Shipyard()
#     ship_a = my_own_factory.construct_ship("B")
#     print ("army = ", ship_a.army)
#     print ("color = ", ship_a.color)
#     print ("weapon = ", ship_a.weapon)
#
# if __name__ == "__main__":
#     main()