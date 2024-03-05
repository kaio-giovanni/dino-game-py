#############################################
# CACTUS SPRITE
#############################################

import pygame as pg
import random


class Cactus(pg.sprite.Sprite):

    def __init__(self, posX):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.sheet = self.imagem
        self.states = {
            0: pg.Rect(227, 2, 19, 36),
            1: pg.Rect(244, 2, 19, 36),
            2: pg.Rect(261, 2, 19, 36),
            3: pg.Rect(279, 2, 34, 36),
            4: pg.Rect(295, 2, 36, 36),
            5: pg.Rect(331, 2, 28, 50),
            6: pg.Rect(381, 2, 28, 50),
            7: pg.Rect(430, 2, 52, 50)
        }
        self.sheet.set_clip(self.states[random.choice([0, 1, 2, 3, 4, 5, 6, 7])])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect().move(posX, self.pos_ground)
        self.position = posX, self.pos_ground

    def __del__(self):
        print("Cactu is dead")

    def update(self):
        if self.rect.height == 36:
            self.rect.y = self.pos_ground + 14
        else:
            self.rect.y = self.pos_ground

        self.rect.move_ip(self.speed, 0)
        self.position = self.rect.x, self.rect.y

        if self.rect.x <= 0:
            self.kill()

    def getPos(self):
        return self.position
