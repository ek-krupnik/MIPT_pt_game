import character
import space_ships
import asteroid

def main():

    print ("Test Signleton : \n")

    my_first_character = character.Character();
    my_second_character = character.Character();
    print ("first id = {}".format(id(my_first_character)))
    print ("second id = {}".format(id(my_second_character)))
    print ("\n")

    print ("Test builder : ")

    my_own_factory = space_ships.Shipyard()             # director
    ship_a = my_own_factory.construct_ship("B")
    print ("health = ", ship_a.health)
    print ("color = ", ship_a.color)
    print ("weapon = ", ship_a.weapon)
    print ("\n")

    print ("Test factory : ")

    small_factory = asteroid.SmallAsteroidFactory()
    my_little_asteroid = small_factory.create()         # object of SmallAsteroid
    print (my_little_asteroid.size)


if __name__ == "__main__":
    main()