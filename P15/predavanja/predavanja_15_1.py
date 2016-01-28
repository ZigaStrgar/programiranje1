from math import *

v = float(input("Hitrost: "))
kot = float(input("Kot: "))
s = v ** 2 * sin(2 * radians(kot)) / 9.81
print("Kroglo bo neslo {:.2f} metrov daleč".format(s))

from PyQt4 import QtGui, uic

app = QtGui.QApplication([])

dlg = uic.loadUi('top.ui')
dlg.show()
dlg.leHitrost.text()  # Dobiš trenuten text
dlg.leHitrost.clear()

dlg.btIzracunaj.clicked.connect(f) # Na pritisk vežem funkcijo "f"

app.exec()
