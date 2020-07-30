#############################################
# FUNCTIONS
#############################################

import pygame as pg
import sys, os, time

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
    time.sleep(1)
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
