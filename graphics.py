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
        pygame.display.set_caption("Metal Gear Skalar")

        if attribute == "w":
            pygame.display.set_mode((window_width, window_height))

        if attribute == "f":
            pygame.display.set_mode((0,0),pygame.FULLSCREEN)


#import pygame
#pygame.init()
#infos = pygame.display.Info()
#screen_size = (infos.current_w, infos.current_h)

#pygame.display.set_mode((0,0),pygame.FULLSCREEN)


##############

#from screeninfo import get_monitors

#for m in get_monitors():
#    print(str(m))
