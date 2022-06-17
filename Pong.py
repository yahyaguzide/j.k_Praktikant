# Mit Importen werden Elemente aus anderen Klassen (Sogenanten Libraries) bekannt gemacht 
import pygame
from pygame.locals import *
import random
from math import sqrt
from math import ceil

#Globale Variable
screensize = (1200,1000)

# Klassen sind Konstrukte welche Objekte abbilden, mit hilfe dieser Klassen kann man Objekte erstellen
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def Set(self,x,y):
        self.x = x
        self.y = y

class Player:
    def __init__(self,position,rect):
        self.position = position
        self.rect = rect
        self.collider = pygame.Rect((self.position.GetX(),self.position.GetY()), (self.rect.GetX(),self.rect.GetY()))
#Zeichnung und Update des Rechtecks (Die neue Position wird fest gelegt)
    def Update(self,screen):
        pygame.draw.rect(screen, (0,   0, 255),
                 [self.position.GetX(),self.position.GetY(), self.rect.GetX(), self.rect.GetY()], 0)
        #pygame.draw.rect(screen,(255,0,0), self.collider)

#Das Rechteck soll sich bewegen
    def Move(self,y, time):
        self.position.Set(self.position.GetX(), self.position.GetY()+int(y*time))
        self.collider = self.collider.move(0, int(y*time))


class Ball:
    def __init__(self,position, speed, r, maxspeed, minspeed, colvec = Vector2D(1,1)):
        self.position = position
        self.speed = speed
        self.colvec = colvec
        self.r = r
        self.maxspeed = maxspeed
        self.minspeed = minspeed
        colliderSideLength = ceil(sqrt(2)*r)
        self.collider = pygame.Rect((self.position.GetX()-colliderSideLength/2, self.position.GetY()-colliderSideLength/2), (colliderSideLength ,colliderSideLength))
    def Update(self,screen, time):
        pygame.draw.circle(screen, (0, 255, 0), [self.position.GetX(), self.position.GetY()], self.r, 0)
        #pygame.draw.rect(screen, (255, 0, 0), self.collider)
        
        self.position.Set(self.position.GetX()+int(self.speed.GetX()*self.colvec.GetX()*time), self.position.GetY()+int(self.speed.GetY()*self.colvec.GetY()*time))
        self.collider = self.collider.move(int(self.speed.GetX()*self.colvec.GetX()*time), int(self.speed.GetY()*self.colvec.GetY()*time))
        # Ändere speed, erst für die Y Achse, dann für die X Achse
        if self.speed.GetY() > self.minspeed:
            if self.speed.GetY()-5 < self.minspeed:
                self.speed.Set(self.speed.GetX(), self.minspeed)
            else:
               self.speed.Set(self.speed.GetX(),self.speed.GetY()-5)
        if self.speed.GetX() > self.minspeed:
            if self.speed.GetX()-5 < self.minspeed:
                self.speed.Set(self.minspeed ,self.speed.GetY()) 
            else:
               self.speed.Set(self.speed.GetX()-5,self.speed.GetY())


    def Collision(self,colvec):
        if colvec.GetX() != 0:
            self.speed.Set(self.maxspeed, self.speed.GetY())
            self.colvec.Set(self.colvec.GetX()*-1, self.colvec.GetY()*random.choice([-1,1]))
        elif colvec.GetY() != 0:
            self.speed.Set(self.speed.GetX(), self.maxspeed)
            self.colvec.Set(self.colvec.GetX()*random.choice([-1,1]), self.colvec.GetY()*-1)



pygame.init()
pygame.key.set_repeat(10)
clock = pygame.time.Clock()

screen = pygame.display.set_mode(screensize)
player1 = Player( Vector2D(100,300), Vector2D(20,150) )
player2 = Player( Vector2D(screensize[0]-120,500), Vector2D(20,150) )
ball = Ball( Vector2D(screensize[0]/2, screensize[1]/2),Vector2D(300,300), 50, 800, 300, Vector2D(-1,1)) 

pointPlayer1 = 0
pointPlayer2 = 0

# Die Grenzen an welchen der Ball Abprallen soll
rect_UP = pygame.Rect((0,0),(screensize[0],20))
rect_DOWN = pygame.Rect((0,screensize[1]-20),(screensize[0],20))
rect_LEFT = pygame.Rect((0,0),(20,screensize[1]))
rect_RIGHT = pygame.Rect((screensize[0],0),(20,screensize[0]))

# Eigener Event für das Physiksystem, dieser löst alle 200 millisekunden einen Event aus
pygame.time.set_timer(pygame.USEREVENT+1, 80)

run = True
while run:
    clock.tick(60)
    screen.fill((255, 255, 255))
    
    delayTime = clock.get_time()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1.Move(-150, delayTime)
                elif event.key == pygame.K_s:
                    player1.Move(150, delayTime)
                if event.key == pygame.K_UP:
                    player2.Move(-150, delayTime)
                elif event.key == pygame.K_DOWN:
                    player2.Move(150, delayTime)
        elif event.type == pygame.USEREVENT+1:
            ball.Collision(Vector2D(ball.collider.collidelist([player1.collider, player2.collider])+1,0))
            
            colLeftRight = ball.collider.collidelist([rect_LEFT, rect_RIGHT])+1
            ball.Collision(Vector2D(colLeftRight, ball.collider.collidelist([rect_UP, rect_DOWN])+1))
            
            if colLeftRight == 2:
                pointPlayer1 = pointPlayer1 +1
                print(str(pointPlayer1) + ":" + str(pointPlayer2))
                pygame.draw.rect(screen, (50, 50, 50), [screensize[0]-10, 0, 10, screensize[1]],0)                
            elif  colLeftRight == 1:
                pointPlayer2 = pointPlayer2 +1
                print(str(pointPlayer1) + ":" + str(pointPlayer2))
                pygame.draw.rect(screen, (50, 50, 50), [0, 0, 10, screensize[1]],0)
                
    # Lasse Objekte sich selber auf den Screen zeichnen
    ball.Update(screen, delayTime)
    player1.Update(screen)
    player2.Update(screen)

   
    pygame.display.update()


