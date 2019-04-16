import pygame
import random
pygame.init()

RX = 600
RY = 400

win = pygame.display.set_mode((RX, RY))
pygame.display.set_caption("Metal Gear Skalar")

walkRight = pygame.image.load("data/fishright.png")
walkLeft = pygame.image.load("data/fishleft.png")
menu = pygame.image.load("data/mgs.png")
pointer = pygame.image.load("data/pointer.png")
bg = pygame.image.load("data/bck.png")
bgOutro = pygame.image.load("data/bgoutro.png")
idle = pygame.image.load("data/fishright.png")
wFilter = pygame.image.load("data/filtr.png")
wScrew = pygame.image.load("data/screw.png")
buttonSound = pygame.mixer.Sound("data/pointer.wav")
deathSound = pygame.mixer.Sound("data/death.wav")
alertSound = pygame.mixer.Sound("data/alert.wav")
screwSound = pygame.mixer.Sound("data/screwpickup.wav")

clock = pygame.time.Clock()


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

    def draw(self,win):
        if self.left:
            win.blit(walkLeft, (self.x, self.y))
        elif self.right:
            win.blit(walkRight, (self.x, self.y))
        else:
            win.blit(idle, (self.x, self.y))
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

def redrawMenuWindow():
    win.blit(menu, (0, 0))


def fmenu():
    musicMenu = pygame.mixer.music.load("data/menu.mp3")
    pygame.mixer.music.play(-1)
    menu = True
    selectpos = True
    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False

        redrawMenuWindow()
        if selectpos:
            win.blit(pointer, (70, 210))
        else:
            win.blit(pointer, (70, 257))

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and selectpos is True:
            selectpos = False
            buttonSound.play()
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and selectpos is False:
            selectpos = True
            buttonSound.play()
        if keys[pygame.K_SPACE] and selectpos is True:
            menu = False
        if keys[pygame.K_SPACE] and selectpos is False:
            pygame.QUIT()
        if keys[pygame.K_ESCAPE]:
            pygame.QUIT()
        pygame.display.update()


def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render('Uniki: ' + str(filtr.miss), 1, (255, 255, 0))
    win.blit(text, (490, 20))
    skalar.draw(win)
    filtr.move()
    filtr.draw(win)
    screwy.move()
    screwy.draw(win)
    pygame.display.update()


def redrawOutroWindow():
    win.blit(bgOutro, (0, 0))
    text = font.render('Porażka śmieciu: ' + str(filtr.miss) + ' czmychnięć', 1, (0, 0, 0))
    win.blit(text, (120, 320))
    text = font.render('r - jeszcze raz, escape - spierdalaj', 1, (0, 0, 0))
    win.blit(text, (100, 350))
    pygame.display.update()


def foutro():
    outro = True
    while outro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                outro = Falsed
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.QUIT()
        if keys[pygame.K_r]:
            filtr.miss = 0
            filtr.vel = 0
            filtr.y = 600
            outro = False
        redrawOutroWindow()
    redrawGameWindow()


fmenu()
pygame.mixer.music.stop()
font = pygame.font.SysFont('impact', 30, True)
skalar = Fish(300, 200, 70, 100)
filtr = Enemy(100, 1, 160, 310)
screwy = PowerUp(-40, 0, 35, 60)
run = True
alertSound.play()
musicAction = pygame.mixer.music.load("data/action.mp3")
pygame.mixer.music.play(-1)
while run:
    clock.tick(30)

    if skalar.hitbox[1] < screwy.hitbox[1] + screwy.hitbox[3] \
	and skalar.hitbox[1] + skalar.hitbox[3] > screwy.hitbox[1]:
        if skalar.hitbox[0] + skalar.hitbox[2] > screwy.hitbox[0] \
and skalar.hitbox[0] < screwy.hitbox[0] + screwy.hitbox[2]:
            filtr.vel -= 1
            screwy.y = 501
            screwSound.play()

    if skalar.hitbox[1] < filtr.hitbox[1] + filtr.hitbox[3] \
	and skalar.hitbox[1] + skalar.hitbox[3] > filtr.hitbox[1]:
        if skalar.hitbox[0] + skalar.hitbox[2] > filtr.hitbox[0] \
and skalar.hitbox[0] < filtr.hitbox[0] + filtr.hitbox[2]:
            deathSound.play()
            foutro()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) \
	and skalar.x > skalar.vel:
        skalar.x -= skalar.vel
        skalar.left = True
        skalar.right = False
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) \
	and skalar.x < (RX - skalar.width - skalar.vel):
        skalar.x += skalar.vel
        skalar.right = True
        skalar.left = False
    if ((keys[pygame.K_LEFT] or keys[pygame.K_a]) \
	and keys[pygame.K_SPACE]) and skalar.x > skalar.vel:
        skalar.x -= skalar.vel+5
        skalar.right = False
        skalar.left = True
    if ((keys[pygame.K_RIGHT] or keys[pygame.K_d]) \
	and keys[pygame.K_SPACE]) \
	and skalar.x < (RX - skalar.width - skalar.vel):
        skalar.x += skalar.vel+5
        skalar.right = True
        skalar.left = False
    if (keys[pygame.K_UP] or keys[pygame.K_w]) \
	and skalar.y > skalar.vel :
       skalar.y -= skalar.vel
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) \
	and skalar.y < (RY - skalar.height - skalar.vel):
        skalar.y += skalar.vel

    redrawGameWindow()

pygame.quit()
