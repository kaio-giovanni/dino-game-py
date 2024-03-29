import pygame as pg

JUMP_VALUE = 14


class Dino(pg.sprite.Sprite):

    def __init__(self, pos: tuple[int, int], image_sheet: pg.surface.Surface, *groups) -> None:
        super().__init__(*groups)
        self.actions = {0: "stoped",
                        1: "running",
                        2: "run_down",
                        3: "jumping",
                        4: "colliding"
                        }
        self.states = {0: pg.Rect(39, 2, 46, 47),
                       1: pg.Rect(891, 2, 46, 47),
                       2: pg.Rect(848, 2, 46, 47),
                       3: pg.Rect(935, 2, 46, 47), #running
                       4: pg.Rect(978, 2, 46, 47), #running
                       5: pg.Rect(1022, 2, 46, 47), #collision
                       6: pg.Rect(1111, 18, 60, 32),
                       7: pg.Rect(1171, 18, 60, 32)
                       }
        self.index_states = 0
        self.jump_value = JUMP_VALUE
        self.position = pos
        self.pos_ground = pos[1]
        self.action = self.actions[0]
        self.image_sheet = image_sheet
        self.image_sheet.set_clip(self.states[self.index_states])
        self.image = self.image_sheet.subsurface(self.image_sheet.get_clip())
        self.rect = self.image.get_rect().move(pos)

    def __del__(self):
        print("Dino is dead")

    def is_dead(self):
        return self.action == self.actions[4]

    def is_stopped(self):
        return self.action == self.actions[0]

    def get_pos(self):
        return self.position

    def update(self):
        if self.action == self.actions[1]:  # running
            self.rect.y = self.pos_ground

        elif self.action == self.actions[2]:  # run down
            self.rect.y = self.pos_ground + 17

        elif self.action == self.actions[3]:  # jumping
            self.rect.y -= int(self.jump_value)
            self.jump_value -= 1
            if self.rect.y > self.pos_ground:
                self.rect.y = self.position[1]
                self.action = self.actions[1]
                self.jump_value = JUMP_VALUE

        self.position = self.rect.x, self.rect.y
        self.animation()

    def animation(self):
        if self.action == self.actions[0]:  # stopped
            self.index_states = 0
            self.image_sheet.set_clip(self.states[self.index_states])
            self.image = self.image_sheet.subsurface(self.image_sheet.get_clip())

        elif self.action == self.actions[1]:  # running
            self.index_states = self.get_index(3, 4.4)
            self.image_sheet.set_clip(self.states[int(self.index_states)])
            self.image = self.image_sheet.subsurface(self.image_sheet.get_clip())

        elif self.action == self.actions[2]:  # run down
            self.index_states = self.get_index(6, 7.7)
            self.image_sheet.set_clip(self.states[int(self.index_states)])
            self.image = self.image_sheet.subsurface(self.image_sheet.get_clip())

        elif self.action == self.actions[3]:  # jumping
            self.index_states = self.get_index(1, 1.4)
            self.image_sheet.set_clip(self.states[int(self.index_states)])
            self.image = self.image_sheet.subsurface(self.image_sheet.get_clip())

        elif self.action == self.actions[4]:  # colliding
            self.index_states = 5
            self.image_sheet.set_clip(self.states[self.index_states])
            self.image = self.image_sheet.subsurface(self.image_sheet.get_clip())

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

    def collide(self):
        self.action = self.actions[4]

    def get_index(self, a, b):  # get index between interval
        if self.index_states < a:
            self.index_states = a
        elif self.index_states > b:
            self.index_states = a
        else:
            self.index_states += 0.2
        return self.index_states

    def has_collided(self, enemy: pg.sprite.Sprite):
        return self.rect.colliderect(enemy.rect)
