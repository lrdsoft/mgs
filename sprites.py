# This module contains loading sprites from files
# into structures, managing them and sorting.

import pygame

class Assets(object):
    def __init__(self):
        self.path = choice
        self.directory = directory


    def return_path(self, theme_number):
        switcher = {
            1: "classic",
            2: "elbow" ,
            3: "greatsphere" ,
            4: "js"
        }
        return switcher.get(theme_number)

# Basic sprite block size
SPRITE_SIZE = 32

# Screen ratio
SCREEN_RATIO = 16

# Basic resolution for sprite filling regarding SNES-clone engine
# for information purposes only
# Pixel multiplied by 6 given a 1920 x 1080 resolution
SCREEN_WIDTH_I = 320
SCREEN_HEIGHT_I = 180

# Pixel multiplied by 5 given a 1920 x 1080 resolution (preffered)
SCREEN_WIDTH_II = 384
SCREEN_HEIGHT_II = 216

# Pixel multiplied by 4 given a 1920 x 1080 resolution (preffered)
SCREEN_WIDTH_III = 480
SCREEN_HEIGHT_III = 270

# Default Value
SPRITE_PATH = "classic"

SPRITEDICT = {'fishleft': pygame.image.load('data/sprites/' + SPRITE_PATH + '/fishleft.png'),
              'fishright': pygame.image.load('data/sprites/' + SPRITE_PATH + '/fishright.png'),
              'bck': pygame.image.load('data/sprites/' + SPRITE_PATH + '/bck.png'),
              'mgs': pygame.image.load('data/sprites/' + SPRITE_PATH + '/mgs.png'),
              'pointer': pygame.image.load('data/sprites/' + SPRITE_PATH + '/pointer.png'),
              'screw': pygame.image.load('data/sprites/' + SPRITE_PATH + '/screw.png'),
              'filtr': pygame.image.load('data/sprites/' + SPRITE_PATH + '/filtr.png')}

