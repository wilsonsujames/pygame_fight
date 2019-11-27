import pygame

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = pygame.Rect(self.x + 17, self.y + 2, 28, 57) # NEW
        self.health=10
        self.visible=True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 32:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //4], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = pygame.Rect(self.x + 16, self.y + 2, 28, 57) # NEW
            else:
                win.blit(self.walkLeft[self.walkCount //4], (self.x, self.y))
                self.walkCount += 1
                self.hitbox = pygame.Rect(self.x + 23, self.y + 2, 28, 57) # NEW
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    # NEW METHOD
    def hit(self): # ALL NEW
        if self.health > 0:
            self.health -= 0.2
        else:
            self.visible = False
        print('hit')