import unittest
import character
import space_ships
import asteroid

class TestCharacter(unittest.TestCase):

    def test_character_singularity(self):
        first_character = character.Character();
        second_character = character.Character();
        self.assertEqual(id(first_character), id(second_character),
                         "Different id of main character")

class TestAsteroid(unittest.TestCase):

    def test_creation_small(self):
        small_factory = asteroid.SmallAsteroidFactory()
        small_asteroid = small_factory.create()
        self.assertEqual(small_asteroid._size, "small",
                         "Incorrect size after creating a small asteroid")

    def test_creation_big(self):
        big_factory = asteroid.BigAsteroidFactory()
        big_asteroid = big_factory.create()
        self.assertEqual(big_asteroid._size, "big",
                         "Incorrect size after creating a big asteroid")

class TestSpaceShip(unittest.TestCase):

    def setUp(self):
        self.director = space_ships.Shipyard()

    def test_a_ship(self):
        ship_a = self.director.construct_ship("A")
        self.assertEqual(ship_a._weapon, False,
                         "Incorrect weapon after creating a A ship")
        self.assertEqual(ship_a._color, "green",
                         "Incorrect color after creating a A ship")
        self.assertEqual(ship_a._health, 100,
                         "Incorrect health after creating a A ship")

    def test_b_ship(self):
        ship_b = self.director.construct_ship("B")
        self.assertEqual(ship_b._weapon, False,
                         "Incorrect weapon after creating a B ship")
        self.assertEqual(ship_b._color, "yellow",
                         "Incorrect color after creating a B ship")
        self.assertEqual(ship_b._health, 200,
                         "Incorrect health after creating a B ship")

    def test_c_ship(self):
        ship_c = self.director.construct_ship("C")
        self.assertEqual(ship_c._weapon, True,
                         "Incorrect weapon after creating a C ship")
        self.assertEqual(ship_c._color, "red",
                         "Incorrect color after creating a C ship")
        self.assertEqual(ship_c._health, 200,
                         "Incorrect health after creating a C ship")

if __name__ == '__main__':
    unittest.main()