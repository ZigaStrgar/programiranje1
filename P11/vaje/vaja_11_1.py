import random

import risar
x1, y1, r1 = random.randint(20, risar.maxX - 20), random.randint(20, risar.maxY - 20), random.randint(5, 20)
risar.krog(x1, y1, r1, barva=risar.nakljucna_barva())

for i in range(50):
    x, y, r = random.randint(20, risar.maxX - 20), random.randint(20, risar.maxY - 20), random.randint(5, 20)
    risar.krog(x, y, r, barva=risar.nakljucna_barva())
    risar.crta(x1, y1, x, y, barva=risar.nakljucna_barva())
risar.stoj()
