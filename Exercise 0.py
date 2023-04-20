class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def draw(self,screen):
        pg.draw.rect(screen,(120,20,220),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self,x=0,y=0,w=0,h=0):
        Rectangle.__init__(self,x,y,w,h)

    def isMouseOn(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.x <= mouse_x <= (self.x+self.w) and self.y <= mouse_y <= (self.y+self.h):
            return True
        else:
            return False

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
    firstObject.draw(screen)

    if btn.isMouseOn():
        btn.w = 200
        btn.h = 300
    else:
        btn.w = 100
        btn.h = 100
    btn.draw(screen)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
