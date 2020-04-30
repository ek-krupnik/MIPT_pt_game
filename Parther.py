import character
import composite_draw
from graphics import *


FPS = 60


def main():
    clock = pygame.time.Clock()

    pygame.init()
    surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    pygame.display.update()

    main_character = character.Character()
    draw_adapter = DrawAdapter()

    surface.fill(GRAY)
    draw_adapter.draw_object(surface, main_character)

    while True:

        clock.tick(FPS)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                return

        composite_draw.draw_new_step(surface, clock.get_time())

        pygame.display.update()


if __name__ == "__main__":
    main()
