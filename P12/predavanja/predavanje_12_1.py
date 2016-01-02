import risar
import turtle

t = turtle.Turtle()


def krak(t, a):
    t.forward(a)
    if a > 5:
        t.turn(30)
        krak(t, a / 1.4)
        t.turn(-60)
        krak(t, a, 1.4)
        t.turn(30)
    return t.backwards()


for i in range(10):
    krak(t, 50)
    t.turn(36)


def broken_line(t, a):
    if a < 5:
        t.forward(a)
    else:
        broken_line(t, a / 3)
        t.turn(60)
        broken_line(t, a / 3)
        t.turn(-120)
        broken_line(t, a / 3)
        t.turn(120)


risar.stoj()
