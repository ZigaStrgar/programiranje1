import unittest


# Ogrevanje
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


# Konec ogrevanja
# Naloge 6
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
    options = {'S': north, 'J': south, 'V': east, 'Z': west}
    return options[smer](x, y, vrednost)


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
            cikel = 1
            while True:
                x, y = premakni(plosca, x, y)
                if x == ox and y == oy:
                    break
                cikel += 1
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
    loops = 0  # Potrebno za oceno 11
    zacetkik = [x for x in range(len(zacetki))] # Zaporedni indexi igralcev
    while len(zacetki) > 1 and loops < polj(plosca):
        start = 0
        while start < len(zacetki):
            x, y = razbij(zacetki[start])
            x, y = premakni(plosca, x, y)
            if na_plosci(plosca, x, y):
                if zasedeno(zacetki, x, y):
                    odstrani_pri = kje_odstranim(zacetki, (x, y))
                    del zacetki[odstrani_pri]
                    del zacetkik[odstrani_pri]
                    if odstrani_pri < start:
                        start -= 1  # Odstranim za trenutnim. Brez tega preskočim enega
                zacetki[start] = (x, y)
            else:
                del zacetki[start]
                del zacetkik[start]
                start -= 1
            start += 1
        loops += 1
    return set(zacetkik)


# Konec naloge 10, 11


class TestOcena05(unittest.TestCase):
    def test_visina(self):
        self.assertEqual(visina([["V1", "V1"], ["V2", "V2"], ["V3", "V3"]]), 3)

        self.assertEqual(visina([["V1", "V1"], ["V2", "V2"], ["V3", "V3"], ["V4", "V4"], ["V4", "V4"]]), 5)

        self.assertEqual(visina([["V1", "V1", "V1", "V1", "V1"]]), 1)

        self.assertEqual(visina([["V1"]]), 1)

    def test_sirina(self):
        self.assertEqual(sirina([["V1", "V1"], ["V2", "V2"], ["V3", "V3"]]), 2)

        self.assertEqual(sirina([["V1", "V1"], ["V2", "V2"], ["V3", "V3"], ["V4", "V4"], ["V4", "V2"]]), 2)

        self.assertEqual(sirina([["V1", "V1", "V1", "V1", "V1"]]), 5)

        self.assertEqual(sirina([["V1", "V1", "V1", "V1", "V1"], ["V2", "V2", "V2", "V2", "V2"]]), 5)

        self.assertEqual(sirina([["V1", "V2", "V3", "V4", "V5"]]), 5)

        self.assertEqual(sirina([["V1"]]), 1)

    def test_polj(self):
        self.assertEqual(polj([["V1", "V1"], ["V2", "V2"], ["V3", "V3"]]), 6)

        self.assertEqual(polj([["V1", "V1"], ["V2", "V2"], ["V3", "V3"], ["V4", "V4"], ["V4", "V2"]]), 10)

        self.assertEqual(polj([["V1", "V1", "V1", "V1", "V1"]]), 5)

        self.assertEqual(polj([["V1", "V1", "V1", "V1", "V1"], ["V2", "V2", "V2", "V2", "V2"]]), 10)

        self.assertEqual(polj([["V1", "V2", "V3", "V4", "V5"]]), 5)

        self.assertEqual(polj([["V1"]]), 1)

    def test_na_plosci(self):
        plosca = [["V1", "V1"], ["V2", "V2"], ["V3", "V3"]]
        self.assertTrue(na_plosci(plosca, 0, 0))
        self.assertTrue(na_plosci(plosca, 1, 0))
        self.assertTrue(na_plosci(plosca, 0, 1))
        self.assertTrue(na_plosci(plosca, 1, 2))

        self.assertFalse(na_plosci(plosca, 0, 3))
        self.assertFalse(na_plosci(plosca, 2, 0))

        self.assertFalse(na_plosci(plosca, 1, 5))
        self.assertFalse(na_plosci(plosca, 1, -5))
        self.assertFalse(na_plosci(plosca, -10, -5))
        self.assertFalse(na_plosci(plosca, 10, 5))
        self.assertFalse(na_plosci(plosca, -10, 0))

        plosca = [["V1"] * 5] * 12
        self.assertTrue(na_plosci(plosca, 4, 11))
        self.assertTrue(na_plosci(plosca, 0, 0))
        self.assertFalse(na_plosci(plosca, 5, 11))
        self.assertFalse(na_plosci(plosca, 4, 12))
        self.assertFalse(na_plosci(plosca, 5, 12))
        self.assertFalse(na_plosci(plosca, -1, -1))

    def test_preberi(self):
        plosca = [["J2", "Z12", "J1"], ["V2", "V1", "S2"], ["S1", "J1345", "S1"]]
        self.assertEqual(preberi(plosca, 0, 1), ("V", 2))
        self.assertEqual(preberi(plosca, 2, 1), ("S", 2))
        self.assertEqual(preberi(plosca, 0, 2), ("S", 1))
        self.assertEqual(preberi(plosca, 1, 0), ("Z", 12))
        self.assertEqual(preberi(plosca, 1, 2), ("J", 1345))


class Plosce(unittest.TestCase):
    def setUp(self):
        self.plosca1 = [["J2", "Z1", "J1"], ["V2", "V1", "S2"], ["S1", "Z1", "S1"]]

        self.plosca2 = [["J2", "Z1", "V1"], ["S1", "V1", "J1"], ["S1", "S1", "Z1"]]

        self.plosca3 = [["J1", "J2"], ["J1", "V1"], ["S1", "S1"]]

        self.plosca4 = [["V2", "V1", "Z1", "J1"]]

        self.plosca5 = [["J2"], ["J1"], ["S1"], ["V1"]]

        self.vsa = {(x, y) for x in range(3) for y in range(3)}


class TestOcena06(Plosce):
    def test_premakni(self):
        plosca = [["J2", "Z12", "J1"], ["V2", "V1", "S2"], ["S1", "J1345", "S1"]]
        self.assertTupleEqual(premakni(plosca, 0, 0), (0, 2))
        self.assertTupleEqual(premakni(plosca, 1, 0), (-11, 0))
        self.assertTupleEqual(premakni(plosca, 2, 0), (2, 1))
        self.assertTupleEqual(premakni(plosca, 0, 1), (2, 1))
        self.assertTupleEqual(premakni(plosca, 1, 1), (2, 1))
        self.assertTupleEqual(premakni(plosca, 2, 1), (2, -1))
        self.assertTupleEqual(premakni(plosca, 0, 2), (0, 1))
        self.assertTupleEqual(premakni(plosca, 1, 2), (1, 1347))
        self.assertTupleEqual(premakni(plosca, 2, 2), (2, 1))

    def test_dolzina_poti(self):
        plosca = self.plosca1
        self.assertEqual(dolzina_poti(plosca, 0, 0), 4)
        self.assertEqual(dolzina_poti(plosca, 1, 0), 5)
        self.assertEqual(dolzina_poti(plosca, 2, 0), 2)
        self.assertEqual(dolzina_poti(plosca, 0, 1), 2)
        self.assertEqual(dolzina_poti(plosca, 1, 1), 2)
        self.assertEqual(dolzina_poti(plosca, 2, 1), 1)
        self.assertEqual(dolzina_poti(plosca, 0, 2), 3)
        self.assertEqual(dolzina_poti(plosca, 1, 2), 4)
        self.assertEqual(dolzina_poti(plosca, 2, 2), 2)

        plosca = [["J2", "Z1"]]
        self.assertEqual(dolzina_poti(plosca, 0, 0), 1)
        self.assertEqual(dolzina_poti(plosca, 1, 0), 2)

        self.assertEqual(dolzina_poti([["Z2"]], 0, 0), 1)


class TestOcena07(Plosce):
    def test_pot(self):
        potl = lambda *x: list(pot(*x))

        plosca = self.plosca1
        self.assertEqual(potl(plosca, 0, 0), [(0, 0), (0, 2), (0, 1), (2, 1)])
        self.assertEqual(potl(plosca, 1, 0), [(1, 0), (0, 0), (0, 2), (0, 1), (2, 1)])
        self.assertEqual(potl(plosca, 2, 0), [(2, 0), (2, 1)])
        self.assertEqual(potl(plosca, 0, 1), [(0, 1), (2, 1)])
        self.assertEqual(potl(plosca, 1, 1), [(1, 1), (2, 1)])
        self.assertEqual(potl(plosca, 2, 1), [(2, 1)])
        self.assertEqual(potl(plosca, 0, 2), [(0, 2), (0, 1), (2, 1)])
        self.assertEqual(potl(plosca, 1, 2), [(1, 2), (0, 2), (0, 1), (2, 1)])
        self.assertEqual(potl(plosca, 2, 2), [(2, 2), (2, 1)])

        plosca = [["J2", "Z1"]]
        self.assertEqual(potl(plosca, 0, 0), [(0, 0)])
        self.assertEqual(potl(plosca, 1, 0), [(1, 0), (0, 0)])

        self.assertEqual(potl([["Z2"]], 0, 0), [(0, 0)])


class TestOcena08(Plosce):
    def test_ciklicno(self):
        for x in range(3):
            for y in range(3):
                self.assertFalse(ciklicno(self.plosca1, x, y))
                if (x, y) != (2, 0):
                    self.assertTrue(ciklicno(self.plosca2, x, y))
        self.assertFalse(ciklicno(self.plosca2, 2, 0))

        self.assertTrue(ciklicno(self.plosca3, 0, 0))
        self.assertTrue(ciklicno(self.plosca3, 0, 1))
        self.assertTrue(ciklicno(self.plosca3, 0, 2))
        self.assertFalse(ciklicno(self.plosca3, 1, 0))
        self.assertFalse(ciklicno(self.plosca3, 1, 1))
        self.assertFalse(ciklicno(self.plosca3, 1, 2))

        self.assertTrue(ciklicno(self.plosca4, 0, 0))
        self.assertTrue(ciklicno(self.plosca4, 1, 0))
        self.assertTrue(ciklicno(self.plosca4, 2, 0))
        self.assertFalse(ciklicno(self.plosca4, 3, 0))

        self.assertTrue(ciklicno(self.plosca5, 0, 0))
        self.assertTrue(ciklicno(self.plosca5, 0, 1))
        self.assertTrue(ciklicno(self.plosca5, 0, 2))
        self.assertFalse(ciklicno(self.plosca5, 0, 3))

    def test_ciklicna(self):
        self.assertSetEqual(ciklicna(self.plosca1), set())
        self.assertSetEqual(ciklicna(self.plosca2), self.vsa - {(2, 0)})
        self.assertSetEqual(ciklicna(self.plosca3), {(0, 0), (0, 1), (0, 2)})
        self.assertSetEqual(ciklicna(self.plosca4), {(0, 0), (1, 0), (2, 0)})
        self.assertSetEqual(ciklicna(self.plosca5), {(0, 0), (0, 1), (0, 2)})

    def test_vrnljivo(self):
        for x in range(3):
            for y in range(3):
                self.assertFalse(vrnljivo(self.plosca1, x, y))
                if (x, y) not in {(1, 0), (2, 0)}:
                    self.assertTrue(vrnljivo(self.plosca2, x, y))
                else:
                    self.assertFalse(vrnljivo(self.plosca2, x, y))
        self.assertFalse(vrnljivo(self.plosca3, 0, 0))
        self.assertTrue(vrnljivo(self.plosca3, 0, 1))
        self.assertTrue(vrnljivo(self.plosca3, 0, 2))
        self.assertFalse(vrnljivo(self.plosca3, 1, 0))
        self.assertFalse(vrnljivo(self.plosca3, 1, 1))
        self.assertFalse(vrnljivo(self.plosca3, 1, 2))

        self.assertFalse(vrnljivo(self.plosca4, 0, 0))
        self.assertTrue(vrnljivo(self.plosca4, 1, 0))
        self.assertTrue(vrnljivo(self.plosca4, 2, 0))
        self.assertFalse(vrnljivo(self.plosca4, 3, 0))

        self.assertFalse(vrnljivo(self.plosca5, 0, 0))
        self.assertTrue(vrnljivo(self.plosca5, 0, 1))
        self.assertTrue(vrnljivo(self.plosca5, 0, 2))
        self.assertFalse(vrnljivo(self.plosca5, 0, 3))

    def test_vrnljiva(self):
        self.assertSetEqual(vrnljiva(self.plosca1), set())
        self.assertSetEqual(vrnljiva(self.plosca2), self.vsa - {(1, 0), (2, 0)})
        self.assertSetEqual(vrnljiva(self.plosca3), {(0, 1), (0, 2)})
        self.assertSetEqual(vrnljiva(self.plosca4), {(1, 0), (2, 0)})
        self.assertSetEqual(vrnljiva(self.plosca5), {(0, 1), (0, 2)})

    def test_varno(self):
        for x in range(3):
            for y in range(3):
                if (x, y) != (2, 1):
                    self.assertTrue(varno(self.plosca1, x, y))
                if (x, y) != (2, 0):
                    self.assertTrue(varno(self.plosca2, x, y))
        self.assertFalse(varno(self.plosca1, 2, 1))
        self.assertFalse(varno(self.plosca2, 2, 0))

    def test_varna(self):
        self.assertSetEqual(varna(self.plosca1), self.vsa - {(2, 1)})
        self.assertSetEqual(varna(self.plosca2), self.vsa - {(2, 0)})
        self.assertSetEqual(varna(self.plosca3), {(0, 0), (1, 0), (0, 1), (0, 2), (1, 2)})
        self.assertSetEqual(varna(self.plosca4), {(0, 0), (1, 0), (2, 0)})
        self.assertSetEqual(varna(self.plosca5), {(0, 0), (0, 1), (0, 2)})


class TestOcena_09(Plosce):
    def test_dolzina_cikla(self):
        for x in range(3):
            for y in range(3):
                self.assertIsNone(dolzina_cikla(self.plosca1, x, y))
                if x == 0 or (x, y) == (1, 0):
                    self.assertEqual(dolzina_cikla(self.plosca2, x, y), 3)
                elif (x, y) == (2, 0):
                    self.assertIsNone(dolzina_cikla(self.plosca2, x, y))
                else:
                    self.assertEqual(dolzina_cikla(self.plosca2, x, y), 4)

        self.assertEqual(dolzina_cikla(self.plosca3, 0, 0), 2)
        self.assertEqual(dolzina_cikla(self.plosca3, 0, 1), 2)
        self.assertEqual(dolzina_cikla(self.plosca3, 0, 2), 2)
        self.assertIsNone(dolzina_cikla(self.plosca3, 1, 0))
        self.assertIsNone(dolzina_cikla(self.plosca3, 1, 1))
        self.assertIsNone(dolzina_cikla(self.plosca3, 1, 2))

        self.assertEqual(dolzina_cikla(self.plosca4, 0, 0), 2)
        self.assertEqual(dolzina_cikla(self.plosca4, 1, 0), 2)
        self.assertEqual(dolzina_cikla(self.plosca4, 2, 0), 2)
        self.assertIsNone(dolzina_cikla(self.plosca4, 3, 0))

        self.assertEqual(dolzina_cikla(self.plosca5, 0, 0), 2)
        self.assertEqual(dolzina_cikla(self.plosca5, 0, 1), 2)
        self.assertEqual(dolzina_cikla(self.plosca5, 0, 2), 2)
        self.assertIsNone(dolzina_cikla(self.plosca5, 0, 3))

    def test_veckratnik_ciklov(self):
        self.assertEqual(veckratnik_ciklov(self.plosca1), 1)
        self.assertEqual(veckratnik_ciklov(self.plosca2), 12)
        self.assertEqual(veckratnik_ciklov(self.plosca3), 2)
        self.assertEqual(veckratnik_ciklov(self.plosca4), 2)
        self.assertEqual(veckratnik_ciklov(self.plosca5), 2)


class TestOcena_10(Plosce):
    def test_igra(self):
        # samo en igralec / single player
        self.assertTrue(igra(self.plosca1, [(2, 0)]) in [0, {0}])

        # prvi izloci drugega, se preden se le-ta premakne
        # the first eliminates the second even before the latter moves
        self.assertTrue(igra(self.plosca1, [(1, 0), (0, 0)]) in [0, {0}])

        # drugi "izloci" prvega  / the second removes the first
        self.assertTrue(igra(self.plosca1, [(2, 0), (2, 2)]) in [1, {1}])
        self.assertTrue(igra(self.plosca1, [(2, 2), (2, 0)]) in [1, {1}])

        # tisti, ki so blizje, padejo cez rob
        # those closer to the path fall off the board
        self.assertTrue(igra(self.plosca1, [(0, 2), (2, 2), (2, 0)]) in [0, {0}])
        self.assertTrue(igra(self.plosca1, [(2, 2), (0, 2), (2, 0)]) in [1, {1}])
        self.assertTrue(igra(self.plosca1, [(2, 2), (2, 0), (0, 2)]) in [2, {2}])

        # drugi "izloci" prvega  / the second removes the first
        self.assertTrue(igra(self.plosca2, [(0, 1), (1, 0)]) in [1, {1}])
        self.assertTrue(igra(self.plosca2, [(1, 0), (0, 1)]) in [1, {1}])

        # drugi "izloci" prvega, eden pa pade čez
        # the second removes the first, and one falls off
        self.assertTrue(igra(self.plosca2, [(1, 0), (0, 1), (2, 0)]) in [1, {1}])
        self.assertTrue(igra(self.plosca2, [(2, 0), (1, 0), (0, 1)]) in [2, {2}])

        self.assertTrue(igra(self.plosca3, [(0, 0), (0, 1)]) in [0, {0}])
        self.assertTrue(igra(self.plosca3, [(0, 1), (0, 0)]) in [0, {0}])
        self.assertTrue(igra(self.plosca3, [(0, 1), (0, 2)]) in [0, {0}])
        self.assertTrue(igra(self.plosca3, [(0, 2), (0, 1)]) in [0, {0}])
        self.assertTrue(igra(self.plosca3, [(0, 2), (0, 0)]) in [1, {1}])
        self.assertTrue(igra(self.plosca3, [(0, 0), (0, 2)]) in [1, {1}])

        self.assertTrue(igra(self.plosca3, [(0, 0), (0, 2), (1, 0)]) in [1, {1}])
        self.assertTrue(igra(self.plosca3, [(0, 0), (1, 0), (0, 2)]) in [2, {2}])
        self.assertTrue(igra(self.plosca3, [(1, 0), (0, 0), (0, 2)]) in [2, {2}])


class TestOcena_11(Plosce):
    def test_igra(self):
        self.assertSetEqual(igra(self.plosca2, [(1, 0), (0, 1), (2, 0), (2, 2)]), {1, 3})
        self.assertSetEqual(igra(self.plosca2, [(1, 0), (0, 1), (2, 0), (2, 2), (1, 2)]), {1, 3})
        self.assertSetEqual(igra(self.plosca2, [(1, 0), (0, 1), (2, 0), (2, 2), (1, 2), (1, 1)]), {1, 3, 5})
        self.assertSetEqual(igra(self.plosca2, [(1, 1), (2, 1), (2, 2), (1, 2)]), {0, 2})


if __name__ == "__main__":
    unittest.main()
