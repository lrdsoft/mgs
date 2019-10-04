# This module contains loading sounds from files
# into structures, managing them and sorting.
# 
# Sprites and soundbank were split due to expected, large
# ammount of files inbound, thus splitting them was done
# for the sole purpose of easier managing them

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

# Default Value
SOUND_PATH = "classic"

SOUNDDICT = {'action_sound': pygame.mixer.Sound('data/soundbank/' + SOUND_PATH + '/action.mp3'),
              'alert_sound': pygame.mixer.Sound('data/soundbank/' + SOUND_PATH + '/alert.wav'),
              'death_sound': pygame.mixer.Sound('data/soundbank/' + SOUND_PATH + '/death.wav'),
              'menu_sound': pygame.mixer.Sound('data/soundbank/' + SOUND_PATH + '/menu.mp3'),
              'pointersound_sound': pygame.mixer.Sound('data/soundbank/' + SOUND_PATH + '/pointer.wav'),
              'screwpickup_sound': pygame.mixer.Sound('data/soundbank/' + SOUND_PATH + '/screwpickup.wav'),


