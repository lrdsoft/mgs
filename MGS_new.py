import pygame
import random

import characters
import graphics


#window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#clock = pygame.time.Clock()

# new game instance starts:
new_screen = graphics.Screen()
# last used parameters used:
new_screen.start_window("w", 800, 800)
# new_screen.redraw_window()

x = 0

while(x < 100):
    new_screen.redraw_window()
    x = x + 1
    print (x)

pygame.quit()
