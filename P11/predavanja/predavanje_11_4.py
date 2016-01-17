import risar
from random import randint, choice
Ax, Ay = 10, 475
Bx, By = 537, 475
Cx, Cy = 271, 10

desetnik = [(10, 475), (537, 475), (271, 10)]
x = 100
y = 200

risar.obnavljaj = False
for i in range(10000):
    dx, dy = choice(desetnik)
    x = (x + dx) / 2
    y = (y + dy) / 2
    risar.tocka(x, y)
risar.obnovi()
risar.stoj()


