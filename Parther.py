import character
import composite_draw
from graphics import *
import game_step


FPS = 60


class Parther(object):

    @staticmethod
    def main():
        clock = pygame.time.Clock()

        pygame.init()
        surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        space_image = pygame.image.load('Resources/space.png').convert()
        space_image = pygame.transform.scale(space_image, (WIN_WIDTH, WIN_HEIGHT))

        game_over_image = pygame.image.load('Resources/game_over.jpg').convert()
        game_over_image = pygame.transform.scale(game_over_image, (WIN_WIDTH, WIN_HEIGHT))

        # asteroids image initialization
        first_asteroid_image = pygame.image.load('Resources/first_asteroid.png').convert()
        first_asteroid_image = pygame.transform.scale(first_asteroid_image, SMALL_SIZE)
        first_asteroid_image.set_colorkey(BLACK)

        second_asteroid_image = pygame.image.load('Resources/second_asteroid.png').convert()
        second_asteroid_image = pygame.transform.scale(second_asteroid_image, BIG_SIZE)
        second_asteroid_image.set_colorkey(BLACK)

        # ships image initialization
        green_ship = pygame.image.load('Resources/green_ship.png').convert()
        green_ship = pygame.transform.scale(green_ship, MIDDLE_SIZE)
        green_ship.set_colorkey(BLACK)

        red_ship = pygame.image.load('Resources/red_ship.png').convert()
        red_ship = pygame.transform.scale(red_ship, MIDDLE_SIZE)
        red_ship.set_colorkey(BLACK)

        yellow_ship = pygame.image.load('Resources/yellow_ship.png').convert()
        yellow_ship = pygame.transform.scale(yellow_ship, MIDDLE_SIZE)
        yellow_ship.set_colorkey(BLACK)

        # character image initialization
        character_image = pygame.image.load('Resources/character.png').convert()
        character_image = pygame.transform.scale(character_image, BIG_SIZE)
        character_image.set_colorkey(BLACK)

        image_dict = {'surface': surface, 'space_image': space_image, 'first_asteroid_image': first_asteroid_image,
                      'second_asteroid_image': second_asteroid_image, 'green_ship': green_ship, 'red_ship': red_ship,
                      'yellow_ship': yellow_ship, 'character_image': character_image}

        pygame.display.set_caption("Try to survive here...")

        pygame.display.update()
        list_objects = []
        list_bullets = []
        step = 0

        main_character = character.Character()
        draw_adapter = DrawAdapter()
        # start position
        list_objects.append(composite_draw.ImageOfObject(main_character, MIDDLE_X, DOWN_Y))

        surface.fill(GRAY)
        draw_adapter.draw_object(image_dict, main_character)

        game_painter = composite_draw.Painter()
        end = None

        while True:
            step += 1
            clock.tick(FPS)
            key_status = None

            surface.blit(space_image, START_COORD)

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_LEFT:
                        key_status = "left"
                    elif i.key == pygame.K_RIGHT:
                        key_status = "right"
                    elif i.key == pygame.K_UP:
                        key_status = "up"

            if end == "Game over":
                surface.blit(game_over_image, START_COORD)
                font = pygame.font.Font(None, TEXT_SIZE)
                info_about_hp = font.render("Game over", True, DARK_RED)

                surface.blit(info_about_hp, TEXT_END_COORD)
                pygame.display.update()
                continue

            lists_first = game_step.calculate_step(pygame.time.get_ticks(), step, list_objects, list_bullets, key_status)
            lists_second = game_painter.draw_new_step(image_dict, lists_first[0], lists_first[1])

            if lists_second == "Game over":
                end = "Game over"
                continue

            list_objects = lists_second[0]
            list_bullets = lists_second[1]

            font = pygame.font.Font(None, TEXT_SIZE)
            info_about_hp = font.render("Health : " + str(main_character.health), True, YELLOW)
            info_about_score = font.render("Score : " + str(int(step / 2)), True, YELLOW)

            surface.blit(info_about_hp, TEXT_HP_COORD)
            surface.blit(info_about_score, TEXT_SCORE_COORD)

            pygame.display.update()


if __name__ == "__main__":

    game = Parther()
    game.main()
