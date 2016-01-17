import math
import random

import risar


class Circle:
    def __init__(self):
        self.radius = 10
        self.color = risar.nakljucna_barva()
        self.x = random.randint(self.radius + 5, risar.maxX - (self.radius + 5))
        self.y = random.randint(self.radius + 5, risar.maxY - (self.radius + 5))
        self.angle = random.randint(0, 360)
        self.head = risar.krog(self.x, self.y, self.radius, self.color)
        self.exploded = False
        self.timer = risar.QTimer()
        self.move_x = random.choice([-5, 5])
        self.move_y = random.choice([-5, 5])

    def move(self, mouse):
        if not self.exploded:
            angle = math.radians(self.angle)
            self.x, self.y = self.x + self.move_x * math.cos(angle), self.y - self.move_y * math.sin(angle)
            self.update()
        if not mouse.clicked:
            mouse.update()
        if risar.klik:
            if self.distance():
                self.exploded = True
                self.explode()

    def update(self):
        if not (self.radius < self.x < risar.maxX - self.radius):
            self.move_x = -self.move_x
        if not (self.radius < self.y < risar.maxY - self.radius):
            self.move_y = -self.move_y
        self.head.setPos(self.x, self.y)

    def distance(self):
        for circle in exploded_circles:
            if math.sqrt((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2) < 40:
                return True

    def explode(self):
        self.head.setRect(-30, -30, 60, 60)
        self.fill()
        if self not in exploded_circles:
            exploded_circles.append(self)
        self.timer.singleShot(4000, self.del_item)
        del_from_circles(self)

    def del_item(self):
        risar.odstrani(self.head)
        del_from_list(self)

    def fill(self):
        c = self.head.pen().color().lighter()
        c.setAlpha(192)
        self.head.setBrush(c)


class Mouse(Circle):  # Mouse inherits from Circle function del_item so there is no function duplication
    def __init__(self):
        self.x, self.y = risar.miska
        self.head = risar.krog(self.x, self.y, 30)
        self.clicked = False
        self.timer = risar.QTimer()

    def update(self):
        if not risar.klik:
            self.x, self.y = risar.miska
            self.head.setPos(self.x, self.y)
        else:
            self.clicked = True
            self.fill()
            if self not in exploded_circles:
                exploded_circles.append(self)
            self.timer.singleShot(4000, self.del_item)


def del_from_list(circle):
    del exploded_circles[exploded_circles.index(circle)]


def del_from_circles(circle):
    counter.append(1)
    del circles[circles.index(circle)]


game = 1
per_level = 5
req_per_level = 2
while game <= 5:
    balls = game * per_level + 4
    req = req_per_level * game + 1
    circles = []
    m = Mouse()
    exploded_circles = []
    counter = []

    risar.QMessageBox.information(None, "Konec", "Level: {}. Razpočiti moraš {} žogic od {}.".format(game, req, balls))

    for fn in range(balls):
        circles.append(Circle())

    while not m.clicked or len(exploded_circles) > 0:
        i = 0
        while len(circles) > i:
            circ = circles[i]
            circ.move(m)
            i += 1
        risar.cakaj(0.02)

    if risar.klik and len(exploded_circles) == 0:
        number = len(counter)
        if number >= req:
            risar.QMessageBox.information(None, "Konec",
                                          "Uspelo ti je narediti level {}. Razpočil si {} žogic.".format(game, number))
            game += 1
        else:
            risar.QMessageBox.information(None, "Konec",
                                          "Žal ti ni useplo narediti levela {}. Razpočil si {} žogic od potrebnih {}.".format(
                                                  game, number, req))
    risar.pobrisi()
    risar.klik = False
