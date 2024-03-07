import pygame as pg

COLOR = pg.Color(0, 0, 0, 255)


# impact, lucidasans, arialblack, couriernew, verdana, timesnewroman


class Score(pg.sprite.Sprite):

    def __init__(self, pos: tuple[int, int], *groups) -> None:
        super().__init__(*groups)
        self.position = pos
        self.score = 0
        self.font = pg.font.SysFont("couriernew", 16)
        self.image = self.font.render(f"Score {self.score}", True, COLOR)
        self.rect = self.image.get_rect().move(pos)

    def __del__(self):
        print("Score deleted")

    def update(self):
        self.image = self.font.render(f"Score {self.score}", True, COLOR)

    def set_score(self, score):
        self.score = score
        print(f"SCORE: {self.score}")
