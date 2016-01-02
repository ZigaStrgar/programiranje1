import random

from PyQt4 import QtGui

import risar

for i in range(100):
    x0, y0 = risar.nakljucne_koordinate()
    x1, y1 = risar.nakljucne_koordinate()
    barva = risar.nakljucna_barva()
    sirina = random.randint(2, 20)
    risar.crta(x0, y0, x1, y1, barva, sirina)

risar.stoj()