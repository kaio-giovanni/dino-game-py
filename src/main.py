#!/usr/bin/env python3.8.2

# -*- coding: utf-8 -*-

''' IMPORTANDO MODULOS'''
import sys, os, time, random
import pygame as pg

''' VARIAVEIS GLOBAIS'''
BG_COLOR = pg.Color(250, 250, 250, 250)
SCREEN_W = 900
SCREEN_H = 400

''' CRIA UM OBJ RECT COM O TAMANHO DA TELA'''
SCREEN = pg.Rect(0, 0, SCREEN_W, SCREEN_H)

'''
class Underground(pg.sprite.Sprite):
    def __init__(self):
        pass

class Dino(pg.sprite.Sprite):
    def __init__(self):
        pass
'''

''' VERIFICANDO A EXISTENCIA DE ERROS'''
def check_errors():
    errors = pg.init()
    if errors[1] > 0:
        print("(!) Ops, {0} houve com algum problema...".format(errors[1]))
        return False
    else:
        print("(+) O jogo foi iniciado com sucesso!")
        return True

''' FUNÇÃO FECHAR JOGO'''
def quit_game():
    time.sleep(0.5)
    pg.quit()
    sys.exit(0)

''' FUNÇÃO EXECUTADA QUANDO O PYGAME DESLIGAR'''
def pygame_off():
    print("\t \t --- O MÓDULO PYGAME FOI DESLIGADO ---")

''' FUNÇÃO PARA OBTER INFORMAÇÕES SOBRE O SISTEMA DE JANELAS ATUAL'''
def get_info_display():
    if pg.display.get_init():
        print("Back-End de exibição do pygame", pg.display.get_driver(), sep=" : ", end="\n")
        print("Informações de exibição de vídeo", pg.display.Info(), sep=" : \n", end="\n")
        print("Informações sobre o sistema de janelas atual", pg.display.get_wm_info(), sep=" : ", end="\n")
    else:
        print("O pygame nao foi iniciado !!")

''' FUNÇÃO PARA CARREGAR IMAGENS EM DISCO'''
def carregar_imagem(pasta,nome_imagem):
    ''' Carrega uma imagem na memória'''
    nome = os.path.join(pasta, nome_imagem)
    ''' os.path.join -> Faz a junção (join) de paths até formar um caminho completo. "Images" é o nome da pasta de imagens '''
    try:
        imagem = pg.image.load(nome)
    except pg.error:
        print("Não foi possivel carregar a imagem: ", nome)
        raise SystemExit
    return imagem, imagem.get_rect()

''' FUNÇÃO PARA CARREGAR UMA LISTA DE IMAGENS'''
def carregar_imagens(pasta, *nome_imagem):
    imgs = []
    for img in nome_imagem:
        imgs.append(carregar_imagem(pasta,img)[0])
    return imgs

''' FUNÇÃO PRINCIPAL '''
def main(surface):

    sprite_sheet = carregar_imagem("assets", "sprite-sheet.png")

    bg_screen = pg.Surface(SCREEN.size)

    surface.blit(bg_screen, (0, 0))

    surface.fill(BG_COLOR)

    pg.display.flip()

    pg.mouse.set_visible(True)

    clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
            elif event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                print(keys)
        clock.tick(60)
    

if __name__ == '__main__':
    if not check_errors():
        sys.exit(-1)
    
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pg.register_quit(pygame_off)

    deep_display = pg.display.mode_ok(SCREEN.size, 0, 32)

    surface = pg.display.set_mode(SCREEN.size, 0, deep_display)

    pg.display.set_caption("Dino game")

    main(surface)
