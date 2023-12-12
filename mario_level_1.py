#!/usr/bin/env python
__author__ = 'StarUI'

"""
这是试图重新创建第一级
NES的超级马里奥兄弟.
"""

import sys
import pygame as pg
from data.main import main
import cProfile


if __name__=='__main__':
    main()
    pg.quit()
    sys.exit()