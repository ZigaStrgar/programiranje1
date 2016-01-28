import unittest


def woman(name):
    return name.endswith("a")


def vstavi_teze(names, weights):
    i = 0
    for index, name in enumerate(names):
        if not woman(name):
            names[index] = weights[i]
            i += 1


def obstaja(give, get, offers):
    for gives, gets in offers:
        if give in gives and get in gets:
            return True
    return False


def menjave(s, offers):
    for give, get in zip(s, s[1:]):
        if not obstaja(give, get, offers):
            return False
    return True


def izmenjavanje(names):
    return len(names) < 2 or (names[1][-1] == "a") != (names[0][-1] == "a") and izmenjavanje(names[1:])


def spremeni_smer(current, move):
    angles = {"U": 360, "L": 270, "R": 90, "D": 180}
    change = {"U": 360, "L": -90, "R": 90, "D": 180, "F": 0}
    new = angles[current] + change[move]
    if new >= 360:
        new -= 360
    for path, angle in angles.items():
        if angle == new:
            return path
    return "U"


def korak(x, y, move):
    moves = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    return x + moves[move][0], y + moves[move][1]


def potuj(x, y, smer, plosca):
    pot = [(x, y)]
    while 0 <= x < len(plosca[0]) and 0 <= y < len(plosca) and (x, y) not in pot[:-1]:
        smer = spremeni_smer(smer, plosca[y][x])
        x, y = korak(x, y, smer)
        pot.append((x, y))
    return pot


class Knjizica:
    def __init__(self):
        self.rented = {}

    def izposodi(self, title, date):
        self.rented[title] = date

    def izposojeno(self):
        return {title for title in self.rented}

    def vrni(self, title):
        del self.rented[title]

    def zamudnina(self, today):
        zamudnina = 0
        for title, date in self.rented.items():
            if today > (date + 21):
                zamudnina += today - (date + 21)
        return zamudnina


class N1VstaviTeze(unittest.TestCase):
    def test_vstavi_teze(self):
        imena = ["Adam", "Eva", "Kajn", "Abel"]
        teze = [87, 86, 75]
        self.assertIsNone(vstavi_teze(imena, teze), "vstavi_teze naj ne vrača rezultate")
        self.assertEqual(teze, [87, 86, 75], "Ne spreminjaj seznama tež!")
        self.assertEqual(imena, [87, "Eva", 86, 75])

        imena = ["Adam", "Kajn", "Abel"]
        teze = [87, 86, 75]
        vstavi_teze(imena, teze)
        self.assertEqual(teze, [87, 86, 75], "Ne spreminjaj seznama tež!")
        self.assertEqual(imena, [87, 86, 75])

        imena = ["Adam", "Kajn"]
        teze = [87, 86]
        vstavi_teze(imena, teze)
        self.assertEqual(teze, [87, 86], "Ne spreminjaj seznama tež!")
        self.assertEqual(imena, [87, 86])

        imena = ["Adam"]
        teze = [87]
        vstavi_teze(imena, teze)
        self.assertEqual(teze, [87], "Ne spreminjaj seznama tež!")
        self.assertEqual(imena, [87])

        imena = ["Adam", "Eva"]
        teze = [87]
        vstavi_teze(imena, teze)
        self.assertEqual(teze, [87], "Ne spreminjaj seznama tež!")
        self.assertEqual(imena, [87, "Eva"])

        imena = ["Eva", "Adam"]
        teze = [87]
        vstavi_teze(imena, teze)
        self.assertEqual(teze, [87], "Ne spreminjaj seznama tež!")
        self.assertEqual(imena, ["Eva", 87])

        imena = ["Eva"]
        teze = []
        vstavi_teze(imena, teze)
        self.assertEqual(teze, [], "Ne spreminjaj seznama tež!")
        self.assertEqual(imena, ["Eva"])


class N2Trgovanje(unittest.TestCase):
    def test_primer_iz_izpita(self):
        ponudbe = [({"deska", "steklenica"}, {"pašteta"}), ({"knjiga", "vilice"}, {"sveča", "deska", "papir"}),
                   ({"riba", "pašteta"}, {"tipkovnica", "zaslon"})]

        self.assertTrue(obstaja("deska", "pašteta", ponudbe))
        self.assertFalse(obstaja("papir", "pašteta", ponudbe))

        self.assertTrue(menjave(["deska", "pašteta", "zaslon"], ponudbe))
        self.assertFalse(menjave(["vilice", "papir", "pašteta", "tipkovnica"], ponudbe))

    def test_obstaja(self):
        ponudbe = [(set("ga"), set("ijk")), (set("abc"), set("def")), (set("efc"), set("bg"))]

        self.assertTrue(obstaja("a", "i", ponudbe))
        self.assertTrue(obstaja("a", "j", ponudbe))
        self.assertTrue(obstaja("g", "k", ponudbe))
        self.assertTrue(obstaja("c", "g", ponudbe))

        self.assertFalse(obstaja("k", "g", ponudbe))
        self.assertFalse(obstaja("x", "y", ponudbe))

    def test_trgovanje(self):
        ponudbe = [(set("ga"), set("ijk")), (set("abc"), set("def")), (set("efc"), set("bg"))]
        self.assertTrue(menjave(list("aegi"), ponudbe))
        self.assertTrue(menjave(list("aeg"), ponudbe))
        self.assertTrue(menjave(list("ae"), ponudbe))
        self.assertTrue(menjave(list("a"), ponudbe))
        self.assertTrue(menjave(list("egi"), ponudbe))
        self.assertTrue(menjave(list("gi"), ponudbe))
        self.assertTrue(menjave(list("eg"), ponudbe))
        self.assertTrue(menjave(list("cfgk"), ponudbe))
        self.assertTrue(menjave(list("cgk"), ponudbe))
        self.assertTrue(menjave(list("fgj"), ponudbe))
        self.assertTrue(menjave(list("cfb"), ponudbe))

        self.assertFalse(menjave(list("ag"), ponudbe))
        self.assertFalse(menjave(list("ga"), ponudbe))
        self.assertFalse(menjave(list("adg"), ponudbe))
        self.assertFalse(menjave(list("aej"), ponudbe))
        self.assertFalse(menjave(list("acgj"), ponudbe))

        ponudbe = [(set("123"), set("456"))]
        self.assertTrue(menjave("16", ponudbe))
        self.assertTrue(menjave("34", ponudbe))
        self.assertFalse(menjave("12", ponudbe))
        self.assertFalse(menjave("56", ponudbe))

        ponudbe = []
        self.assertTrue(menjave("e", ponudbe))
        self.assertFalse(menjave("eg", ponudbe))


class N3Izmenjavanje(unittest.TestCase):
    def test_izmenjavanje(self):
        self.assertTrue(izmenjavanje(["Ana", "Benjamin", "Cilka", "Daniel"]))
        self.assertTrue(izmenjavanje(["Ana", "Benjamin", "Cilka"]))
        self.assertTrue(izmenjavanje(["Ana", "Benjamin"]))
        self.assertTrue(izmenjavanje(["Ana"]))
        self.assertTrue(izmenjavanje(["Benjamin", "Cilka", "Daniel", "Ana"]))
        self.assertTrue(izmenjavanje(["Benjamin", "Cilka", "Daniel"]))
        self.assertTrue(izmenjavanje(["Benjamin", "Cilka"]))
        self.assertTrue(izmenjavanje(["Benjamin"]))

        self.assertFalse(izmenjavanje(["Ana", "Cilka"]))
        self.assertFalse(izmenjavanje(["Ana", "Cilka", "Benjamin"]))
        self.assertFalse(izmenjavanje(["Benjamin", "Ana", "Cilka"]))
        self.assertFalse(izmenjavanje(["Ana", "Cilka", "Benjamin", "Eva"]))
        self.assertFalse(izmenjavanje(["Ana", "Benjamin", "Cilka", "Eva"]))

        self.assertFalse(izmenjavanje(["An", "Cilk"]))
        self.assertFalse(izmenjavanje(["An", "Cilk", "Benjamina"]))
        self.assertFalse(izmenjavanje(["Benjamina", "An", "Cilk"]))
        self.assertFalse(izmenjavanje(["An", "Cilk", "Benjamina", "Ev"]))
        self.assertFalse(izmenjavanje(["An", "Benjamina", "Cilk", "Ev"]))

        self.assertFalse(izmenjavanje(["Ana", "Cilka", "Benjamina"]))
        self.assertFalse(izmenjavanje(["An", "Cilk", "Benjamin"]))


class N4Figura(unittest.TestCase):
    def test_spremeni_smer(self):
        self.assertEqual(spremeni_smer("U", "R"), "R")
        self.assertEqual(spremeni_smer("U", "L"), "L")
        self.assertEqual(spremeni_smer("U", "F"), "U")

        self.assertEqual(spremeni_smer("D", "R"), "L")
        self.assertEqual(spremeni_smer("D", "L"), "R")
        self.assertEqual(spremeni_smer("D", "F"), "D")

        self.assertEqual(spremeni_smer("R", "R"), "D")
        self.assertEqual(spremeni_smer("R", "L"), "U")
        self.assertEqual(spremeni_smer("R", "F"), "R")

        self.assertEqual(spremeni_smer("L", "R"), "U")
        self.assertEqual(spremeni_smer("L", "L"), "D")
        self.assertEqual(spremeni_smer("L", "F"), "L")

    def test_44(self):
        plosca = ["RLLL", "RRLL", "FRFF", "FRLF"]

        # Potovanje se konča, ko pride na isto polje -- (0, 2):
        self.assertListEqual(potuj(0, 3, "U", plosca), [(0, 3), (0, 2), (0, 1), (1, 1), (1, 2), (0, 2)])

        # Potovanje se konča, ker pride čez spodnji rob
        self.assertListEqual(potuj(0, 3, "R", plosca), [(0, 3), (1, 3), (1, 4)])

        self.assertListEqual(potuj(3, 1, "U", plosca), [(3, 1), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3)])
        self.assertListEqual(potuj(3, 1, "R", plosca), [(3, 1), (3, 0), (2, 0), (2, 1), (3, 1)])

    def test_33r(self):
        plosca = ["RFR", "FRF", "RFR"]
        self.assertListEqual(potuj(0, 1, "U", plosca),
                             [(0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)])
        self.assertListEqual(potuj(1, 2, "U", plosca), [(1, 2), (1, 1), (2, 1), (3, 1)])

    def test_33l(self):
        plosca = ["LFL", "FLF", "LFL"]
        self.assertListEqual(potuj(2, 1, "U", plosca),
                             [(2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1)])
        self.assertListEqual(potuj(1, 2, "U", plosca), [(1, 2), (1, 1), (0, 1), (-1, 1)])

    def test_22l(self):
        plosca = ["LL", "LL"]
        self.assertListEqual(potuj(1, 0, "U", plosca), [(1, 0), (0, 0), (0, 1), (1, 1), (1, 0)])
        self.assertListEqual(potuj(1, 1, "U", plosca), [(1, 1), (0, 1), (0, 2)])
        self.assertListEqual(potuj(0, 1, "U", plosca), [(0, 1), (-1, 1)])
        self.assertListEqual(potuj(0, 0, "U", plosca), [(0, 0), (-1, 0)])

    def test_22r(self):
        plosca = ["RR", "RR"]
        self.assertListEqual(potuj(1, 0, "U", plosca), [(1, 0), (2, 0)])
        self.assertListEqual(potuj(1, 1, "U", plosca), [(1, 1), (2, 1)])
        self.assertListEqual(potuj(0, 0, "U", plosca), [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
        self.assertListEqual(potuj(0, 1, "U", plosca), [(0, 1), (1, 1), (1, 2)])

    def test_1(self):
        self.assertListEqual(potuj(0, 0, "U", ["F"]), [(0, 0), (0, -1)])
        self.assertListEqual(potuj(0, 0, "D", ["F"]), [(0, 0), (0, 1)])
        self.assertListEqual(potuj(0, 0, "R", ["F"]), [(0, 0), (1, 0)])
        self.assertListEqual(potuj(0, 0, "L", ["F"]), [(0, 0), (-1, 0)])

        self.assertListEqual(potuj(0, 0, "U", ["L"]), [(0, 0), (-1, 0)])
        self.assertListEqual(potuj(0, 0, "D", ["L"]), [(0, 0), (1, 0)])
        self.assertListEqual(potuj(0, 0, "R", ["L"]), [(0, 0), (0, -1)])
        self.assertListEqual(potuj(0, 0, "L", ["L"]), [(0, 0), (0, 1)])

        self.assertListEqual(potuj(0, 0, "U", ["R"]), [(0, 0), (1, 0)])
        self.assertListEqual(potuj(0, 0, "D", ["R"]), [(0, 0), (-1, 0)])
        self.assertListEqual(potuj(0, 0, "R", ["R"]), [(0, 0), (0, 1)])
        self.assertListEqual(potuj(0, 0, "L", ["R"]), [(0, 0), (0, -1)])


class N5Knjizica(unittest.TestCase):
    def test_init(self):
        Knjizica()

    def test_izposodi_izposojeno(self):
        k1 = Knjizica()
        self.assertSetEqual(k1.izposojeno(), set())

        k1.izposodi("Otok zakladov", 10)
        self.assertSetEqual(k1.izposojeno(), {"Otok zakladov"})

        k2 = Knjizica()
        self.assertSetEqual(k2.izposojeno(), set())

        k1.izposodi("Deset odtenkov zelene", 15)
        self.assertSetEqual(k1.izposojeno(), {"Otok zakladov", "Deset odtenkov zelene"})

        k2.izposodi("Kapital", 20)
        self.assertSetEqual(k1.izposojeno(), {"Otok zakladov", "Deset odtenkov zelene"})
        self.assertSetEqual(k2.izposojeno(), {"Kapital"})

    def test_izposodi_vrni(self):
        k1 = Knjizica()
        k1.izposodi("Otok zakladov", 10)
        k1.izposodi("Deset odtenkov zelene", 15)
        k1.izposodi("Kapital", 20)

        k1.vrni("Otok zakladov")
        self.assertSetEqual(k1.izposojeno(), {"Deset odtenkov zelene", "Kapital"})
        k1.vrni("Kapital")
        self.assertSetEqual(k1.izposojeno(), {"Deset odtenkov zelene"})
        k1.vrni("Deset odtenkov zelene")
        self.assertSetEqual(k1.izposojeno(), set())

    def test_zamudnina(self):
        k1 = Knjizica()
        k1.izposodi("Otok zakladov", 10)
        k1.izposodi("Deset odtenkov zelene", 15)
        k1.izposodi("Kapital", 20)

        self.assertEqual(k1.zamudnina(31), 0)
        self.assertEqual(k1.zamudnina(32), 1)
        self.assertEqual(k1.zamudnina(33), 2)
        self.assertEqual(k1.zamudnina(36), 5)
        self.assertEqual(k1.zamudnina(37), 6 + 1)
        self.assertEqual(k1.zamudnina(38), 7 + 2)
        self.assertEqual(k1.zamudnina(41), 10 + 5 + 0)
        self.assertEqual(k1.zamudnina(42), 11 + 6 + 1)
        self.assertEqual(k1.zamudnina(50), 19 + 14 + 9)


if __name__ == "__main__":
    unittest.main()
