# coding=utf-8
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class QGraphicsViewWMouse(QGraphicsView):
    def __init__(self, *args, **kw):
        super(QGraphicsViewWMouse, self).__init__(*args, **kw)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, ev):
        global miska # Takole se programirajo samo zasilni moduli za Programiranje 1!!!
        miska = ev.x(), ev.y()
        super(QGraphicsViewWMouse, self).mouseMoveEvent(ev)

    def mousePressEvent(self, ev):
        global miska, klik # Takole se programirajo samo zasilni moduli za Programiranje 1!!!
        miska = ev.x(), ev.y()
        klik = True
        super(QGraphicsViewWMouse, self).mousePressEvent(ev)

    def keyPressEvent(self, ev):
        global levo, desno
        super().keyPressEvent(ev)
        levo = ev.key() == Qt.Key_Left
        desno = ev.key() == Qt.Key_Right

    def keyReleaseEvent(self, ev):
        global levo, desno
        super().keyReleaseEvent(ev)
        levo = desno = False


app=QApplication([])
widget = QDialog()
widget.setWindowTitle("Janezovo zasilno platno")
widget.setLayout(QVBoxLayout())
widget.layout().setMargin(2)
widget.scene = QGraphicsScene(widget)
widget.scene.setBackgroundBrush(Qt.black)
widget.view = QGraphicsViewWMouse(widget.scene, widget)
widget.view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
widget.view.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
widget.view.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
widget.layout().addWidget(widget.view)
widget.resize(800, 500)
widget.scene.setSceneRect(0, 0, widget.view.width(), widget.view.height())
widget.view.setSceneRect(0, 0, widget.view.width(), widget.view.height())
widget.show()
widget.raise_()
maxX = widget.view.width()
maxY = widget.view.height()

miska = maxX/2, maxY/2
klik = False
barve = bela, crna, rdeca, zelena, modra, vijolicna, rumena, siva, rjava = Qt.white, Qt.black, Qt.red, Qt.green, Qt.blue, Qt.magenta, Qt.yellow, Qt.gray, Qt.darkRed

barva = QColor

obnavljaj = True

def nakljucna_barva():
    from random import randint
    return barva(randint(0, 255), randint(0, 255), randint(0, 255))

def nakljucne_koordinate():
    from random import randint
    return randint(0, maxX), randint(0, maxY)

def obnovi():
    """
    Obnovi sliko na zaslonu.

    Funkcije ni potrebno klicati, če je 'obnavljaj' nastavljen na True. Prav
    tako funkcija 'cakaj' sama pokliče tudi 'obnovi'.
    """
    widget.scene.update()
    qApp.processEvents()

def cakaj(t):
    """Počaka t sekund."""
    import time
    obnovi()
    time.sleep(t)

def barvaOzadja(barva):
    """Nastavi barvo ozadja."""
    widget.scene.setBackgroundBrush(barva)
    if obnavljaj:
        obnovi()

def crta(x0, y0, x1, y1, barva=bela, sirina=1):
    """Potegni črto med podanima točkama."""
    crta = widget.scene.addLine(0, 0, x1-x0, y1-y0, QPen(QBrush(barva), sirina))
    crta.setPos(x0, y0)
    if obnavljaj:
        obnovi()
    return crta

def tocka(x, y, barva=bela):
    """Nariše točko na podanih koordinatah."""
    if obnavljaj:
        obnovi()
    return widget.scene.addLine(x, y, x, y, QPen(QBrush(barva), 1))

def elipsa(x, y, rx, ry, barva=bela, sirina=1):
    """Nariše elipso s središčem v (x, y) in polmeroma rx in ry."""
    elipsa = widget.scene.addEllipse(-rx, -ry, 2*rx, 2*ry, QPen(QBrush(barva), sirina))
    elipsa.setPos(x, y)
    if obnavljaj:
        obnovi()
    return elipsa

def krog(x, y, r, barva=bela, sirina=1):
    """Nariše krog s polmerom r in središčem v (x, y)."""
    elipsa = widget.scene.addEllipse(-r, -r, 2*r, 2*r, QPen(QBrush(barva), sirina))
    elipsa.setPos(x, y)
    if obnavljaj:
        obnovi()
    return elipsa

def besedilo(x, y, txt, barva=bela, velikost=20, pisava="Arial"):
    """Izpiše besedilo txt; koordinati podajata zgornji levi vogal."""
    font = QFont(pisava)
    font.setPixelSize(velikost)
    txt = widget.scene.addText(txt, font)
    txt.setPos(x, y)
    txt.setDefaultTextColor(barva)
    if obnavljaj:
        obnovi()
    return txt

def slika(x, y, fname):
    """
    Naloži sliko iz datoteke fname in jo postavi na sliko tako, da je
    zgornji levi vogal na koordinatah (x, y)
    """
    pict = QPixmap(fname)
    pixmap = widget.scene.addPixmap(pict)
    pixmap.setPos(x, y)
    rect = pixmap.boundingRect()
    pixmap.translate(-rect.width() / 2, -rect.height() / 2)
    if obnavljaj:
        obnovi()
    return pixmap

def pobrisi():
    widget.scene.clear()
    obnovi()

def odstrani(stvar):
    widget.scene.removeItem(stvar)

def stoj():
    qApp.exec_()

levo = desno = False

