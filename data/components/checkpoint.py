__author__ = 'StarUI'

import pygame as pg
from .. import constants as c


class Checkpoint(pg.sprite.Sprite):
    """隐形精灵用于添加敌人,
       特殊盒子和扳机滑下旗杆"""
    def __init__(self, x, name, y=0, width=10, height=600):
        super(Checkpoint, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name




