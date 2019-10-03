import pygame
import random
pygame.init()

class Assets(object):
    def __init__(self, choice):
        self.walkRight = pygame.image.load("data/fishright.png")
        self.walkLeft = pygame.image.load("data/fishleft.png")
        self.menu = pygame.image.load("data/mgs.png")
        self.pointer = pygame.image.load("data/pointer.png")
        self.bg = pygame.image.load("data/bck.png")
        self.bgOutro = pygame.image.load("data/bgoutro.png")
        self.idle = pygame.image.load("data/fishright.png")
        self.wFilter = pygame.image.load("data/filtr.png")
        self.wScrew = pygame.image.load("data/screw.png")
        self.buttonSound = pygame.mixer.Sound("data/pointer.wav")
        self.deathSound = pygame.mixer.Sound("data/death.wav")
        self.alertSound = pygame.mixer.Sound("data/alert.wav")
        self.screwSound = pygame.mixer.Sound("data/screwpickup.wav")

class Fish(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        # hitbox
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.idle = Assets.idle

    def draw(self,win):
        if self.left:
            win.blit(walkLeft, (self.x, self.y))
        elif self.right:
            win.blit(walkRight, (self.x, self.y))
        else:
            win.blit(self.idle, (self.x, self.y))
        # hitbox
        self.hitbox = (self.x + 20, self.y, 28, 60)
        # hitboxtest
        # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

class Enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.miss = 0
        self.vel = 0
        # hitbox
        self.hitbox = (self.x + 40, self.y, 90, 300)
    
    def move(self):
        if self.y < 500:
            self.y += 10 + self.vel * 0.2
        else:
            self.x = random.randint(0, 480)
            self.y = -200
            self.miss += 1
            self.vel += 1

    def draw(self,win):
        win.blit(wFilter, (self.x, self.y))
        # hitbox
        self.hitbox = (self.x + 40, self.y, 90, 300)
        # hitboxtest
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class PowerUp(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        # hitbox
        self.hitbox = (self.x + 10, self.y, 30, 50)

    def move(self):
        if self.y < 500:
            self.y += 10
        else:
            self.x = random.randint(0, 480)
            self.y = random.randint(-4000, 0)

    def draw(self,win):
        win.blit(wScrew, (self.x, self.y))
        # hitbox
        self.hitbox = (self.x + 10, self.y, 30, 50)
        # hitboxtest
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
