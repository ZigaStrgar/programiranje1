from PyQt4 import QtGui, uic, QtCore


class Odstevalnik:
    def __init__(self):
        dlg = self.dlg = uic.loadUi("odstevalnik.ui")
        self.zvok = QtGui.QSound("ringing.wav")
        self.dlg.btIzberiZvok.clicked.connect(self.izberiZvok)
        self.dlg.btZacni.clicked.connect(self.zacni)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.odstej)
        dlg.show()

    def izberiZvok(self):
        n = QtGui.QFileDialog.getOpenFileName(None, "Izberi zvočno datoteko", ".", "Zvočne datoteke (*.mp3 *.wav *m4a)")
        if n:
            self.zvok = QtGui.QSound(n)

    def sprozi(self):
        self.zvok.play()

    def ustavi(self):
        self.zvok.stop()

    def zacni(self):
        self.timer.start()

    def odstej(self):
        dlg = self.dlg
        sek = dlg.sbSek.value()
        minu = dlg.sbMin.value()
        if sek > 0:
            sek -= 1
        elif minu > 0:
            minu -= 1
            sek = 59
        dlg.sbSek.setValue(sek)
        dlg.sbMin.setValue(minu)
        if sek == min == 0:
            self.sprozi()
            self.timer.stop()


app = QtGui.QApplication([])
ods = Odstevalnik()
app.exec()

