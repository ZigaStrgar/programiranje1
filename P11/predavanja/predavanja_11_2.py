import random

import risar
from PyQt4 import QtGui

besede = ["test", "123", "beseda"]

for beseda in besede:
    risar.besedilo(random.randint(0, 750), random.randint(0, 400), beseda, risar.nakljucna_barva(), velikost= random.randint(30, 80), pisava="Calibri")

risar.stoj()
