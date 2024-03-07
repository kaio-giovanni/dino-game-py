import pygame as pg


class Bird(pg.sprite.Sprite):

    speed = -12

    def __init__(self, pos, image_sheet, *groups) -> None:
        super().__init__(*groups)
        self.states = {0: pg.Rect(133, 8, 47, 33),
                       1: pg.Rect(179, 2, 47, 33)
                       }
        self.index_states = 0
        self.position = pos
        self.image_sheet = image_sheet
        self.image_sheet.set_clip(self.states[self.index_states])
        self.image = self.image_sheet.subsurface(self.image_sheet.get_clip())
        self.rect = self.image.get_rect().move(pos)

    def __del__(self):
        print("Bird deleted")

    def update(self):
        self.rect.move_ip(Bird.speed, 0)
        self.position = self.rect.x, self.rect.y
        self.animation()

        if self.rect.x < -5:
            self.kill()

    def animation(self):
        self.index_states = self.get_index(0, 1)
        self.image_sheet.set_clip(self.states[int(self.index_states)])
        self.image = self.image_sheet.subsurface(self.image_sheet.get_clip())

    def get_index(self, a, b):  # get index between interval
        if self.index_states < a:
            self.index_states = a
        elif self.index_states > b:
            self.index_states = a
        else:
            self.index_states += 0.2
        return self.index_states
