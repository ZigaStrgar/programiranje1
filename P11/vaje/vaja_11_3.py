import math

import risar

sez = []

xc, yc, r = risar.maxX / 2, risar.maxY / 2, 200
n = 25
angle = 2 * math.pi / n

ys = []
for i in range(n):
    ny = round((r * math.sin(angle * i)), 4)
    ys.append(ny)

xs = []
for i in range(n):
    ny = round((r * math.cos(angle * i)), 4)
    xs.append(ny)

sredisca = zip(xs, ys)

r = 200 * math.sin(angle / 2)

for x, y in sredisca:
    risar.krog(x + xc, y + yc, r, barva=risar.nakljucna_barva())
    sez.append((x + xc, y + yc))

for x, y in sez:
    for x1, y1 in sez:
        risar.crta(x, y, x1, y1, barva = risar.nakljucna_barva())

risar.stoj()
