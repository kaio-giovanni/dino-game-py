import random
import sys
import time

from modules.Bird import Bird
from modules.Cactus import Cactus
from modules.Dino import Dino
from modules.Underground import Underground
from modules.Score import Score
from modules.functions import *

BG_COLOR = pg.Color(250, 250, 250, 255)
SCREEN_W = 700
SCREEN_H = 300
SCREEN = pg.Rect(0, 0, SCREEN_W, SCREEN_H)


def handle_keyboard_events(player: Dino):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit_game()
        elif event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()

            if keys[pg.K_ESCAPE]:
                quit_game()
            elif keys[pg.K_SPACE] or keys[pg.K_UP]:
                player.jump()
            elif keys[pg.K_DOWN]:
                player.run_down()
        elif event.type == pg.KEYUP:
            player.run()


def main(surface: pg.surface.Surface):
    surface.fill(BG_COLOR)
    sprite_sheet = carregar_imagem("assets", "sprite-sheet.png")
    bg_screen = pg.Surface(SCREEN.size)
    bg_screen.fill(BG_COLOR)
    surface.blit(bg_screen, (0, 0))
    pg.display.flip()
    pg.mouse.set_visible(True)
    pg.key.set_repeat(10)

    container_all = pg.sprite.RenderUpdates()
    container_underground = pg.sprite.Group()
    container_cactus = pg.sprite.Group()
    container_bird = pg.sprite.Group()

    underground_pos_y = SCREEN.bottom - 44
    cactus_pos_y = SCREEN.bottom - 76
    bird_positions_y = [SCREEN.bottom - 68, SCREEN.bottom - 100, SCREEN.bottom - 110]

    player = Dino((50, SCREEN.bottom - 76),
                  sprite_sheet[0],
                  container_all)

    underground_sprite_1 = Underground((0, underground_pos_y),
                                       sprite_sheet[0],
                                       container_underground)
    underground_sprite_2 = Underground((1204, underground_pos_y),
                                       sprite_sheet[0],
                                       container_underground)
    score_sprite = Score((SCREEN_W - 100, 12), container_all)

    clock = pg.time.Clock()
    framerate = 40
    next_enemy_time = 0
    score = 0

    while player.alive():
        container_all.clear(surface, bg_screen)
        container_all.update()
        handle_keyboard_events(player=player)

        if player.is_dead():
            player.kill()
        elif not (player.is_stopped()):
            container_all.add(underground_sprite_1, underground_sprite_2)
            all_cactus = container_cactus.sprites()

            # Create enemies
            if pg.time.get_ticks() > next_enemy_time and len(all_cactus) < 10:
                cactus_pos_x = SCREEN_W + random.randrange(80, 200, 40)
                cactus_sprite = Cactus((cactus_pos_x, cactus_pos_y),
                                       sprite_sheet[0],
                                       container_cactus)
                container_all.add(cactus_sprite)
                next_enemy_time += 1250

                if score in range(10, 2000, 10):
                    bird_pos_x = SCREEN_W + random.randrange(100, 200, 20)
                    bird_pos_y = random.choice(bird_positions_y)
                    bird_sprite = Bird((bird_pos_x,bird_pos_y), sprite_sheet[0], container_bird)
                    container_all.add(bird_sprite)

                    Cactus.speed *= 1.2
                    Underground.speed *= 1.2
                    print(f"Increasing the game level to {Cactus.speed}")

            for cactus in all_cactus:
                if cactus.get_pos()[0] < -10:
                    score += 10
                    score_sprite.set_score(score)
                    cactus.kill()
                    del cactus

            for cactus in pg.sprite.spritecollide(player, container_cactus, True):
                cactus.kill()
                player.kill()
                quit_game()

            for bird in pg.sprite.spritecollide(player, container_bird, True):
                bird.kill()
                player.kill()
                quit_game()

        dirty = container_all.draw(surface)
        pg.display.update(dirty)
        clock.tick(framerate)
    print("Fim do jogo")


if __name__ == '__main__':
    pg.init()

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.register_quit(pygame_off)
    deep_display = pg.display.mode_ok(SCREEN.size, 0, 32)
    surface = pg.display.set_mode(SCREEN.size, 0, deep_display)
    pg.display.set_caption("Dino game")
    main(surface)
