import composite_draw
from space_ships import *
from character import *
from asteroid import *
from bullet import *
from macros import *
import random


def dist(first_obj, second_obj):
    return abs(first_obj.y - second_obj.y) < EPS and abs(first_obj.x - second_obj.x) < EPS


def is_outside(the_object):
    return the_object.y > WIN_WIDTH + EPS or the_object.y < -EPS


class Observer(object):

    # first handle event (observer)
    @staticmethod
    def bullet_in_object(bullet_image, image):
        if isinstance(image.object, Bullet):
            return False
        bullet = bullet_image.object
        if dist(bullet_image, image) and not isinstance(image.object, Character) and bullet.direction == 'up':
            return True
        if dist(bullet_image, image) and not isinstance(image.object, Ship) and bullet.direction == 'down':
            return True
        return False

    # second handle event (observer)
    @staticmethod
    def bullet_hit_character(list_bullets, image):
        summary_hit = 0
        for bullet_image in list_bullets:
            bullet = bullet_image.object
            if bullet.direction == 'down' and dist(image, bullet_image):
                summary_hit += bullet.hit
        return summary_hit

    @staticmethod
    def create_bullet(direction, bullet_hit, x, y):
        new_bullet = Bullet(direction, bullet_hit)
        new_bullet_image = composite_draw.ImageOfObject(new_bullet, x, y)
        return new_bullet_image


def get_bullet_speed(timer):
    if timer > FIRST_TIME_EDGE:
        if timer > SECOND_TIME_EDGE:
            return BULLET_HIGH_SPEED
        else:
            return BULLET_MIDDLE_SPEED
    else:
        return BULLET_LOW_SPEED


# returns lists = [list_objects (images) , list_bullets]
def get_state(list_objects, list_bullets):

    new_list = []
    new_list_bullets = []
    observer = Observer()

    for image in list_objects:
        old_object = image.object

        if is_outside(image):
            continue

        # about character
        if isinstance(old_object, Character):
            summary_hit = observer.bullet_hit_character(list_bullets, image)
            old_object.health -= summary_hit
            if old_object.health <= 0:
                return "GAME OVER : health"

            for another_image in list_objects:
                if dist(image, another_image) and image != another_image and\
                        not isinstance(another_image.object, Bullet):
                    return "GAME OVER : broken"

            new_list.append(image)

        # about bullets
        elif isinstance(old_object, Bullet):
            for another_image in list_objects:
                if observer.bullet_in_object(image, another_image):
                    break
            else:
                new_list.append(image)
                new_list_bullets.append(image)

        # about asteroids and ships
        elif isinstance(old_object, Ship):
            is_killed = False
            for bullet_image in list_bullets:
                bullet = bullet_image.object
                if bullet.direction == 'up' and dist(bullet_image, image):
                    is_killed = True
                    break
            if not is_killed:
                new_list.append(image)
        elif isinstance(old_object, Asteroid):
            new_list.append(image)

    return [new_list, new_list_bullets]


# returns lists = [list_objects (images) , list_bullets]
def calculate_step(timer, step, list_objects, list_bullets, key_status):

    observer = Observer()
    upper = WIN_HEIGHT
    for image in list_objects:

        old_object = image.object
        if not isinstance(old_object, Bullet):
            upper = min(upper, image.y)

        bullet_hit = 0

        # about character
        if isinstance(old_object, Character):
            if key_status == 'left' and image.x != LEFT_X:
                image.x -= CHARACTER_STEP
            elif key_status == 'right' and image.x != RIGHT_X:
                image.x += CHARACTER_STEP
            elif key_status == 'up':
                new_bullet_image = observer.create_bullet('up', BULLET_HIT, image.x, image.y)
                list_bullets.append(new_bullet_image)
                list_objects.append(new_bullet_image)

        # about bullet
        elif isinstance(old_object, Bullet):
            if old_object.direction == 'down':
                image.y += get_bullet_speed(timer)
            else:
                image.y -= old_object.speed

        # about asteroids and ships
        else:
            if timer > FIRST_TIME_EDGE:
                if timer > SECOND_TIME_EDGE:
                    image.y += HIGH_SPEED
                    bullet_hit = RED_BULLET_HIT
                else:
                    image.y += MIDDLE_SPEED
                    bullet_hit = YELLOW_BULLET_HIT
            else:
                image.y += LOW_SPEED
                bullet_hit = GREEN_BULLET_HIT

        # create new bullets
        if isinstance(old_object, Ship):
            if step % BULLET_TIME == 0:
                new_bullet_image = observer.create_bullet('down', bullet_hit, image.x, image.y)
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
