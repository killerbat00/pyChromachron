#!/bin/env python2.7
'''
chromachron clone in python2.7
    and pygame1.9

inspired by awesome german design and pixies
@author brian morrow
'''
import pygame, sys, random, time, math, pygame.gfxdraw
from pygame.locals import *

fps = 30
winwidth = 500
winheight = 500
colors = {
    0 : (255,235,35),
    1 : (255,125,25),
    2 : (255,195,195),
    3 : (215,35,45),
    4 : (255,105,205),
    5 : (185,25,165),
    6 : (65,65,184),
    7 : (45,125,45),
    8 : (5,195,195),
    9 : (155,75,55),
    10: (225,215,185),
    11: (205,155,105)
}
graycolors = {
    'gray' : (204,204,204),
    'slightlygrayergray' : (102,102,102)
}

def degToRad(deg):
    return deg/180.0 * math.pi
def radToDeg(rad):
    return 180.0/math.pi * rad

def main():
    global fpsclock
    pygame.init()
    fpsclock = pygame.time.Clock()
    display = pygame.display.set_mode((winwidth, winheight))
    pygame.display.set_caption('chromachron')
    cf = ClockFace(color='color')
    cf.draw()
    while True:
        checkForQuit()
        clock()

def clock():
    ch = ClockHands()
    ch.draw()
    pygame.display.update()
    fpsclock.tick(fps)

def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()

class ClockHands:
    def __init__(self):
        pass
    def updatePos(self):
        pass
    def draw(self):
        pass

class ClockFace:
    def __init__(self, color=None):
        self.surf = pygame.display.get_surface()
        self.center = (winwidth/2, winheight/2)
        self.radius = 200
        self.pieces = self.makePieces()
        if color != None:
            self.bg = 'color'
        else:
            self.bg = 'gray'

    def makePieces(self):
        ''' pieces = [(Surface, None, Rect, start_angle, stop_angle, None)]'''
        pieces = []
        for x in range(12):
            start = 30*x
            end = start+30
            p = (self.surf, self.center[0], self.center[1], self.radius, start, end, None)
            pieces.append(p)
        return pieces

    def draw(self):
        def _colorize(pieces, bg):
            if bg == 'color':
                for x in range(12):
                    pieces[x] = list(pieces[x])
                    pieces[x][6] = colors[x]
            elif bg == 'gray':
                pass
            return pieces
        self.pieces = _colorize(self.pieces, self.bg)
        for piece in self.pieces:
            pygame.gfxdraw.pie(piece[0], piece[1], piece[2], piece[3], piece[4], piece[5], piece[6])

if __name__ == '__main__':
    main()
