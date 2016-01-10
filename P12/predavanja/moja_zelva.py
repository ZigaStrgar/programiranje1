from math import radians, cos, sin

import risar


class Turtle:
    def __init__(self):
        self.ime = "Barb"
        self.x = risar.maxX / 2
        self.y = risar.maxY / 2
        self.angle = 0
        self.pen_active = True
        self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog(0, 0, 3, risar.zelena, 3)
        self.update()
        self.pause = 0
        self.color = "bela"
        self.width = 1

    def set_pause(self, n):
        self.pause = n

    def no_pause(self):
        self.set_pause(0)

    def hide(self):
        self.body.hide()
        self.head.hide()

    def show(self):
        self.body.show()
        self.head.show()

    def pen_up(self):
        self.pen_active = False

    def pen_down(self):
        self.pen_active = True

    def update(self):
        self.body.setPos(self.x, self.y)
        self.head.setPos(self.x + 5 * cos(radians(90 - self.angle)), self.y + 5 * sin(radians(90 - self.angle)))
        risar.cakaj(self.pause)

    def fly(self, x, y, angle):
        self.x, self.y, self.angle = x, y, angle
        self.update()

    def forward(self, a):
        phi = radians(90 - self.angle)
        nx = self.x + a * cos(phi)
        ny = self.y + a * sin(phi)
        if self.pen_active:
            risar.crta(self.x, self.y, nx, ny)
        self.x, self.y = nx, ny
        self.update()
        risar.cakaj(self.pause)

    def backward(self, a):
        self.forward(-a)

    def turn(self, phi):
        self.angle += phi
        self.update()

    def left(self):
        self.turn(-90)

    def right(self):
        self.turn(90)

    def turnAround(self):
        self.turn(180)


t = Turtle()
t.forward(100)
risar.stoj()
