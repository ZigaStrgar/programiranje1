from PyQt4 import QtGui, uic
from math import *


class Temperature:
    def __init__(self):
        dlg = self.dlg = uic.loadUi('temp.ui')
        dlg.show()
        dlg.inTemp.textChanged.connect(self.calculate)

    def calculate(self):
        dlg = self.dlg
        c = 5 / 9 * (float(dlg.inTemp.text()) - 32)
        dlg.lbRez.setText("{:.2f}".format(c))


class Convert:
    def __init__(self):
        dlg = self.dlg = uic.loadUi('convert.ui')
        dlg.show()
        dlg.inNumber.textChanged.connect(self.convert)

    def convert(self):
        dlg = self.dlg
        binary = dlg.inNumber.text()
        if binary.find(".") != -1:
            binary = binary.split(".")
            whole = int(binary[0], 2)
            fraction = 0
            for i, e in enumerate(binary[1]):
                if e == "1":
                    fraction += 1 / 2 ** (i + 1)
        else:
            fraction = 0
            whole = int(binary, 2)
        dlg.lbRez.setText("{}".format(whole + fraction))


class Kalkulator:
    def __init__(self):
        dlg = self.dlg = uic.loadUi('calc.ui')
        dlg.show()
        dlg.inExprs.returnPressed.connect(self.calculate)

    def calculate(self):
        dlg = self.dlg
        expr = dlg.inExprs.text()
        rez = eval(expr)
        dlg.tBrowser.append("{} = <strong>{}</strong>".format(expr, rez))
        dlg.inExprs.clear()


app = QtGui.QApplication([])
calc = Kalkulator()
app.exec()
