#!/usr/bin/env python3.8.2

# -*- coding: utf-8 -*-

''' IMPORTANDO MODULOS'''
import sys, os, time, random
import pygame as pg

''' VARIAVEIS GLOBAIS'''
BG_COLOR = pg.Color(250, 250, 250, 255)
SCREEN_W = 700
SCREEN_H = 300

''' CRIA UM OBJ RECT COM O TAMANHO DA TELA'''
SCREEN = pg.Rect(0, 0, SCREEN_W, SCREEN_H)

class Underground(pg.sprite.Sprite):
    speed = -3

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.sheet = self.imagem
        self.states = { 0: pg.Rect(0, 57, 1204, 11) }
        self.sheet.set_clip(self.states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect().move(pos)

    def __del__(self):
        print("Del ground sprite")
    def update(self):
        self.rect.move_ip(self.speed, 0)
        
class Dino(pg.sprite.Sprite):
    jump_value = 10
    actions = { 0: "stoped",
                1: "running",
                2: "run_down",
                3: "jumping",
                4: "colliding"
            }

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.sheet = self.imagem
        self.states = { 0: pg.Rect(39, 3, 46, 49),
                        1: pg.Rect(891, 1, 46, 49),
                        2: pg.Rect(847, 1, 46, 49),
                        3: pg.Rect(934, 1, 46, 49),
                        4: pg.Rect(979, 1, 46, 49),
                        5: pg.Rect(1023, 1, 46, 49),
                        6: pg.Rect(1111, 18, 60, 32),
                        7: pg.Rect(1171, 19, 60, 32)
                      }
        self.index_states = 0
        self.sheet.set_clip(self.states[self.index_states])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect().move(pos)
        self.position = pos
        self.action = self.actions[0]

    def __del__(self):
        print("Dino is dead")
    def update(self):
        if self.action == self.actions[3]: #jumping
            self.rect.y -= int(self.jump_value)
            self.jump_value -= 0.7

            if self.rect.y > SCREEN.bottom - 77:
                self.rect.y = SCREEN.bottom - 77
                self.action = self.actions[1]
                self.jump_value = 10
        elif self.action == self.action[2]: #run down
            pass

        self.position = self.rect.x, self.rect.y
        self.animation()

    def animation(self):
        if self.action == self.actions[0]:
            self.index_states = 0
            self.sheet.set_clip(self.states[self.index_states])
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        elif self.action == self.actions[1]:
            self.index_states = self.get_index(2,4.4)
            self.sheet.set_clip(self.states[int(self.index_states)])
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        elif self.action == self.actions[2]:
            self.index_states = self.get_index(6,7)
            self.sheet.set_clip(self.states[int(self.index_states)])
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        elif self.action == self.actions[3]:
            self.index_states = self.get_index(1, 1.4)
            self.sheet.set_clip(self.states[int(self.index_states)])
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        elif self.action == self.actions[4]:
            self.index_states = 5
            self.sheet.set_clip(self.states[self.index_states])
            self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        self.rect = self.image.get_rect().move(self.position)

    def jump(self):
        if self.action == self.actions[0] or \
            self.action == self.actions[1] or \
            self.action == self.actions[2]:
            self.action = self.actions[3]

    def run(self):
        if self.action == self.actions[0] or \
            self.action == self.actions[2]:
            self.action = self.actions[1]

    def run_down(self):
        if self.action == self.actions[1]:
            self.action = self.actions[2]
        
    def get_index(self, a, b): #get index between interval
        if self.index_states < a:
            self.index_states = a
        elif self.index_states > b:
            self.index_states = a
        else:
            self.index_states += 0.5
        return self.index_states

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

    Underground.imagem = sprite_sheet[0]
    Dino.imagem = sprite_sheet[0]
    
    Dino.containers = container_all

    player = Dino((20, SCREEN.bottom - 77))

    underground1 = Underground((0,SCREEN.bottom - 40))
    underground2 = Underground((1204, SCREEN.bottom - 40))

    clock = pg.time.Clock()

    while not player.action == player.actions[4]:

        container_all.clear(surface, bg_screen)
        container_all.update()

        if not (player.action == player.actions[0]): 
            container_all.add(underground1, underground2)
            container_underground.add(underground1, underground2)
        
            for ground in container_underground.sprites():
                if(ground.rect.x <= -ground.rect.width):
                    ground.rect.x = ground.rect.width
                
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit_game()
            elif event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()

                if keys[pg.K_SPACE]:
                    player.jump()
                elif keys[pg.K_DOWN]:
                    player.run_down()
            elif event.type == pg.KEYUP:
                player.run()

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
