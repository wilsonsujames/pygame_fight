import pygame
import enemy
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("Great People fight")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

Rpunch=[pygame.image.load('rightPuncture2.png'),pygame.image.load('rightPuncture2.png'),pygame.image.load('rightPuncture3.png'),pygame.image.load('rightPuncture3.png'),pygame.image.load('rightPuncture3.png'),pygame.image.load('rightPuncture3.png'),pygame.image.load('rightPuncture3.png'),pygame.image.load('rightPuncture3.png'),pygame.image.load('rightPuncture3.png')]

Lpunch=[pygame.image.load('leftPuncture2.png'),pygame.image.load('leftPuncture2.png'),pygame.image.load('lefttPuncture3.png'),pygame.image.load('lefttPuncture3.png'),pygame.image.load('lefttPuncture3.png'),pygame.image.load('lefttPuncture3.png'),pygame.image.load('lefttPuncture3.png'),pygame.image.load('lefttPuncture3.png'),pygame.image.load('lefttPuncture3.png')]

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.Rpunchact=False
        self.Lpunchact=False
        self.walkCount = 0
        self.jumpCount = 9
        self.face=-1
        self.hitbox = pygame.Rect(self.x + 17, self.y + 11, 29, 52) # NEW
        self.punchhitbox=pygame.Rect(0, 0, 0, 0)
       

    def draw(self, win):
        # 設定偵數
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            self.face =1
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            self.punchhitbox=pygame.Rect(0, 0, 0, 0)

        elif self.right:
            self.face =-1
                    
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
            self.punchhitbox=pygame.Rect(0, 0, 0, 0)
          

        elif self.Lpunchact :
            win.blit(Lpunch[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
            self.punchhitbox=pygame.Rect(self.x + 5 , self.y + 30, 20, 15) 

        elif self.Rpunchact :
            win.blit(Rpunch[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
            self.punchhitbox=pygame.Rect(self.x + 36 , self.y + 30, 20, 15)

        #standing facing side     
        else:
            if self.face==-1:
                win.blit(walkRight[0], (self.x, self.y))
                self.punchhitbox=pygame.Rect(0, 0, 0, 0)

            else:
                win.blit(walkLeft[0], (self.x, self.y))
                self.punchhitbox=pygame.Rect(0, 0, 0, 0)

        self.hitbox = pygame.Rect(self.x + 17, self.y + 11, 29, 52) 
        pygame.draw.rect(win, (255,0,0), self.hitbox,2) # To draw the hit box around the player
        pygame.draw.rect(win, (0,10,180), self.punchhitbox,2)


def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)
    
    pygame.display.update()


#mainloop
man = player(100, 410, 64,64)
goblin = enemy.enemy(100, 410, 64, 64, 450)
run = True
count=0
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
        
    if man.punchhitbox.colliderect(goblin.hitbox):
        goblin.hit()    



    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False

    elif keys[pygame.K_a] and man.face==1 :  
        man.right = False
        man.left = False
        man.Lpunchact= True    
    elif keys[pygame.K_a] and man.face==-1 :  
        man.right = False
        man.left = False
        man.Rpunchact= True    
    else:
        man.Rpunchact= False
        man.Lpunchact= False
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -9:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 9
       
            
    redrawGameWindow()

pygame.quit()