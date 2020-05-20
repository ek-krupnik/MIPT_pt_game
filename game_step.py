import composite_draw
from space_ships import *
from character import *
from asteroid import *
from bullet import *
from macros import *
import random


def dist(first_obj, second_obj):
    return abs(first_obj._y - second_obj._y) < EPS and abs(first_obj._x - second_obj._x) < EPS


def is_outside(object):
    return object._y > WIN_WIDTH + EPS or object._y < -EPS


def bullet_in_object(bullet_image, image):
    if isinstance(image._object, Bullet):
        return False
    bullet = bullet_image._object
    if dist(bullet_image, image) and not isinstance(image._object, Character) and bullet._direction == 'up':
        return True
    if dist(bullet_image, image) and not isinstance(image._object, Ship) and bullet._direction == 'down':
        return True
    return False


def bullet_hit_character(list_bullets, image):
    summary_hit = 0
    for bullet_image in list_bullets:
        bullet = bullet_image._object
        if bullet._direction == 'down' and dist(image, bullet_image):
            summary_hit += bullet._hit
    return summary_hit


# returns lists = [list_objects (images) , list_bullets]
def get_state(list_objects, list_bullets):

    new_list = []
    new_list_bullets = []

    for image in list_objects:
        old_object = image._object

        if is_outside(image):
            continue

        # about character
        if isinstance(old_object, Character):
            summary_hit = bullet_hit_character(list_bullets, image)
            old_object._health -= summary_hit
            if old_object._health <= 0:
                return "GAME OVER"

            for another_image in list_objects:
                if dist(image, another_image) and image != another_image and\
                        not isinstance(another_image._object, Bullet):
                    return "GAME OVER"

            new_list.append(image)

        # about bullets
        elif isinstance(old_object, Bullet):
            for another_image in list_objects:
                if bullet_in_object(image, another_image):
                    break
            else:
                new_list.append(image)
                new_list_bullets.append(image)

        # about asteroids and ships
        elif isinstance(old_object, Ship):
            is_killed = False
            for bullet_image in list_bullets:
                bullet = bullet_image._object
                if bullet._direction == 'up' and dist(bullet_image, image):
                    is_killed = True
                    break
            if not is_killed:
                new_list.append(image)
        elif isinstance(old_object, Asteroid):
            new_list.append(image)

    return [new_list, new_list_bullets]


# returns lists = [list_objects (images) , list_bullets]
def calculate_step(timer, list_objects, list_bullets, key_status):

    upper = WIN_HEIGHT
    for image in list_objects:

        old_object = image._object
        if not isinstance(old_object, Bullet):
            upper = min(upper, image._y)

        bullet_hit = 0

        # about character
        if isinstance(old_object, Character):
            if key_status == 'left' and image._x != LEFT_X:
                image._x -= CHARACTER_STEP
            elif key_status == 'right' and image._x != RIGHT_X:
                image._x += CHARACTER_STEP
            elif key_status == 'up':
                new_bullet = Bullet('up', BULLET_HIT)
                new_bullet_image = composite_draw.ImageOfObject(new_bullet, image._x, image._y)
                list_bullets.append(new_bullet_image)
                list_objects.append(new_bullet_image)

        # about bullet
        elif isinstance(old_object, Bullet):
            if old_object._direction == 'down':
                image._y += old_object._speed
            else:
                image._y -= old_object._speed

        # about asteroids and ships
        else:
            if timer > FIRST_TIME_EDGE:
                if timer > SECOND_TIME_EDGE:
                    image._y += HIGH_SPEED
                    bullet_hit = RED_BULLET_HIT
                else:
                    image._y += MIDDLE_SPEED
                    bullet_hit = YELLOW_BULLET_HIT
            else:
                image._y += LOW_SPEED
                bullet_hit = GREEN_BULLET_HIT

        # create new bullets
        if isinstance(old_object, Ship):
            if timer % RAND_TIME == 0:
                new_bullet = Bullet('down', bullet_hit)
                new_bullet_image = composite_draw.ImageOfObject(new_bullet, image._x, image._y)
                list_bullets.append(new_bullet_image)
                list_objects.append(new_bullet_image)

    if upper >= DISTANCE:
        type_new_object = random.choice(["small asteroid", "big asteroid", "ship"])
        new_x = random.choice([LEFT_X, MIDDLE_X, RIGHT_X])

        if type_new_object == "small asteroid":
            small_factory = SmallAsteroidFactory()
            new_object = small_factory.create()
        elif type_new_object == "big asteroid":
            big_factory = BigAsteroidFactory()
            new_object = big_factory.create()
        else:
            director = Shipyard()
            if timer > FIRST_TIME_EDGE:
                if timer > SECOND_TIME_EDGE:
                    new_object = director.construct_ship("C")
                else:
                    new_object = director.construct_ship("B")
            else:
                new_object = director.construct_ship("A")
        new_image = composite_draw.ImageOfObject(new_object, new_x, UP_Y)
        list_objects.append(new_image)

    return [list_objects, list_bullets]
