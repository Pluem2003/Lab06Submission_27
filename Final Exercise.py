r,g,b = 0,255,0
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

class InputBox:
    def __init__(self,x,y,w,h,text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
             
            if self.active:
                self.color = COLOR_ACTIVE
            else:
                self.color = COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def handle_event_num(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
             
            if self.active:
                self.color = COLOR_ACTIVE
            else:
                self.color = COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if chr(event.key).isnumeric():
                        self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self,Screen):
        Screen.blit(self.txt_surface,(self.rect.x+5, self.rect.y+5))
        pg.draw.rect(Screen, self.color, self.rect, 2)
    
    def isMousePress(self):
        return pg.mouse.get_pressed()[0]
    
import sys
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x,win_y))

COLOR_INACTIVE = pg.Color(141,182,205) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(28,134,238)     # ^^^
FONT = pg.font.Font(None, 32)

font = pg.font.Font('freesansbold.ttf', 26)
text_Firstname = font.render('Firstname', True, 'black', (255,255,255))
text_Lastname = font.render('Lastname', True, 'black', (255,255,255))
text_Age = font.render('Age', True, 'black', (255,255,255))
text_Summit = font.render('Summit', True, 'black')


firstname = InputBox(100, 70, 140, 32)
lastname = InputBox(100, 170, 140, 32)
age = InputBox(100, 270, 140, 32)
summit = Button(100, 370, 200, 32)
summitPress = False

input_boxes = [firstname, lastname]
run = True

while(run):
    screen.fill((255,255,255))
    summit.draw(screen)
    screen.blit(text_Firstname, (100,40))
    screen.blit(text_Lastname, (100,140))
    screen.blit(text_Age, (100,240))
    screen.blit(text_Summit, (150,372))
    if summit.isMouseOn():
        r,g,b = 128,128,128
        if summit.isMousePress():
            r,g,b = 128,0,128
            summitPress = True
    else:
        r,g,b = 0,255,0
    if summitPress:
        screen.blit(font.render('Hello '+ firstname.text+' '+ lastname.text+'!', True, 'black'), (100,420))
        screen.blit(font.render('You are '+ age.text+' years old.', True, 'black'), (100,450))
    for box in input_boxes:
        box.update()
        box.draw(screen)
    age.update()
    age.draw(screen)
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        age.handle_event_num(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()