from math import sin, cos, radians

import risar


class Turtle(object):
    def __init__(self):
        self.x, self.y = risar.maxX // 2, risar.maxY // 2
        self.angle = 0
        self.penActive = True

        self.pause = 1
        self.body = risar.krog(0, 0, 5, risar.zelena, 3)
        self.head = risar.krog(0, 0, 2, risar.zelena, 3)
        self.pen = risar.krog(0, 0, 2, risar.rumena, 3)
        self.update()

        self.width = 1
        self.color = risar.bela

        self.stamps = []

        self. macro = []

    def show(self):
        self.body.show()
        self.head.show()
        if self.penActive:
            self.pen.show()
        else:
            self.pen.hide()

    def hide(self):
        self.body.hide()
        self.head.hide()
        self.pen.hide()

    def update(self):
        angle = radians(90 - self.angle)
        self.body.setPos(self.x, self.y)
        self.pen.setPos(self.x, self.y)
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
            risar.crta(self.x, self.y, nx, ny, sirina = self.width, barva = self.color)
        self.x, self.y = nx, ny
        self.update()
        self.macro.append([self.forward, [l]])

    def backward(self, l):
        self.forward(-l)

    def turn(self, angle):
        self.angle += angle
        self.update()
        self.macro.append([self.turn, [angle]])

    def left(self):
        self.turn(-90)

    def right(self):
        self.turn(90)

    def penUp(self):
        self.penActive = False
        self.macro.append(self.penUp)


    def penDown(self):
        self.penActive = True
        if self.head.isVisible():
            self.pen.show()
        self.macro.append(self.penDown)

    def fly(self, x, y, angle):
        self.x, self.y = x, y
        self.angle = angle
        self.update()
        self.macro.append([self.fly, [x, y, angle]])

    def wait(self, s=0):
        risar.cakaj(s)

    def turnAround(self):
        self.turn(180)

    def setWidth(self, n):
        self.width = n

    def setColor(self, color):
        self.color = color

    def stamp(self):
        angle = radians(90 - self.angle)
        self.stamps.append(risar.krog(self.x, self.y, 5, risar.zelena, 3))
        self.stamps.append(risar.krog(self.x + 5 * cos(angle), self.y - 5 * sin(angle), 3, risar.zelena, 3))

    def clearStamps(self):
        for stamp in self.stamps:
            risar.odstrani(stamp)

    def startRecording(self):
        self.macro = []

    def stopRecording(self):
        macros = self.macro
        self.macro = []
        return macros

    def play(self, trace):
        for func, pars in trace:
            func(*pars)

t = Turtle()
t.startRecording()
t.forward(10)
t.stamp()
t.left()
t.forward(100)
t.turn(45)
t.forward(20)
t.stamp()
t.right()
t.forward(40)
t.left()
t.forward(40)
t.right()
t.forward(40)
t.stamp()
t.right()
a = t.stopRecording()
t.fly(risar.maxX // 2, risar.maxY // 2, 0)
t.setColor(risar.rdeca)
t.setWidth(2)
t.play(a)
t.clearStamps()
risar.stoj()
