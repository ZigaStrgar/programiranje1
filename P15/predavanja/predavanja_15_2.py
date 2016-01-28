import urllib.request
import sys

from PyQt4 import uic, QtGui


class Valute:
    def __init__(self):
        dlg = self.dlg = uic.loadUi("valuta.ui")
        self.preberi_tecajno()
        dlg.show()
        dlg.cbValuta.addItems(list(self.tecaji))
        dlg.cbValuta.currentIndexChanged.connect(self.preracunaj)
        dlg.inVrednost.textChanged.connect(self.preracunaj)

    def preberi_tecajno(self):
        v = None
        for i in range(5):
            try:
                v = urllib.request.urlopen("https://www.nlb.si/services/tecajnica/?type=individuals&format=txt")
                break
            except:
                pass
        if v is None:
            QtGui.QMessageBox.critical(None, "Napaka", "Ne morem pridobiti tečajne liste")
            sys.exit()
        s = v.read().decode('ascii').splitlines()[1:]
        self.tecaji = {}
        for vrstica in s:
            vrstica = vrstica.split()
            self.tecaji[vrstica[5]] = float(vrstica[6].replace(",", "."))

    def preracunaj(self):
        try:
            dlg = self.dlg
            v = float(dlg.inVrednost.text()) * self.tecaji[dlg.cbValuta.currentText()]
            self.dlg.lbZnesek.setText("{:.2f}".format(v))
        except:
            dlg.lbZnesek.setText("...")


app = QtGui.QApplication([])
val = Valute()
app.exec()
