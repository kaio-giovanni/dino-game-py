import pygame as pg
import random


class Cactus(pg.sprite.Sprite):

    speed = -8

    def __init__(self, pos: tuple[int, int], image_sheet: pg.surface.Surface, *groups):
        super().__init__(*groups)
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
        
        self.position = pos
        self.pos_y_tallest = pos[1] + 14
        self.image_sheet = image_sheet
        self.image_sheet.set_clip(self.states[random.choice([0, 1, 2, 3, 4, 5, 6, 7])])
        self.image = self.image_sheet.subsurface(self.image_sheet.get_clip())
        self.rect = self.image.get_rect().move(pos)

    def __del__(self):
        print("Cactus deleted")

    def update(self):
        if self.rect.height == 36:
            self.rect.y = self.pos_y_tallest
        else:
            self.rect.y = self.position[1]

        self.rect.move_ip(Cactus.speed, 0)
        self.position = self.rect.x, self.rect.y

    def get_pos(self):
        return self.position

