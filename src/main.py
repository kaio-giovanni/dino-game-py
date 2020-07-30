#!/usr/bin/env python3.8.2
# -*- coding: utf-8 -*-

#############################################
# FUNCTION MAIN
#############################################

''' IMPORTANDO MODULOS'''
import pygame as pg
from functions import *
from Dino import Dino
from Underground import Underground
from Cactus import Cactus

''' VARIAVEIS GLOBAIS'''
BG_COLOR = pg.Color(250, 250, 250, 255)
SCREEN_W = 700
SCREEN_H = 300

''' CRIA UM OBJ RECT COM O TAMANHO DA TELA'''
SCREEN = pg.Rect(0, 0, SCREEN_W, SCREEN_H)

''' FUNÇÃO PRINCIPAL '''
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

    Underground.imagem = sprite_sheet[0]
    Cactus.imagem = sprite_sheet[0]
    Dino.imagem = sprite_sheet[0]

    Cactus.pos_ground = SCREEN.bottom - 76 
    Dino.pos_ground = SCREEN.bottom - 76
    
    Dino.containers = container_all
    Cactus.containers = container_cactus
    Underground.containers = container_underground

    Underground.speed = -5
    Cactus.speed = -5

    player = Dino((50, SCREEN.bottom - 76))

    underground1 = Underground((0,SCREEN.bottom - 44))
    underground2 = Underground((1204, SCREEN.bottom - 44))

    clock = pg.time.Clock()

    while player.alive():

        container_all.clear(surface, bg_screen)
        container_all.update()
        
        ##################    TESTE   ###########################
        player.teste(surface)
        ##################    TESTE   ###########################

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
            elif event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()

                if keys[pg.K_ESCAPE]:
                    quit_game()
                elif keys[pg.K_SPACE]:
                    player.jump()
                elif keys[pg.K_DOWN]:
                    player.run_down()
            elif event.type == pg.KEYUP:
                player.run()

        if player.action == player.actions[4]:
            player.kill()
        
        elif not (player.action == player.actions[0]): 
            container_all.add(underground1, underground2)
                
            for mCactu in pg.sprite.spritecollide(player, container_cactus, False):
                player.collide()

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