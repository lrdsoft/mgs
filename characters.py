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
