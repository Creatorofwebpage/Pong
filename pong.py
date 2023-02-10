import pygame
import random


WIDTH = 600
HEIGHT = 400
VELKOST = 20
VELKOSTRH = 10
VELKOSTRV = 100
RYCHLOST = 10
ACCEL = 10
randomposx  = random.randint(VELKOST,WIDTH -VELKOST)
randomposy  = random.randint(VELKOST,HEIGHT-VELKOST)
pos_rakety1 = (HEIGHT-VELKOSTRH)/2
pos_rakety2 = (HEIGHT-VELKOSTRH)/2


def gulicka(pos_x, pos_y):
    return pygame.Rect(pos_x, pos_y, VELKOST,VELKOST)

def raketa1(r1):
    return pygame.Rect(0,r1, VELKOSTRH,VELKOSTRV)

def raketa2(r2):
    return pygame.Rect(WIDTH -VELKOSTRH,r2, VELKOSTRH, VELKOSTRV)

def okno(pos_rakety2, pos_rakety1):

    rychlost_x =  RYCHLOST
    rychlost_y = RYCHLOST
    r1 = pos_rakety1
    r2 = pos_rakety2
    pos_x = randomposx
    pos_y = randomposy

    screen = pygame.display.set_mode((WIDTH , HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            running=False
    
        if pressed[pygame.K_UP]:
            r2 -= ACCEL
        if pressed[pygame.K_DOWN]:
            r2+= ACCEL
        if pressed[pygame.K_w]:
            r1 -= ACCEL
        if pressed[pygame.K_s]:
            r1+= ACCEL
        pygame.draw.rect(screen, (255,255,255), gulicka(pos_x, pos_y))
        pygame.draw.rect(screen, (255,255,250), raketa1(r1))
        pygame.draw.rect(screen, (255,255,250), raketa2(r2))
        pos_y -= rychlost_y
        pos_x += rychlost_x
        if pos_y>HEIGHT-VELKOST:
            rychlost_y = -rychlost_y
        if pos_x>WIDTH -VELKOST:
            rychlost_x = -rychlost_x
        if pos_y<0:
            rychlost_y = -rychlost_y
        if pos_x<0:
            rychlost_x = -rychlost_x

        pygame.display.flip()
        screen.fill((0,0,0)) 
        clock.tick(30)
def main():
    pygame.init()
    okno(pos_rakety2,pos_rakety1)
    pygame.quit()

if __name__=="__main__":
    main()