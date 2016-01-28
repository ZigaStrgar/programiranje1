import collections
import unittest


class Blok:
    def __init__(self, floors):
        self.floors = floors
        self.tenants = {}

    def vseli(self, floor, name):
        if not self.tenants.get(floor, None):
            self.tenants[floor] = name
            return True
        return False

    def stanovalec(self, floor):
        return self.tenants.get(floor, None)

    def izseli(self, floor):
        del self.tenants[floor]

    def kamorkoli(self, name):
        i = self.floors - 1
        t = []
        while i >= 0:
            t.append(self.vseli(i, name))
            if any(t):
                break
            i -= 1
        return any(t)


def dopis(who, to, relations):
    relations[who].add(to)


def najzgovornejsi(relations):
    maxx = None
    for who, to in relations.items():
        if maxx is None or len(to) > len(relations[maxx]):
            maxx = who
    return maxx


def vse_osebe(relations):
    persons = set()
    for who, to in relations.items():
        persons.add(who)
        persons.update(to)
    return persons


def neznanci(name, relations):
    persons = vse_osebe(relations)
    persons.remove(name)
    persons.difference_update(relations[name])
    return persons


def binarno(n):
    if n <= 1:
        return str(n)
    return binarno(n // 2) + str(n % 2)


def se_lihih(s):
    for x in s:
        if x % 2 == 1:
            return True
    return False


def najprej_lihi(s):
    i = 0
    position = 0
    while i < len(s):
        element = s[i]
        if se_lihih(s[i:]):
            if element % 2 == 1:
                s.pop(i)
                s.insert(position, element)
                position += 1
        i += 1


def sirina(s):
    return len(s[0])


def visina(s):
    return len(s)


if set("ABC") > set("ABC"):
    print("yes")


def check_lang(s, t):
    if len(s & t) != 0:
        return True


def sogovorniki(s):
    mnozica = set()
    for i, e in enumerate(s):
        for num, langs in enumerate(e):
            if 0 < i - 1 < visina(s):
                if check_lang(set(langs), set(s[i - 1][num])):
                    mnozica.add(((i, num), (i - 1, num)))
            if 0 < i + 1 < visina(s):
                if check_lang(set(langs), set(s[i + 1][num])):
                    mnozica.add(((i, num), (i + 1, num)))
            if 0 < num - 1 < sirina(s):
                if check_lang(set(langs), set(s[i][num - 1])):
                    mnozica.add(((i, num), (i, num - 1)))
            if 0 < num + 1 < sirina(s):
                if check_lang(set(langs), set(s[i][num + 1])):
                    mnozica.add(((i, num), (i, num + 1)))
    print(mnozica)
    return len(mnozica)


class TestNajprejLihi(unittest.TestCase):
    def test(self):
        s = [1, 2, 3, 4]
        self.assertIsNone(najprej_lihi(s), "Funkcija ne sme vračati rezultata")
        self.assertListEqual(s, [1, 3, 2, 4])

        s = [4, 3, 2, 1]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [3, 1, 4, 2])

        s = [1, 3, 5]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [1, 3, 5])

        s = [5, 3, 1]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [5, 3, 1])

        s = [2, 4, 6]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [2, 4, 6])

        s = [6, 4, 2]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [6, 4, 2])

        s = [1]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [1])

        s = [2]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [2])

        s = [21, 34]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [21, 34])

        s = [34, 21]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [21, 34])

        s = [34, 34, 21, 34, 21]
        self.assertIsNone(najprej_lihi(s))
        self.assertListEqual(s, [21, 21, 34, 34, 34])


class TestBinarno(unittest.TestCase):
    def test(self):
        self.assertEqual(binarno(3), "11")
        self.assertEqual(binarno(2), "10")
        self.assertEqual(binarno(1), "1")
        self.assertEqual(binarno(0), "0")
        self.assertEqual(binarno(42), "101010")


class TestDopisovanje(unittest.TestCase):
    def test_dopis(self):
        relacije = collections.defaultdict(set)
        dopis("Ana", "Berta", relacije)
        self.assertEqual(relacije, {"Ana": {"Berta"}})
        dopis("Ana", "Berta", relacije)
        self.assertEqual(relacije, {"Ana": {"Berta"}})

        relacije2 = collections.defaultdict(set)
        dopis("Ana", "Cene", relacije2)

        dopis("Ana", "Cilka", relacije)
        self.assertEqual(relacije, {"Ana": {"Berta", "Cilka"}})
        dopis("Berta", "Cilka", relacije)
        self.assertEqual(relacije, {"Ana": {"Berta", "Cilka"}, "Berta": {"Cilka"}})
        dopis("Ana", "Dani", relacije)
        self.assertEqual(relacije, {"Ana": {"Berta", "Cilka", "Dani"}, "Berta": {"Cilka"}})

    def test_najzgovornejsi(self):
        self.assertEqual(najzgovornejsi({"Ana": {"Berta", "Cilka", "Dani"}, "Berta": {"Cilka"}}), "Ana")
        self.assertEqual(najzgovornejsi({"Berta": {"Cilka"}}), "Berta")
        self.assertEqual(najzgovornejsi({"Ana": {"Berta", "Cilka", "Dani"}, "Berta": {"Cilka"}, "Cilka": {},
                                         "Ema": {"Cilka", "Fanci", "Greta", "Helga"}}), "Ema")

    def test_vse_osebe(self):
        self.assertSetEqual(vse_osebe({"Ana": {"Berta", "Cilka", "Dani"}, "Berta": {"Cilka"}}),
                            {"Ana", "Berta", "Cilka", "Dani"})
        self.assertSetEqual(vse_osebe({"Ana": {"Berta", "Dani"}, "Berta": {"Cilka"}}),
                            {"Ana", "Berta", "Cilka", "Dani"})
        self.assertSetEqual(vse_osebe({"Ana": {"Berta"}}), {"Ana", "Berta"})
        self.assertSetEqual(vse_osebe({"Ana": set()}), {"Ana"})
        self.assertSetEqual(vse_osebe({}), set())

    def test_neznanci(self):
        relacije = {"Ana": {"Berta", "Cilka", "Dani"}, "Berta": {"Cilka"}, "Cilka": set(),
                    "Ema": {"Cilka", "Fanci", "Greta"}}
        self.assertFalse("Ana" in neznanci("Ana", relacije), "Nobena oseba ni neznana sebi")
        self.assertSetEqual(neznanci("Ana", relacije), {"Ema", "Fanci", "Greta"})
        self.assertSetEqual(neznanci("Berta", relacije), {"Ana", "Dani", "Ema", "Fanci", "Greta"})
        self.assertSetEqual(neznanci("Cilka", relacije), {"Ana", "Berta", "Dani", "Ema", "Fanci", "Greta"})
        self.assertSetEqual(neznanci("Ema", relacije), {"Ana", "Berta", "Dani"})


class TestZapor(unittest.TestCase):
    def test_sogovorniki(self):
        self.assertEqual(sogovorniki(
                [["ABC", "B", "BC", "E", "A"], ["C", "D", "AE", "DB", "DC"], ["BC", "AE", "E", "BC", "AED"]]), 9)
        self.assertEqual(sogovorniki([["ABC", "B", "BC", "E", "A"]]), 2)
        self.assertEqual(sogovorniki([["ABC", "B", "BCA", "A"]]), 3)
        self.assertEqual(sogovorniki([["ABC"], ["C"], ["BC"]]), 2)
        self.assertEqual(sogovorniki([["ABC"]]), 0)
        self.assertEqual(sogovorniki([["ABC", "DE", "BC"]]), 0)
        self.assertEqual(sogovorniki([["ABC"], ["DE"], ["BC"], ["A"]]), 0)


class TestBlok(unittest.TestCase):
    def test_konstruktor(self):
        blok = Blok(3)

    def test_vseli(self):
        blok = Blok(3)
        blok2 = Blok(5)
        self.assertTrue(blok.vseli(1, "Ana"))
        self.assertTrue(blok.vseli(2, "Berta"))
        self.assertFalse(blok.vseli(1, "Cilka"))
        self.assertFalse(blok.vseli(1, "Ana"))
        self.assertTrue(blok.vseli(0, "Ana"))
        self.assertTrue(blok2.vseli(1, "Berta"))

    def test_stanovalec(self):
        blok = Blok(20)
        blok2 = Blok(5)
        for i in range(20):
            self.assertIsNone(blok.stanovalec(i))
        self.assertTrue(blok.vseli(18, "Ana"))
        self.assertEqual(blok.stanovalec(18), "Ana")
        self.assertTrue(blok.vseli(2, "Berta"))
        self.assertEqual(blok.stanovalec(18), "Ana")
        self.assertEqual(blok.stanovalec(2), "Berta")
        self.assertFalse(blok.vseli(2, "Cilka"))
        self.assertEqual(blok.stanovalec(2), "Berta")
        self.assertIsNone(blok.stanovalec(1), "Berta")

        self.assertTrue(blok2.vseli(2, "Cilka"))
        self.assertEqual(blok.stanovalec(2), "Berta")
        self.assertEqual(blok2.stanovalec(2), "Cilka")

    def test_izseli(self):
        blok = Blok(20)
        self.assertTrue(blok.vseli(18, "Ana"))
        self.assertEqual(blok.stanovalec(18), "Ana")
        self.assertTrue(blok.vseli(2, "Berta"))
        self.assertEqual(blok.stanovalec(2), "Berta")
        self.assertFalse(blok.vseli(2, "Berta"))
        self.assertFalse(blok.vseli(2, "Cilka"))
        self.assertEqual(blok.stanovalec(2), "Berta")
        self.assertIsNone(blok.izseli(2), "Metoda 'izseli' naj ne vrača rezultata")
        self.assertIsNone(blok.stanovalec(2))
        self.assertTrue(blok.vseli(2, "Cilka"))
        self.assertEqual(blok.stanovalec(2), "Cilka")

    def test_kamorkoli(self):
        blok = Blok(5)
        blok.vseli(2, "Ana")
        self.assertTrue(blok.kamorkoli("Berta"))
        self.assertIsNone(blok.stanovalec(0))
        self.assertIsNone(blok.stanovalec(1))
        self.assertEqual(blok.stanovalec(2), "Ana")
        self.assertIsNone(blok.stanovalec(3))
        self.assertEqual(blok.stanovalec(4), "Berta")
        self.assertTrue(blok.kamorkoli("Cilka"))
        self.assertEqual(blok.stanovalec(3), "Cilka")
        self.assertFalse(blok.vseli(3, "Dani"))
        self.assertEqual(blok.stanovalec(3), "Cilka")
        self.assertTrue(blok.kamorkoli("Dani"))
        self.assertTrue(blok.kamorkoli("Ema"))
        self.assertEqual(blok.stanovalec(0), "Ema")
        self.assertEqual(blok.stanovalec(1), "Dani")
        self.assertEqual(blok.stanovalec(2), "Ana")
        self.assertEqual(blok.stanovalec(3), "Cilka")
        self.assertEqual(blok.stanovalec(4), "Berta")
        self.assertFalse(blok.kamorkoli("Fanci"))


if __name__ == "__main__":
    unittest.main()
