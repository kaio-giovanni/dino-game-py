import pygame as pg


class Bird(pg.sprite.Sprite):

    def __init__(self, *groups) -> None:
        super().__init__(*groups)