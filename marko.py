from PyQt4.QtGui import QColor, QDesktopWidget


def raz(a, b):    # Vrne razdaljo med točkama a(x, y) in b(x, y)
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def trikotnik(a, b, c,
              i=True):        # Nariše trikotnik med točkami a(x, y), b(x, y) in c(x, y)
    barvnaCrta(a, b, i)
    barvnaCrta(b, c, i)
    barvnaCrta(c, a, i)


def barvnaCrta(a, b,
               i):    # Določi barvo črte med a(x, y) in b(x, y) ter jo nariše
    a1 = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)        # a1 je sredina črte
    r_a0 = raz(a1,
               a0) * 255 / d            # rdeča barva je odvisna od oddaljenosti a1 od ogljišča a0
    g_a0 = raz(a1, b0) * 255 / d            # zelena -> oddaljenost od b0
    b_a0 = raz(a1, c0) * 255 / d            # modra -> oddaljenost od c0
    if not i:                            # Naredi negativ barve
        r_a0 = 255 - r_a0
        g_a0 = 255 - g_a0
        b_a0 = 255 - b_a0
    risar.crta(a[0], a[1], b[0], b[1], QColor(r_a0, b_a0, g_a0))


def serp(a1, b1, c1):
    l = [[a1, b1, c1,
          True]]    # l = FIFO (first in, first out) stack, rekurzija navadno uporablja LIFO (last in, first out) stack
    delay = 0.5
    m = 1
    n = 1
    p = 1
    while l:
        i = l.pop(0)
        a = i[0]
        b = i[1]
        c = i[2]
        a1 = (
        (a[0] + b[0]) / 2, (a[1] + b[1]) / 2)        # Izračuna sredine stranic
        b1 = ((b[0] + c[0]) / 2, (b[1] + c[1]) / 2)
        c1 = ((c[0] + a[0]) / 2, (c[1] + a[1]) / 2)
        trikotnik(a1, b1, c1, i[3])        # Nariše trikotnik
        l.append([a, a1, c1,
                  i[3]])        # Na stack doda tri nove trikotnike (fraktale)
        l.append([b, b1, a1, i[3]])
        l.append([c, c1, b1, i[3]])
        if fill == 'Y':
            l.append([a1, b1, c1, not i[
                3]])    # Doda še četrti (notranji) trikotnik, ki ga izriše z negativno barvo (zato not i[3])
        m -= 1
        if delay >= 0.005:            # Delay pri izrisovanju
            risar.cakaj(delay)
            p = 1
        elif m % p == 0:
            risar.obnovi()
        if not m:
            if fill == 'Y':
                n *= 4
                delay /= 4
                p *= 4
            else:
                n *= 3
                delay /= 3
                p *= 3
            m = n


def sierpinski(a1, b1, c1):
    risar.obnavljaj = True
    l = [[a1, b1, c1,
          True]]    # l = FIFO (first in, first out) stack, rekurzija navadno uporablja LIFO (last in, first out) stack
    while l:
        i = l.pop(0)    # Vzame prvi element s stacka
        a = i[
            0]    # Prepiše ogljiča iz seznama v ločene spremenljivke, zaradi preglednosti
        b = i[1]
        c = i[2]
        a1 = (
        (a[0] + b[0]) / 2, (a[1] + b[1]) / 2)        # Izračuna sredine stranic
        b1 = ((b[0] + c[0]) / 2, (b[1] + c[1]) / 2)
        c1 = ((c[0] + a[0]) / 2, (c[1] + a[1]) / 2)
        trikotnik(a1, b1, c1, i[3])        # Nariše trikotnik
        l.append([a, a1, c1,
                  i[3]])        # Na stack doda tri nove trikotnike (fraktale)
        l.append([b, b1, a1, i[3]])
        l.append([c, c1, b1, i[3]])
        if fill == 'Y':
            l.append([a1, b1, c1, not i[
                3]])    # Doda še četrti (notranji) trikotnik, ki ga izriše z negativno barvo (zato not i[3])


def pozeni():    # Požene program
    var = "Y" #input('Izrisuj po segmentih? (Y/N) ')    # Prebere način izrisovanja
    global fill
    fill = "N" #input(
        #'Zapolni notranji trikotnik? (Y/N) ')    # Prebere način izrisovanja
    init()        # Kliče inicializacijo (določi spremenljivke, velikost kanvasa, naslov, ...
    global a0, b0, c0    # Definira ogljišča osnovnega trikotnika kot globalne spremenljivke (dostopne ostalim funkcijam
    a0 = (10, d * (
    3 ** 0.5) / 2 + 10)    # Določi ogljišča enakostraničnega trikotnika
    b0 = (10 + d, d * (3 ** 0.5) / 2 + 10)
    c0 = (d / 2 + 10, 10)
    trikotnik(a0, b0, c0)    # Nariše osnovni trikotnik
    if var == 'Y':            # Požene fraktalizacijo
        serp(a0, b0, c0)
    else:
        sierpinski(a0, b0, c0)
    risar.stoj()

# Preostanek kode lahko ignoriraš

def init():
    global risar
    import risar

    global d        # Naredi dolžino stranice globalno dostopno

    screen = QDesktopWidget().screenGeometry()
    w, h = screen.width() - 25, screen.height() - 25

    print(w, h)
    if w * (3 ** 0.5) / 2 > h:        # Izračuna maksimalno velikost trikotnika
        d = 2 * h / (3 ** 0.5)
        w = d + 25
        h += 25
    else:
        d = w
        w += 25
        h = w * (3 ** 0.5) / 2 + 25

    risar.obnavljaj = False        # Nastavi risar, da ne izriše novih trikotnikov avtomatično
    risar.widget.resize(w, h)    # Nastavi velikost risarja
    risar.widget.setWindowTitle("Fraktali")        # Ime okna

    setattr(risar.widget, "closeEvent",
            exit)    # Prepiše privzeto funkcijo za zapiranje okna s funkcijo, ki zapre celoten program (monkey-patching način)

pozeni()    # Požene program