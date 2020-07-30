#############################################
# DINO SPRITE
#############################################

import pygame as pg

#############################################
COLOR_TESTE = pg.Color(255, 255, 10, 10)
#############################################

class Dino(pg.sprite.Sprite):
    jump_value = 12
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
                        3: pg.Rect(936, 1, 46, 49),
                        4: pg.Rect(980, 1, 46, 49),
                        5: pg.Rect(1024, 1, 46, 49),
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
        if self.action == self.actions[1]: # running
            self.rect.y = self.pos_ground

        elif self.action == self.actions[2]: #run down
            self.rect.y = self.pos_ground + 17
            
        elif self.action == self.actions[3]: #jumping
            self.rect.y -= int(self.jump_value)
            self.jump_value -= 0.7
            if self.rect.y > self.pos_ground:
                self.rect.y = self.pos_ground
                self.action = self.actions[1]
                self.jump_value = 12
        
        self.position = self.rect.x, self.rect.y
        self.animation()

    def animation(self):
        if self.action == self.actions[0]: # stopped
            self.index_states = 0
            self.sheet.set_clip(self.states[self.index_states])
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        elif self.action == self.actions[1]: # running
            self.index_states = self.get_index(3,4.4)
            self.sheet.set_clip(self.states[int(self.index_states)])
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        elif self.action == self.actions[2]: # run down
            self.index_states = self.get_index(6,7)
            self.sheet.set_clip(self.states[int(self.index_states)])
            self.image = self.sheet.subsurface(self.sheet.get_clip())            

        elif self.action == self.actions[3]: # jumping
            self.index_states = self.get_index(1, 1.4)
            self.sheet.set_clip(self.states[int(self.index_states)])
            self.image = self.sheet.subsurface(self.sheet.get_clip())

        elif self.action == self.actions[4]: # colliding
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
            print(self.action)
    
    def collide(self):
        self.action = self.actions[4]
        
    def get_index(self, a, b): #get index between interval
        if self.index_states < a:
            self.index_states = a
        elif self.index_states > b:
            self.index_states = a
        else:
            self.index_states += 0.2
        return self.index_states

    ##################    TESTE   ###########################
    def teste(self, surface): 
        pg.draw.rect(surface, COLOR_TESTE, self.rect)
    ##################    TESTE   ###########################
        
