import pygame as pg
import sys, os, time


def check_errors():
    errors = pg.init()
    if errors[1] > 0:
        print(f"(!) Ops, houve com algum problema... {errors}")
        return False
    else:
        print("(+) O jogo foi iniciado com sucesso!")
        return True


def quit_game():
    time.sleep(1)
    pg.quit()
    sys.exit(0)


def pygame_off():
    print("\t \t --- O MÓDULO PYGAME FOI DESLIGADO ---")


def get_info_display():
    if pg.display.get_init():
        print("Back-End de exibição do pygame", pg.display.get_driver(), sep=" : ", end="\n")
        print("Informações de exibição de vídeo", pg.display.Info(), sep=" : \n", end="\n")
        print("Informações sobre o sistema de janelas atual", pg.display.get_wm_info(), sep=" : ", end="\n")
    else:
        print("O pygame nao foi iniciado !!")


def carregar_imagem(pasta, nome_imagem):
    nome = os.path.join(os.path.curdir, pasta, nome_imagem)
    try:
        imagem = pg.image.load(nome)
    except pg.error:
        print("Não foi possivel carregar a imagem: ", nome)
        raise SystemExit
    return imagem, imagem.get_rect()


def carregar_imagens(pasta, *nome_imagem):
    imgs = []
    for img in nome_imagem:
        imgs.append(carregar_imagem(pasta, img)[0])
    return imgs

