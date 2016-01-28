import unittest
from itertools import permutations

permutations([1, 2])


def stevilo_sosedov(s):
    sums = []
    for i, e in enumerate(s):
        i1 = i + 1
        if i1 >= len(s):
            i1 = 0
        sums.append(s[i1] + s[i - 1])
    return sums


"""WTF?"""


def trki(xs):
    d = {}
    for x in xs:
        k = skrij(x)
        if k in d:
            return d[k], x
        d[k] = x


def preveri_zaporedje(zap):
    for e1, e2 in zip(zap, zap[1:]):
        for char in str(e1):
            if str(e2).find(char) != -1:
                break
        else:
            return False
    return True


def postar(s):
    return any(preveri_zaporedje(x) for x in permutations(s))


def zenska(ime):
    ime = ime.split()
    return ime[0][-1] == "a"


def sester_pod(ime, rodbina):
    ma = 0
    for name in rodbina[ime]:
        n = 0
        for name2 in rodbina[ime]:
            if zenska(name2) and name2 != name:
                n += 1
        if n > ma:
            ma = n
    return ma


def najvec_sester(ime, rodovnik):
    n = sester_pod(ime, rodovnik)
    for otrok in rodovnik[ime]:
        no = najvec_sester(otrok, rodovnik)
        if no > n:
            n = no
    return n


class Blagajna:
    def __init__(self):
        self.value = []

    def dodaj(self, bankovec):
        self.value.append(bankovec)

    def vzemi(self, bankovec):
        if bankovec in self.value:
            del self.value[self.value.index(bankovec)]
            return True
        else:
            return False

    def bilanca(self):
        return sum(self.value)


class TestIzpit(unittest.TestCase):
    def test_stevilo_sosedov(self):
        self.assertEqual(stevilo_sosedov([1, 2, 0, 5]), [7, 1, 7, 1])
        self.assertEqual(stevilo_sosedov([1, 0, 0]), [0, 1, 1])
        self.assertEqual(stevilo_sosedov([0, 1, 0]), [1, 0, 1])
        self.assertEqual(stevilo_sosedov([0, 0, 1]), [1, 1, 0])
        self.assertEqual(stevilo_sosedov([0, 9, 0]), [9, 0, 9])
        self.assertEqual(stevilo_sosedov([0, 1, 1]), [2, 1, 1])
        self.assertEqual(stevilo_sosedov([1, 0, 1]), [1, 2, 1])
        self.assertEqual(stevilo_sosedov([1, 1, 0]), [1, 1, 2])
        self.assertEqual(stevilo_sosedov([1, 2, 3]), [5, 4, 3])
        self.assertEqual(stevilo_sosedov([1, 2, 3, 4]), [6, 4, 6, 4])
        self.assertEqual(stevilo_sosedov([1, 0, 0, 0, 0, 0, 0, 0]), [0, 1, 0, 0, 0, 0, 0, 1])
        self.assertEqual(stevilo_sosedov([1, 1, 0, 2, 2, 0, 4, 4]), [5, 1, 3, 2, 2, 6, 4, 5])
        self.assertEqual(stevilo_sosedov([24, 36, 19, 85, 92, 4, 23, 92, 1, 9]),
                         [45, 43, 121, 111, 89, 115, 96, 24, 101, 25])
        self.assertEqual(stevilo_sosedov([61, 72, 59, 20, 57, 100, 95, 25, 93, 98]),
                         [170, 120, 92, 116, 120, 152, 125, 188, 123, 154])
        self.assertEqual(stevilo_sosedov([95, 35, 62, 12, 15, 98, 77, 85, 94, 45]),
                         [80, 157, 47, 77, 110, 92, 183, 171, 130, 189])
        self.assertEqual(stevilo_sosedov([49, 65, 46, 46, 49, 39, 16, 72, 0, 21]),
                         [86, 95, 111, 95, 85, 65, 111, 16, 93, 49])
        self.assertEqual(stevilo_sosedov([48, 48, 31, 24, 16, 10, 26, 9, 3, 14]),
                         [62, 79, 72, 47, 34, 42, 19, 29, 23, 51])
        self.assertEqual(
                stevilo_sosedov([29, 28, 77, 69, 5, 92, 65, 24, 49, 65, 29, 100, 61, 62, 22, 12, 77, 15, 73, 84]),
                [112, 106, 97, 82, 161, 70, 116, 114, 89, 78, 165, 90, 162, 83, 74, 99, 27, 150, 99, 102])
        self.assertEqual(stevilo_sosedov([82, 7, 96, 5, 56, 8, 13, 88, 81, 46, 89, 61, 11, 0, 3, 58, 58, 17, 80, 40]),
                         [47, 178, 12, 152, 13, 69, 96, 94, 134, 170, 107, 100, 61, 14, 58, 61, 75, 138, 57, 162])
        self.assertEqual(stevilo_sosedov([18, 24, 75, 30, 93, 92, 6, 73, 21, 7, 62, 84, 14, 67, 96, 75, 73, 0, 0, 8]),
                         [32, 93, 54, 168, 122, 99, 165, 27, 80, 83, 91, 76, 151, 110, 142, 169, 75, 73, 8, 18])
        self.assertEqual(stevilo_sosedov([71, 39, 68, 57, 85, 9, 56, 2, 82, 1, 29, 96, 77, 65, 12, 73, 65, 73, 90, 35]),
                         [74, 139, 96, 153, 66, 141, 11, 138, 3, 111, 97, 106, 161, 89, 138, 77, 146, 155, 108, 161])
        self.assertEqual(
                stevilo_sosedov([95, 32, 22, 49, 0, 28, 17, 15, 42, 6, 78, 19, 48, 72, 53, 35, 60, 34, 45, 54]),
                [86, 117, 81, 22, 77, 17, 43, 59, 21, 120, 25, 126, 91, 101, 107, 113, 69, 105, 88, 140])

    def test_trki(self):
        global skrij

        def assertCollision(xs):
            res = trki(xs)
            self.assertIsNotNone(res)
            self.assertIn(res[0], xs)
            self.assertIn(res[1], xs)
            self.assertNotEqual(res[0], res[1])
            self.assertEqual(skrij(res[0]), skrij(res[1]))

        # preveri pravilnost
        def skrij1(s):
            return '42'

        skrij = skrij1
        self.assertIsNone(trki([]))
        self.assertIsNone(trki(['a']))
        assertCollision(['a', 'b'])
        assertCollision(['a', 'b', 'c'])
        assertCollision(['', 'a'])

        def skrij2(s):
            return s[0]

        skrij = skrij2
        self.assertIsNone(trki(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
        self.assertIsNone(trki(['ana', 'berta']))
        self.assertIsNone(trki(['ana', 'berta', 'cilka', 'jozica']))
        self.assertIsNone(trki(['ana', 'berta', 'cilka', 'jozica', 'maja']))
        assertCollision(['a', 'ab'])
        assertCollision(['ana', 'anja'])
        assertCollision(['ana', 'berta', 'cilka', 'anja'])
        assertCollision(['ana', 'berta', 'cilka', 'anja', 'bojana'])
        assertCollision(['Ljubljana', 'Maribor', 'Celje', 'Ptuj', 'Prian'])

        def skrij3(s):
            return s[:-1]

        skrij = skrij3
        self.assertIsNone(trki(['aa', 'bb', 'cc']))
        self.assertIsNone(trki(['ana', 'berta']))
        self.assertIsNone(trki(['ana', 'berta', 'cilka', 'jozica']))
        self.assertIsNone(trki(['ana', 'berta', 'cilka', 'jozica', 'maja']))
        self.assertIsNone(trki(['ana', 'berta', 'cilka', 'jozica', 'maja', 'anja']))
        self.assertIsNone(trki(['ana', 'berta', 'cilka', 'jozica', 'maja', 'anja', 'bojana']))
        assertCollision(['ane', 'ani'])
        assertCollision(['ana', 'berta', 'cilka', 'jozica', 'berti', 'maja', 'anja', 'bojana'])
        assertCollision(['ana', 'berta', 'cilka', 'jozica', 'maja', 'anja', 'jozice', 'bojana'])
        assertCollision(['Ljubljana', 'Maribor', 'Celje', 'Ljubljanske', 'Ljubljanski', 'Ptuj', 'Prian'])

        # preveri hitrost izvajanja na velikih seznamih
        xs = [str(i) + '0' for i in range(10 ** 5)]
        self.assertIsNone(trki(xs))
        assertCollision(xs + ['13371'])
        assertCollision(xs + ['42', '24'])

    def test_postar(self):
        self.assertTrue(postar([]))
        self.assertTrue(postar([1]))
        self.assertTrue(postar([12, 23, 34, 45, 56]))
        self.assertTrue(postar([45, 12, 56, 34, 23]))
        self.assertTrue(postar([11121, 22233222, 8889, 34, 44488]))
        self.assertTrue(postar([1234, 4321, 2143, 45, 5678, 8765]))
        self.assertTrue(postar([1234, 123, 1, 4321, 46, 56778, 7, 85, 57]))
        self.assertTrue(postar([134, 423, 324, 564, 5, 234, 234]))
        self.assertFalse(postar([1, 2]))
        self.assertFalse(postar([12, 23, 34, 45, 56, 78]))
        self.assertFalse(postar([11121, 22233222, 8889, 44, 44488]))
        self.assertFalse(postar([1234, 4321, 2143, 45, 8765, 8, 7]))
        self.assertFalse(postar([1234, 123, 1, 4321, 56778, 85, 57]))
        self.assertFalse(postar([134, 324, 564, 5, 6, 234, 234]))

    def test_najvec_sester(self):
        self.assertEqual(najvec_sester('1a', {'1a': []}), 0)
        self.assertEqual(najvec_sester('1a', {'1a': ['2a'], '2a': []}), 0)
        self.assertEqual(najvec_sester('1a', {'1a': ['2a', '3a'], '2a': [], '3a': []}), 1)
        self.assertEqual(najvec_sester('1a', {'1a': ['2a', '1'], '2a': [], '3a': [], '1': []}), 1)
        self.assertEqual(najvec_sester('1a', {'1a': ['2a', '3a', '4a'], '2a': [], '3a': [], '4a': []}), 2)
        self.assertEqual(najvec_sester('1a', {'1a': ['2a', '3a', '4a', '1'], '2a': [], '3a': [], '4a': [],
                                              '1': ['5a', '6a', '7a', '8a', '9a'], '5a': [], '6a': [], '7a': [],
                                              '8a': [], '9a': []}), 4)
        self.assertEqual(najvec_sester('2a', {'1a': ['2a', '3a', '4a', '1'], '2a': ['2'], '3a': [], '4a': [],
                                              '1': ['5a', '6a', '7a', '8a', '9a'], '5a': [], '6a': [], '7a': [],
                                              '8a': [], '9a': [], '2': []}), 0)
        self.assertEqual(najvec_sester('1', {'1a': ['2a', '3a', '4a', '1'], '2a': ['2'], '3a': [], '4a': [],
                                             '1': ['5a', '6a', '7a', '8a', '9a'], '5a': [], '6a': [], '7a': [],
                                             '8a': [], '9a': [], '2': []}), 4)
        self.assertEqual(najvec_sester('1',
                                       {'1': ['2', '3'], '2': ['1a', '2a', '3a'], '3': ['4a', '5a'], '4a': ['6a', '4'],
                                        '1a': [], '2a': [], '3a': [], '5a': [], '6a': [], '4': []}), 2)
        self.assertEqual(najvec_sester('2',
                                       {'1': ['2', '3'], '2': ['1a', '2a', '3a'], '3': ['4a', '5a'], '4a': ['6a', '4'],
                                        '1a': [], '2a': [], '3a': [], '5a': [], '6a': [], '4': []}), 2)
        self.assertEqual(najvec_sester('1a',
                                       {'1': ['2', '3'], '2': ['1a', '2a', '3a'], '3': ['4a', '5a'], '4a': ['6a', '4'],
                                        '1a': [], '2a': [], '3a': [], '5a': [], '6a': [], '4': []}), 0)
        self.assertEqual(najvec_sester('3',
                                       {'1': ['2', '3'], '2': ['1a', '2a', '3a'], '3': ['4a', '5a'], '4a': ['6a', '4'],
                                        '1a': [], '2a': [], '3a': [], '5a': [], '6a': [], '4': []}), 1)
        self.assertEqual(najvec_sester('4a',
                                       {'1': ['2', '3'], '2': ['1a', '2a', '3a'], '3': ['4a', '5a'], '4a': ['6a', '4'],
                                        '1a': [], '2a': [], '3a': [], '5a': [], '6a': [], '4': []}), 1)

        tree = {'Ulrik I.': ['Viljem'], 'Margareta': [], 'Herman I.': ['Herman II.', 'Hans'], 'Elizabeta II.': [],
                'Viljem': ['Ana Poljska'], 'Elizabeta I.': [], 'Ana Poljska': [], 'Herman III.': ['Margareta'],
                'Ana OrtenburĹĄka': [], 'Barbara': [], 'Herman IV.': [], 'Katarina': [], 'Friderik III.': [],
                'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.', 'Elizabeta I.', 'Barbara'],
                'Ulrik II.': ['Herman IV.', 'Jurij', 'Elizabeta II.'], 'Hans': [], 'Ludvik': [],
                'Friderik I.': ['Ulrik I.', 'Katarina', 'Herman I.', 'Ana OrtenburĹĄka'],
                'Friderik II.': ['Friderik III.', 'Ulrik II.'], 'Jurij': []}
        self.assertEqual(najvec_sester('Friderik I.', tree), 2)
        self.assertEqual(najvec_sester('Ulrik I.', tree), 0)
        self.assertEqual(najvec_sester('Viljem', tree), 0)
        self.assertEqual(najvec_sester('Herman I.', tree), 2)
        self.assertEqual(najvec_sester('Herman II.', tree), 2)
        self.assertEqual(najvec_sester('Herman III.', tree), 0)
        self.assertEqual(najvec_sester('Friderik II.', tree), 1)

    def test_blagajna(self):
        # dodaj
        b = Blagajna()
        b.dodaj(1000)
        self.assertEqual(b.bilanca(), 1000)

        # vzemi
        b = Blagajna()
        b.dodaj(1000)
        b.dodaj(1000)
        self.assertFalse(b.vzemi(100))
        self.assertTrue(b.vzemi(1000))
        self.assertTrue(b.vzemi(1000))
        self.assertFalse(b.vzemi(1000))
        self.assertEqual(b.bilanca(), 0)

        # dve blagajni
        b1 = Blagajna()
        b2 = Blagajna()
        self.assertEqual(b1.bilanca(), 0)
        self.assertIsNone(b1.dodaj(1))
        self.assertEqual(b1.bilanca(), 1)
        self.assertIsNone(b1.dodaj(1))
        self.assertEqual(b1.bilanca(), 2)
        self.assertIsNone(b1.dodaj(2))
        self.assertEqual(b1.bilanca(), 4)
        self.assertIsNone(b1.dodaj(3))
        self.assertEqual(b1.bilanca(), 7)

        self.assertEqual(b2.bilanca(), 0)
        self.assertIsNone(b2.dodaj(3))
        self.assertEqual(b2.bilanca(), 3)
        self.assertIsNone(b2.dodaj(3))
        self.assertEqual(b2.bilanca(), 6)
        self.assertIsNone(b2.dodaj(100))
        self.assertEqual(b2.bilanca(), 106)

        self.assertFalse(b1.vzemi(100))
        self.assertTrue(b1.vzemi(1))
        self.assertEqual(b1.bilanca(), 6)
        self.assertTrue(b1.vzemi(1))
        self.assertEqual(b1.bilanca(), 5)
        self.assertFalse(b1.vzemi(1))
        self.assertEqual(b1.bilanca(), 5)
        self.assertTrue(b1.vzemi(3))
        self.assertEqual(b1.bilanca(), 2)
        self.assertTrue(b1.vzemi(2))
        self.assertEqual(b1.bilanca(), 0)
        self.assertTrue(b2.vzemi(100))
        self.assertEqual(b2.bilanca(), 6)
        self.assertFalse(b2.vzemi(100))


if __name__ == "__main__":
    unittest.main(verbosity = 2)
