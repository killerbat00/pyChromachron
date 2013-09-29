#!/bin/env python2.7
'''
chromachron clone in python2.7
    and pygame1.9

inspired by awesome german design and pixies
@author brian morrow
'''
import pygame, sys, random, time, math, pygame.gfxdraw
from pygame.locals import *
from datetime import datetime

fps = 1
winwidth = 500
winheight = 500

def main():
    pygame.init()
    fpsclock = pygame.time.Clock()
    display = pygame.display.set_mode((winwidth, winheight))
    pygame.display.set_caption('chromachron')
    pygame.mouse.set_visible(0)

    cf = ClockFace()
    ch = ClockHands()
    ch.setInitTime()
    sprites = pygame.sprite.RenderPlain((cf, ch))

    while True:
        fpsclock.tick(fps)
        sprites.update()
        sprites.draw(display)
        pygame.display.flip()
        checkForQuit()

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()

class ClockHands(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ch.png')
        self.original = self.image
        self.rect = self.image.get_rect()
        self.angle = 0

    # magic
    def setInitTime(self):
        def _getTime():
            time = datetime.now().time()
            return str(time)[:5]

        time = _getTime()
        hour = time[:2]
        min = time[3:]
        hDeg = int(hour)*30
        mDeg = int(min)/2
        self.angle = (hDeg+mDeg)*-1

    def update(self):
        center = self.rect.center
        self.angle = self.angle - 0.008335
        if self.angle == -360:
            self.angle = 0
            self.image = self.original
        else:
            self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect = self.image.get_rect(center=center)

class ClockFace(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('bg.png')
        self.rect = self.image.get_rect()

if __name__ == '__main__':
    main()
