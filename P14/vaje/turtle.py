import random
from math import sin, cos, radians

from PyQt4.QtGui import *

import risar


class Turtle(object):
    def __init__(self):
        self.x, self.y = risar.maxX // 2, risar.maxY // 2
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
        self.head.setPos(self.x + 5 * cos(angle), self.y - 5 * sin(angle))
        if self.pause:
            self.wait(self.pause)

    def setPause(self, s):
        self.pause = s

    def noPause(self):
        self.setPause(0)

    def forward(self, l):
        angle = radians(90 - self.angle)
        nx, ny = self.x + l * cos(angle), self.y - l * sin(angle)
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

    def __mul__(self, other):
        import math
        if math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) < 10:
            return Turtle()
        raise ValueError("Želvi nista dovolj blizu")


class ZelvaZImenom(Turtle):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def pozdrav(self):
        print("Jaz sem želvica", self.name)


class Cveka(ZelvaZImenom):
    def __init__(self, name):
        super().__init__(name)

    def forward(self, l):
        super().forward(l)
        print("{} gre {} korakov naprej".format(self.name, l))

    def turn(self, angle):
        super().turn(angle)
        print("{} se obrača za {} stopinj".format(self.name, angle))

    def backward(self, l):
        super().forward(-l)
        print("{} gre {} korakov nazaj".format(self.name, l))


class Rdecevratka(Turtle):
    def __init__(self):
        super().__init__()
        self.head.setPen(QPen(QBrush(risar.rdeca), 3))

    def forward(self, l):
        super().forward(l / 2)

    def hide(self):
        self.head.hide()


class VojskaZelv:
    def __init__(self, num):
        self.vojska = [Turtle() for x in range(num)]
        for i, e in enumerate(self.vojska):
            e.x += 20 * (i - ((num - 1) / 2))
            e.update()

    def forward(self, l):
        for e in self.vojska:
            e.forward(l)

    def turn(self, l):
        for e in self.vojska:
            e.turn(l)

    def backward(self, l):
        for e in self.vojska:
            e.forward(-l)


class Pijanka(Turtle):
    def __init__(self):
        super().__init__()
        self.numdrink = 0

    def forward(self, l):
        if self.numdrink < 5:
            self.turn(random.randint(-5 * self.numdrink, 5 * self.numdrink))
            super().forward(l)

    def turn(self, angle):
        if self.numdrink < 5:
            super().turn(angle)

    def drink(self):
        self.numdrink += 1


class Pravokotnica(Turtle):
    def __init__(self):
        super().__init__()

    def forward(self, l):
        ang = self.angle
        self.angle = 0
        super().forward(l * cos(radians(ang)))
        super().turn(90)
        super().forward(l * sin(radians(ang)))
        self.angle = ang
        self.update()


c = VojskaZelv(4)
c.forward(100)

oce = Turtle()
mati = Turtle()
son = oce * mati

oce.forward(20)
oce.turn(30)
oce.forward(20)

mati.forward(20)
mati.turn(-30)
mati.forward(20)
risar.stoj()
