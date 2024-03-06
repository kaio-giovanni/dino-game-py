#!/usr/bin/env python3.8.2
# -*- coding: utf-8 -*-

import random
import time

from .Cactus import Cactus
from .Dino import Dino
from .Underground import Underground
from .functions import *

BG_COLOR = pg.Color(250, 250, 250, 255)
SCREEN_W = 700
SCREEN_H = 300
RANGE_CACTUS = range(-1200, -100, 150)

SCREEN = pg.Rect(0, 0, SCREEN_W, SCREEN_H)


def main(surface):
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

    dino_pos = (50, SCREEN.bottom - 76)
    underground_pos_y = SCREEN.bottom - 44
    cactus_pos_y = SCREEN.bottom - 76

    player = Dino(pos_x=dino_pos[0],
                  pos_y=dino_pos[1],
                  image_sheet=sprite_sheet[0],
                  containers=container_all)

    underground1 = Underground((0, underground_pos_y),
                               image_sheet=sprite_sheet[0],
                               speed=-5,
                               containers=container_underground)
    underground2 = Underground((1204, underground_pos_y),
                               image_sheet=sprite_sheet[0],
                               speed=-5,
                               containers=container_underground)

    clock = pg.time.Clock()

    while player.alive():
        container_all.clear(surface, bg_screen)
        container_all.update()

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

        if player.action == player.actions[4]:
            player.kill()

        elif not (player.action == player.actions[0]):
            container_all.add(underground1, underground2)

            for mUnder in container_underground.sprites():
                if mUnder.rect.x in RANGE_CACTUS:
                    cactus_pos_x = (random.randrange(-1200, -100, 150) * -1) + SCREEN_W
                    cactus = Cactus(pos_x=cactus_pos_x,
                                    pos_y=cactus_pos_y,
                                    speed=-5,
                                    image_sheet=sprite_sheet[0],
                                    containers=container_cactus)
                    container_all.add(cactus)

            for mCactu in pg.sprite.spritecollide(player, container_cactus, True):
                # player.collide()
                mCactu.kill()
                player.kill()
                time.sleep(1)

        dirty = container_all.draw(surface)
        pg.display.update(dirty)
        clock.tick(30)

    print("Fim do jogo")


if __name__ == '__main__':
    if not check_errors():
        sys.exit(-1)

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.register_quit(pygame_off)
    deep_display = pg.display.mode_ok(SCREEN.size, 0, 32)
    surface = pg.display.set_mode(SCREEN.size, 0, deep_display)
    pg.display.set_caption("Dino game")
    main(surface)