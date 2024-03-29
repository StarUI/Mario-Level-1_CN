__author__ = 'StarUI'

import pygame as pg
from .. import setup
from .. import constants as c
from . import score


class Coin(pg.sprite.Sprite):
    """在盒子和砖块中找到金币"""
    def __init__(self, x, y, score_group):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['item_objects']
        self.frames = []
        self.frame_index = 0
        self.animation_timer = 0
        self.state = c.SPIN
        self.setup_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y - 5
        self.gravity = 1
        self.y_vel = -15
        self.initial_height = self.rect.bottom - 5
        self.score_group = score_group


    def get_image(self, x, y, width, height):
        """从 Sprite 表中获取图像帧"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)


        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image


    def setup_frames(self):
        """创建框架列表"""
        self.frames.append(self.get_image(52, 113, 8, 14))
        self.frames.append(self.get_image(4, 113, 8, 14))
        self.frames.append(self.get_image(20, 113, 8, 14))
        self.frames.append(self.get_image(36, 113, 8, 14))


    def update(self, game_info, viewport):
        """更新硬币的行为"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.viewport = viewport
        if self.state == c.SPIN:
            self.spinning()


    def spinning(self):
        """硬币处于 SPIN 状态时的操作"""
        self.image = self.frames[self.frame_index]
        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if (self.current_time - self.animation_timer) > 80:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 0

            self.animation_timer = self.current_time

        if self.rect.bottom > self.initial_height:
            self.kill()
            self.score_group.append(score.Score(self.rect.centerx - self.viewport.x,
                                                self.rect.y,
                                                200))






