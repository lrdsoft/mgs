# This module handles display.
#
# Class Screen
#   method start_window: starts a window instance
#
#   method redraw_window: redraws a window based on the start_window method
#       it uses the variable "game_screen" stated in the start_window
#       and thanks to the "blit" function it draws the window content
#
#

import pygame
pygame.init()

class Screen(object):
    def __init__(self):
        self.resolution = pygame.display.Info()

    def return_resolution(self, attribute):
        if attribute == "w":
            return self.resolution.current_w

        if attribute == "h":
            return self.resolution.current_h

    def start_window(self, attribute, window_width, window_height):
        # Title bar of the game window
        pygame.display.set_caption("LRD Engine")

        if attribute == "w":
            self.game_screen = pygame.display.set_mode((window_width, window_height))

        if attribute == "f":
            self.game_screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)

    def redraw_window(self):
        bck = pygame.image.load("data/bck.png")
        self.game_screen.blit(bck, (0, 0))
        pygame.display.update()
        
        


#import pygame
#pygame.init()
#infos = pygame.display.Info()
#screen_size = (infos.current_w, infos.current_h)

#pygame.display.set_mode((0,0),pygame.FULLSCREEN)


##############

#from screeninfo import get_monitors

#for m in get_monitors():
#    print(str(m))
