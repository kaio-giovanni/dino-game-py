import pygame as pg


class Underground(pg.sprite.Sprite):

    def __init__(self, pos, image_sheet, speed, containers):
        super().__init__(containers)
        self.states = {
            0: pg.Rect(0, 52, 1204, 16)
        }
        self.image_sheet = image_sheet
        self.image_sheet.set_clip(self.states[0])
        self.image = self.image_sheet.subsurface(self.image_sheet.get_clip())
        self.rect = self.image.get_rect().move(pos)
        self.speed = speed

    def __del__(self):
        print("Del ground sprite")

    def update(self):
        self.rect.move_ip(self.speed, 0)

        if self.rect.x <= -self.rect.width:
            self.rect.x *= -1
