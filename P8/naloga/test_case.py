plosca2 = [["J2", "Z1", "J1"], ["V2", "V1", "S2"], ["S1", "Z1", "S1"]]


def visina(plosca):
    return len(plosca)


def sirina(plosca):
    return len(plosca[0])


def polj(plosca):
    return visina(plosca) * sirina(plosca)


def na_plosci(plosca, x, y):
    return sirina(plosca) > x > -1 and visina(plosca) > y > -1


def preberi(plosca, x, y):
    return plosca[y][x][:1], int(plosca[y][x][1:])


def north(x, y, vrednost):
    return x, y - vrednost


def south(x, y, vrednost):
    return x, y + vrednost


def east(x, y, vrednost):
    return x + vrednost, y


def west(x, y, vrednost):
    return x - vrednost, y


def premakni(plosca, x, y):
    smer, vrednost = preberi(plosca, x, y)
    options = {'S': (0, -1), 'J': (0, 1), 'V': (1, 0), 'Z': (-1, 0)}
    return x + vrednost * options[smer][0], y + vrednost * options[smer][1]


def premakni(plosca, x, y):
    smer, vrednost = preberi(plosca, x, y)
    if smer == "S":
        return x, y - vrednost
    if smer == "J":
        return x, y + vrednost
    if smer == "Z":
        return x - vrednost, y
    if smer == "V":
        return x + vrednost, y


def dolzina_poti(plosca, x, y):
    dolzina = 0
    while na_plosci(plosca, x, y):
        x, y = premakni(plosca, x, y)
        dolzina += 1
    return dolzina


# Konec naloge 6
# Naloge 7

def pot(plosca, x, y):
    while na_plosci(plosca, x, y):
        yield x, y
        x, y = premakni(plosca, x, y)


for x, y in pot(plosca2, 0, 0):
    print(x, y)


# Konec naloge 7
# Naloge 8

def izberi(plosca, lastnost):
    polja = set()
    for y in range(0, visina(plosca)):
        for x in range(0, sirina(plosca)):
            if lastnost(plosca, x, y):
                polja.add((x, y))
    return polja


def ciklicno(plosca, x, y):
    prepotovano = []
    while na_plosci(plosca, x, y):
        x, y = premakni(plosca, x, y)
        prepotovano.append((x, y))
        if len(prepotovano) >= polj(plosca):
            return True
    return False


def vrnljivo(plosca, x, y):
    original = (x, y)
    prepotovano = []
    while na_plosci(plosca, x, y):
        x, y = premakni(plosca, x, y)
        prepotovano.append((x, y))
        if len(prepotovano) > polj(plosca) or original in prepotovano:
            break
    if original in prepotovano:
        return True
    return False


def varno(plosca, x, y):
    x, y = premakni(plosca, x, y)
    return na_plosci(plosca, x, y)


def ciklicna(plosca):
    return izberi(plosca, ciklicno)


def vrnljiva(plosca):
    return izberi(plosca, vrnljivo)


def varna(plosca):
    return izberi(plosca, varno)


# Konec naloge 8
# Naloga 9
def dolzina_cikla(plosca, x, y):
    prepotovano = [(x, y)]
    while na_plosci(plosca, x, y):
        x, y = premakni(plosca, x, y)
        if (x, y) in prepotovano:
            ox, oy = x, y
            x, y = premakni(plosca, x, y)
            cikel = 0
            while True:
                cikel += 1
                if x == ox and y == oy:
                    break
                x, y = premakni(plosca, x, y)
            return cikel
        prepotovano.append((x, y))


def veckratnik_ciklov(plosca):
    dolzine = []
    for y in range(0, visina(plosca)):
        for x in range(0, sirina(plosca)):
            dolzina = dolzina_cikla(plosca, x, y)
            if dolzina and dolzina > 1 and dolzina not in dolzine:
                dolzine.append(dolzina)
    veckratnik = 1
    for dolzina in dolzine:
        veckratnik *= dolzina
    return veckratnik


# Konec naloge 9
# Naloga 10, 11

def zasedeno(igralci, x, y):
    for val in igralci:
        if val == (x, y):
            return True
    return False


def kje_odstranim(igralci, koordinate):
    for key, val in enumerate(igralci):
        if val == koordinate:
            return key


def razbij(d):
    return d[0], d[1]


def igra(plosca, zacetki):
    loops = 0
    zacetkik = [x for x in range(0, len(zacetki))]
    while len(zacetki) > 1 and loops < polj(plosca):
        trenutni = 0
        while trenutni < len(zacetki):
            x, y = razbij(zacetki[trenutni])
            x, y = premakni(plosca, x, y)
            if na_plosci(plosca, x, y):
                if zasedeno(zacetki, x, y):
                    odstrani_pri = kje_odstranim(zacetki, (x, y))
                    del zacetki[odstrani_pri]
                    del zacetkik[odstrani_pri]
                    if odstrani_pri < trenutni:
                        trenutni -= 1
                zacetki[trenutni] = (x, y)
            else:
                del zacetki[trenutni]
                del zacetkik[trenutni]
                trenutni -= 1
            trenutni += 1
        loops += 1
    return set(zacetkik)


# Konec naloge 10, 11


import time

start_time = time.time()
i = 0
while i < 1000000:
    veckratnik_ciklov(plosca2)
    i += 1
print("--- %s seconds ---" % (time.time() - start_time))
