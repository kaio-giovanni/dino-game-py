#############################################
# UNDERGROUND SPRITE
#############################################

import pygame as pg

class Underground(pg.sprite.Sprite):
    
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.sheet = self.imagem
        self.states = { 0: pg.Rect(0, 52, 1204, 16) }
        self.sheet.set_clip(self.states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect().move(pos)

    def __del__(self):
        print("Del ground sprite")

    def update(self):
        self.rect.move_ip(self.speed, 0)

        if self.rect.x <= -self.rect.width:
            self.rect.x *=-1
