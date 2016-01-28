import collections
import unittest


def soda_liha(s):
    soda = []
    liha = []
    for x in s:
        if x % 2 == 0:
            soda.append(x)
        else:
            liha.append(x)
    s.clear()
    for so, li in zip(soda, liha):
        s += (so, li)


def decimalno(s):
    if len(s) < 2:
        return int(s)
    return decimalno(s[:-1]) * 2 + int(s[-1])


def ograje(s):
    return False



def opravil(name, lession, lessions):
    lessions[name].add(lession)


def najbolj_ucen(lessions):
    most = None
    for name, less in lessions.items():
        if most is None or len(less) > len(lessions[most]):
            most = name
    return most


def vsi_tecaji(lessions):
    return {x for lession in lessions.values() for x in lession}


def neopravljeni(name, lessions):
    return vsi_tecaji(lessions) - lessions[name]


class Naselje:
    def __init__(self, s):
        self.houses = {x: None for x in s}

    def vseli(self, house, name):
        if self.houses[house]:
            return False
        self.houses[house] = name
        return True

    def stanovalec(self, house):
        return self.houses[house]

    def izseli(self, house):
        self.houses[house] = None

    def prostih(self):
        i = 0
        for e in self.houses.values():
            if e is None:
                i += 1
        return i


class TestSodaLiha(unittest.TestCase):
    def test(self):
        s = [1, 2, 3, 4]
        self.assertIsNone(soda_liha(s), "Funkcija ne sme vračati rezultata")
        self.assertListEqual(s, [2, 1, 4, 3])

        s = [4, 3, 2, 1]
        self.assertIsNone(soda_liha(s))
        self.assertListEqual(s, [4, 3, 2, 1])

        s = [1, 3, 5]
        self.assertIsNone(soda_liha(s))
        self.assertListEqual(s, [])

        s = [5, 3, 1]
        self.assertIsNone(soda_liha(s))
        self.assertListEqual(s, [])

        s = [2, 4, 6]
        self.assertIsNone(soda_liha(s))
        self.assertListEqual(s, [])

        s = [6, 4, 2]
        self.assertIsNone(soda_liha(s))
        self.assertListEqual(s, [])

        s = [1]
        self.assertIsNone(soda_liha(s))
        self.assertListEqual(s, [])

        s = [2]
        self.assertIsNone(soda_liha(s))
        self.assertListEqual(s, [])

        s = [21, 34]
        self.assertIsNone(soda_liha(s))
        self.assertListEqual(s, [34, 21])

        s = [34, 21]
        self.assertIsNone(soda_liha(s))
        self.assertListEqual(s, [34, 21])

        s = [6, 4, 7, 9, 0, 7, 5, 34, 2, 4, 5]
        self.assertIsNone(soda_liha(s))
        self.assertListEqual(s, [6, 7, 4, 9, 0, 7, 34, 5, 2, 5])


class TestDecimalno(unittest.TestCase):
    def test(self):
        self.assertEqual(decimalno("0"), 0)
        self.assertEqual(decimalno("1"), 1)
        self.assertEqual(decimalno("10"), 2)
        self.assertEqual(decimalno("11"), 3)
        self.assertEqual(decimalno("101010"), 42)
        self.assertEqual(decimalno("0000"), 0)
        self.assertEqual(decimalno("0010"), 2)
        self.assertEqual(decimalno("1111"), 15)


class TestDopisovanje(unittest.TestCase):
    def test_opravil(self):
        tecaji = collections.defaultdict(set)
        opravil("Ana", "B", tecaji)
        self.assertEqual(tecaji, {"Ana": {"B"}})
        opravil("Ana", "B", tecaji)
        self.assertEqual(tecaji, {"Ana": {"B"}})

        tecaji2 = collections.defaultdict(set)
        opravil("Ana", "X", tecaji2)

        opravil("Ana", "C", tecaji)
        self.assertEqual(tecaji, {"Ana": {"B", "C"}})
        opravil("Berta", "C", tecaji)
        self.assertEqual(tecaji, {"Ana": {"B", "C"}, "Berta": {"C"}})
        opravil("Ana", "D", tecaji)
        self.assertEqual(tecaji, {"Ana": {"B", "C", "D"}, "Berta": {"C"}})

    def test_najbolj_ucen(self):
        self.assertEqual(najbolj_ucen({"Ana": {"B", "C", "D"}, "Berta": {"C"}}), "Ana")
        self.assertEqual(najbolj_ucen({"Berta": {"C"}}), "Berta")
        self.assertEqual(
                najbolj_ucen({"Ana": {"B", "C", "D"}, "Berta": {"C"}, "Cilka": {}, "Ema": {"C", "F", "G", "H"}}), "Ema")

    def test_vsi_tecaji(self):
        self.assertSetEqual(vsi_tecaji({"Ana": {"B", "C", "D"}, "Berta": {"C"}}), {"B", "C", "D"})
        self.assertSetEqual(vsi_tecaji({"Ana": {"B", "D"}, "Berta": {"C"}}), {"B", "C", "D"})
        self.assertSetEqual(vsi_tecaji({"Ana": {"B"}}), {"B"})
        self.assertSetEqual(vsi_tecaji({"Ana": set()}), set())
        self.assertSetEqual(vsi_tecaji({}), set())

    def test_neopravljeno(self):
        tecaji = {"Ana": {"B", "C", "D"}, "Berta": {"C"}, "Cilka": set(), "Ema": {"B", "D", "C", "F", "G"}}
        self.assertSetEqual(neopravljeni("Ana", tecaji), {"F", "G"})
        self.assertSetEqual(neopravljeni("Berta", tecaji), {"B", "D", "F", "G"})
        self.assertSetEqual(neopravljeni("Cilka", tecaji), {"B", "C", "D", "F", "G"})
        self.assertSetEqual(neopravljeni("Ema", tecaji), set())


class TestOgraje(unittest.TestCase):
    def test_ograje(self):
        self.assertEqual(ograje(["AAABC", "ABCDC", "ACCDA"]), 30)
        self.assertEqual(ograje(["AAABCA"]), 17)
        self.assertEqual(ograje(["A", "A", "A", "B", "C", "A"]), 17)
        self.assertEqual(ograje(["A"]), 4)
        self.assertEqual(ograje(["AAAAA"] * 5), 20)


class TestNaselje(unittest.TestCase):
    def test_konstruktor(self):
        naselje = Naselje(["Triglav", "Bled", "Hosta", "Znojile"])

    def test_vseli(self):
        naselje = Naselje(["Triglav", "Bled", "Hosta", "Znojile"])
        naselje2 = Naselje(["Bled", "Kranj"])
        self.assertTrue(naselje.vseli("Bled", "Ana"))
        self.assertTrue(naselje.vseli("Hosta", "Berta"))
        self.assertFalse(naselje.vseli("Bled", "Cilka"))
        self.assertFalse(naselje.vseli("Bled", "Ana"))
        self.assertTrue(naselje.vseli("Triglav", "Ana"))
        self.assertTrue(naselje2.vseli("Bled", "Berta"))

    def test_stanovalec(self):
        naselje = Naselje(["Triglav", "Bled", "Hosta", "Znojile"])
        naselje2 = Naselje(["Bled", "Kranj"])
        self.assertIsNone(naselje.stanovalec("Bled"))
        self.assertIsNone(naselje.stanovalec("Hosta"))
        self.assertTrue(naselje.vseli("Bled", "Ana"))
        self.assertEqual(naselje.stanovalec("Bled"), "Ana")
        self.assertIsNone(naselje.stanovalec("Hosta"))
        self.assertTrue(naselje.vseli("Hosta", "Berta"))
        self.assertEqual(naselje.stanovalec("Bled"), "Ana")
        self.assertFalse(naselje.vseli("Bled", "Cilka"))
        self.assertTrue(naselje2.vseli("Bled", "Cilka"))
        self.assertEqual(naselje.stanovalec("Bled"), "Ana")
        self.assertEqual(naselje2.stanovalec("Bled"), "Cilka")
        self.assertTrue(naselje.vseli("Triglav", "Cilka"))
        self.assertFalse(naselje.vseli("Bled", "Ana"))
        self.assertFalse(naselje.vseli("Triglav", "Ana"))
        self.assertTrue(naselje2.vseli("Kranj", "Berta"))
        self.assertEqual(naselje.stanovalec("Triglav"), "Cilka")
        self.assertEqual(naselje.stanovalec("Bled"), "Ana")
        self.assertEqual(naselje2.stanovalec("Kranj"), "Berta")

    def test_izseli(self):
        naselje = Naselje(["Triglav", "Bled", "Hosta", "Znojile"])
        self.assertTrue(naselje.vseli("Bled", "Ana"))
        self.assertFalse(naselje.vseli("Bled", "Berta"))
        self.assertIsNone(naselje.izseli("Bled"), "Izseli naj ne vrača ničesar")
        self.assertIsNone(naselje.stanovalec("Bled"))
        self.assertTrue(naselje.vseli("Bled", "Berta"))

    def test_prostih(self):
        naselje = Naselje(["Triglav", "Bled", "Hosta", "Znojile"])
        self.assertEqual(naselje.prostih(), 4)
        naselje2 = Naselje(["Bled", "Kranj"])
        self.assertEqual(naselje.prostih(), 4)
        self.assertTrue(naselje.vseli("Bled", "Ana"))
        self.assertEqual(naselje.prostih(), 3)
        self.assertTrue(naselje.vseli("Hosta", "Berta"))
        self.assertEqual(naselje.prostih(), 2)
        self.assertFalse(naselje.vseli("Bled", "Cilka"))
        self.assertEqual(naselje.prostih(), 2)
        self.assertEqual(naselje2.prostih(), 2)
        self.assertTrue(naselje2.vseli("Bled", "Cilka"))
        self.assertEqual(naselje.prostih(), 2)
        self.assertEqual(naselje2.prostih(), 1)
        naselje.izseli("Bled")
        self.assertEqual(naselje.prostih(), 3)
        naselje.izseli("Hosta")
        self.assertEqual(naselje.prostih(), 4)


if __name__ == "__main__":
    unittest.main()
