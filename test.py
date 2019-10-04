#from screeninfo import get_monitors

#for m in get_monitors():
#    print(str(m))

import pygame

pygame.init()

SPRITE_PATH = "classic"

SPRITEDICT = {'fishleft': pygame.image.load('data/sprites/' + SPRITE_PATH + '/fishleft.png'),
              'fishright': pygame.image.load('data/sprites/' + SPRITE_PATH + '/fishright.png'),
              'bck': pygame.image.load('data/sprites/' + SPRITE_PATH + '/bck.png'),
              'mgs': pygame.image.load('data/sprites/' + SPRITE_PATH + '/mgs.png'),
              'pointer': pygame.image.load('data/sprites/' + SPRITE_PATH + '/pointer.png'),
              'screw': pygame.image.load('data/sprites/' + SPRITE_PATH + '/screw.png'),
              'filtr': pygame.image.load('data/sprites/' + SPRITE_PATH + '/filtr.png')}

bg = pygame.image.load("data/bck.png")

win = pygame.display.set_mode((400, 400))
win.blit(SPRITEDICT['bck'], (0, 0))

while(True):
    pygame.display.update()
    print(1)




