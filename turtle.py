import risar
from math import pi, sin, cos, radians

class Turtle(object):
    def __init__(self):
        self.x, self.y = risar.maxX//2, risar.maxY//2
        self.angle = 0
        self.penActive = True

        self.pause = 0
        self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog(0, 0, 2, risar.zelena, 3)
        self.update()

    def show(self):
        self.body.show()
        self.head.show()

    def hide(self):
        self.body.hide()
        self.head.hide()

    def update(self):
        angle = radians(90 - self.angle)
        self.body.setPos(self.x, self.y)
        self.head.setPos(self.x+5*cos(angle), self.y-5*sin(angle))
        if self.pause:
            self.wait(self.pause)

    def setPause(self, s):
        self.pause = s
        
    def noPause(self):
        self.setPause(0)

    def forward(self, l):
        angle = radians(90 - self.angle)
        nx, ny = self.x+l*cos(angle), self.y-l*sin(angle)
        nx, ny = max(0, nx), max(0, ny)
        nx, ny = min(nx, risar.maxX), min(ny, risar.maxY)
        if self.penActive:
            risar.crta(self.x, self.y, nx, ny)
        self.x, self.y = nx, ny
        self.update()

    def backward(self, l):
        self.forward(-l)

    def turn(self, angle):
        self.angle += angle
        self.update()

    def left(self):
        self.turn(-90)

    def right(self):
        self.turn(90)

    def penUp(self):
        self.penActive = False

    def penDown(self):
        self.penActive = True

    def fly(self, x, y, angle):
        self.x, self.y = x, y
        self.angle = angle
        self.update()

    def wait(self, s=0):
        risar.cakaj(s)
