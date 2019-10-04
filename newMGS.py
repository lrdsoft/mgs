import pygame
import random

import characters
import graphics
import sprites


#window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#clock = pygame.time.Clock()

# new game instance starts:
new_screen = graphics.Screen()
# last used parameters used:
new_screen.start_window("w", 800, 800)
# new_screen.redraw_window()

x = 0

while(x < 10000):
    new_screen.redraw_window()
    x = x + 1
    print (new_screen.resolution.current_w)

pygame.quit()
