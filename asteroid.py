
from abc import abstractmethod


class Asteroid(object):

    def __init__(self):
        setattr(self, "size", "none")
        # setattr()

    @abstractmethod
    def creation(self):
        # setattr(self, size, "none")
        # setattr(self, color, "none")
        pass

class SmallAsteroid(Asteroid):
    def creation(self):
        print("we created it!")
        self.size = "small"
        return self

class BigAsteroid(Asteroid):
    def creation(self):
        self.size = "big"
        return self


class AsteroidFactory(object):

    @abstractmethod
    def create(self):
        pass

class SmallAsteroidFactory(AsteroidFactory):
    def create(self) -> SmallAsteroid:
        return SmallAsteroid().creation()

class BigAsteroidFactory(AsteroidFactory):
    def create(self) -> BigAsteroid:
        return BigAsteroid().creation()

# def main():
#     small_factory = SmallAsteroidFactory()
#     my_little_asteroid = small_factory.create()         # object of SmallAsteroid
#     print(my_little_asteroid.size)
#
# if __name__ == "__main__":
#     main()