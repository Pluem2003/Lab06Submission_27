r,g,b = 255,0,0
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw(self,screen):
        pg.draw.rect(screen,(r,g,b),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self,x=0,y=0,w=0,h=0):
        Rectangle.__init__(self,x,y,w,h)

    def isMouseOn(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.x <= mouse_x <= (self.x+self.w) and self.y <= mouse_y <= (self.y+self.h):
            return True
        else:
            return False
    def isMousePress(self):
        return pg.mouse.get_pressed()[0]

import sys
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x,win_y))
firstObject = Rectangle(20,20,100,100)
btn = Button(400,240,100,100)

while(run):
    screen.fill((255,255,255))

    if btn.isMouseOn():
        r,g,b = 128,128,128
        if btn.isMousePress():
            r,g,b = 128,0,128
    else:
        r,g,b = 255,0,0
    btn.draw(screen)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
