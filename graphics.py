# This module handles display.
#
# Class Screen
#   method return_resolution: returns screen resolution
#       this method is obsolete (you can replace it by
#       accesing resolution.current_w/current_h but I decided
#       to leave it for information purposes
#
#   method return_proportions: returns proportions for scaling
#
#   method start_window: starts a window instance
#
#   method scale_image: wrapper for the pygame.transform.scale method
#
#   method redraw_window: redraws a window based on the start_window method
#       it uses the variable "game_screen" stated in the start_window
#       and thanks to the "blit" function it draws the window content
#
#   method draw_sprite: draws a sprite on the pygame surface (from start_window_
#

import pygame

import sprites

pygame.init()

class Screen(object):
    def __init__(self):
        self.resolution = pygame.display.Info()


    def return_resolution(self, attribute):
        if attribute == "w":
            return self.resolution.current_w

        if attribute == "h":
            return self.resolution.current_h


    def return_proportions(self, resolution):
        switcher = {
            1920: 6,
            1080: 6,
            1600: 5,
            900: 5,
            1280: 4,
            800: 4
        }
        return switcher.get(resolution)



    def start_window(self, attribute, window_width, window_height):
        # Title bar of the game window
        pygame.display.set_caption("LRD Engine")

        if attribute == "w":
            self.game_screen = pygame.display.set_mode((window_width, window_height))

        if attribute == "f":
            self.game_screen = pygame.display.set_mode((window_width, window_height),pygame.FULLSCREEN)


    def scale_image(self, image, image_width, sprite_height):
        # targeted solution is by using return_proportions()
        # for testing purpose hardcoded data
        new_image = pygame.transform.scale(image, (image_width * self.return_proportions(1920), sprite_height * self.return_proportions(1080)))
        return new_image


    def redraw_window(self):
        # test
#        self.game_screen.blit(sprites.SPRITEDICT['fishright'], (0, 0))
#        self.game_screen.blit(pygame.transform.scale(sprites.SPRITEDICT['fishright'], (140, 200)), (0, 0))
        self.game_screen.blit(self.scale_image(sprites.SPRITEDICT['fishright'], 70, 100), (0, 0))
        # END test;
        pygame.display.update()

        
    def draw_sprite(self, sprite, x_coord, y_coord):
        self.game_screen.blit(sprite, (x_coord, y_coord))


