__author__ = 'StarUI'

import pygame as pg
from .. import constants as c

class Collider(pg.sprite.Sprite):
    """放置在背景部分上方的隐形精灵,可以与之碰撞(管道,台阶,地面等)."""
    def __init__(self, x, y, width, height, name='collider'):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        #self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None

