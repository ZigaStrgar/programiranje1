import risar


def trikotnik(Ax, Ay, Bx, By, Cx, Cy):
    risar.crta(Ax, Ay, Bx, By)
    risar.crta(Cx, Cy, Bx, By)
    risar.crta(Ax, Ay, Cx, Cy)


def deli(Ax, Ay, Bx, By, Cx, Cy, n):
    if n == 0:
        return
    ABx, ABy = (Ax + Bx) / 2, (Ay + By) / 2
    ACx, ACy = (Ax + Cx) / 2, (Ay + Cy) / 2
    BCx, BCy = (Cx + Bx) / 2, (Cy + By) / 2
    trikotnik(ABx, ABy, ACx, ACy, BCx, BCy)
    deli(Ax, Ay, ACx, ACy, ABx, ABy, n - 1)
    deli(ACx, ACy, Cx, Cy, BCx, BCy, n - 1)
    deli(ABx, ABy, BCx, BCy, Bx, By, n - 1)


Ax, Ay = 10, 475
Bx, By = 537, 475
Cx, Cy = 271, 10

trikotnik(Ax, Ay, Bx, By, Cx, Cy)
deli(Ax, Ay, Bx, By, Cx, Cy, 5)
risar.stoj()
