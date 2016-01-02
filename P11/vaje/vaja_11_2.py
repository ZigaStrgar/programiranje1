import random

import risar

sez = []
for i in range(50):
    x, y, r = random.randint(20, risar.maxX - 20), random.randint(20, risar.maxY - 20), random.randint(5, 20)
    risar.krog(x, y, r, barva=risar.nakljucna_barva())
    sez.append((x, y))

for x, y in sez:
    for x1, y1 in sez:
        risar.crta(x, y, x1, y1, barva = risar.nakljucna_barva())
risar.stoj()
