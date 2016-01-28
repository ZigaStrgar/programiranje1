import collections
import math
import unittest


def loci(s):
    return [name for name, st in s if st % 2 == 0], [name for name, st in s if st % 2 == 1]


def skrij(s):
    t = collections.Counter(list(s))
    s = sorted(list(t))
    string = ""
    for char in s:
        string += char + str(t[char])
    return string


def srecanje(vrt):
    return 0


def otroci(oseba, rodbina):
    return rodbina[oseba]


def st_vnukov(oseba, rodbina):
    sk = 0
    for otrok in otroci(oseba, rodbina):
        sk += len(otroci(otrok, rodbina))
    return sk


def najvec_vnukov(ime, rodbina):
    n = st_vnukov(ime, rodbina)
    for otrok in otroci(ime, rodbina):
        no = najvec_vnukov(otrok, rodbina)
        if n < no:
            n = no
    return n


class Liki:
    def __init__(self):
        self.liki = collections.defaultdict(list)

    def krog(self, x, y, r):
        self.liki["krog"].append([x, y, r])

    def pravokotnik(self, x1, y1, x2, y2):
        self.liki["pravokotnik"].append([x1, y1, x2, y2])

    def ploscina(self):
        p = 0
        for tip, s in self.liki.items():
            for e in s:
                if tip == "krog":
                    p += math.pi * e[-1] ** 2
                else:
                    p += abs(e[0] - e[2]) * abs(e[1] - e[3])
        return p

    def krogi(self, max_r):
        krogci = []
        for x, y, r in self.liki["krog"]:
            if r < max_r:
                krogci.append((x, y))
        return krogci



class TestIzpit(unittest.TestCase):
    def test_loci(self):
        self.assertEqual(loci([]), ([], []))
        self.assertEqual(loci([('Ana', 5)]), ([], ['Ana']))
        self.assertEqual(loci([('Ana', 6)]), (['Ana'], []))
        self.assertEqual(loci([('Ana', 5), ('Berta', 20)]), (['Berta'], ['Ana']))
        self.assertEqual(loci([('Mojca', 1), ('Ana', 5), ('Berta', 20)]), (['Berta'], ['Mojca', 'Ana']))
        self.assertEqual(loci([('Mojca', 1), ('Ana', 5), ('Neza', 42), ('Berta', 20)]),
                         (['Neza', 'Berta'], ['Mojca', 'Ana']))
        self.assertEqual(loci([('Mojca', 1), ('Ana', 5), ('Neza', 42), ('Berta', 20), ('Polona', 100)]),
                         (['Neza', 'Berta', 'Polona'], ['Mojca', 'Ana']))
        self.assertEqual(loci([('Mojca', 1), ('Luka', 4), ('Ana', 5), ('Neza', 42), ('Berta', 20), ('Polona', 100)]),
                         (['Luka', 'Neza', 'Berta', 'Polona'], ['Mojca', 'Ana']))
        self.assertEqual(loci(
                [('Mojca', 1), ('Luka', 4), ('Ana', 5), ('Blaz', 10), ('Neza', 42), ('Berta', 20), ('Polona', 100)]),
                (['Luka', 'Blaz', 'Neza', 'Berta', 'Polona'], ['Mojca', 'Ana'],))
        self.assertEqual(loci(
                [('Mojca', 1), ('Tjasa', 1), ('Luka', 4), ('Ana', 5), ('Blaz', 10), ('Neza', 42), ('Berta', 20),
                 ('Polona', 100)]), (['Luka', 'Blaz', 'Neza', 'Berta', 'Polona'], ['Mojca', 'Tjasa', 'Ana']))
        self.assertEqual(loci(
                [('Mojca', 2), ('Tjasa', 9), ('Luka', 7), ('Ana', 2), ('Blaz', 12), ('Neza', 43), ('Berta', 80),
                 ('Polona', 101)]), (['Mojca', 'Ana', 'Blaz', 'Berta'], ['Tjasa', 'Luka', 'Neza', 'Polona']))

    def test_skrij(self):
        self.assertEqual(skrij('hana'), 'a2h1n1')
        self.assertEqual(skrij(''), '')
        self.assertEqual(skrij('a'), 'a1')
        self.assertEqual(skrij('z'), 'z1')
        self.assertEqual(skrij('aa'), 'a2')
        self.assertEqual(skrij('zz'), 'z2')
        self.assertEqual(skrij('az'), 'a1z1')
        self.assertEqual(skrij('za'), 'a1z1')
        self.assertEqual(skrij('aazz'), 'a2z2')
        self.assertEqual(skrij('azaz'), 'a2z2')
        self.assertEqual(skrij('zzaa'), 'a2z2')
        self.assertEqual(skrij('zaaz'), 'a2z2')
        self.assertEqual(skrij('abeceda'), 'a2b1c1d1e2')
        self.assertEqual(skrij('dolgabeseda'), 'a2b1d2e2g1l1o1s1')
        self.assertEqual(skrij('sedaljsabeseda'), 'a3b1d2e3j1l1s3')
        self.assertEqual(skrij('superdolgabeseda'), 'a2b1d2e3g1l1o1p1r1s2u1')
        self.assertEqual(skrij('najdaljsamoznabeseda'), 'a5b1d2e2j2l1m1n2o1s2z1')
        self.assertEqual(skrij('fjwoievlreoijscnsalskrywoijdfsaclkjsdfoiqyreqpodsakljjfsmmmsnvxzcaldsflsdfoqmnkk'),
                         'a4c3d5e3f6i4j6k5l6m4n3o6p1q3r3s10v2w2x1y2z1')

    def test_srecanje(self):
        self.assertEqual(srecanje([0]), 0)
        self.assertEqual(srecanje([1]), 0)
        self.assertEqual(srecanje([0, 0]), 0.5)
        self.assertEqual(srecanje([1, 0]), 0)
        self.assertEqual(srecanje([0, 1]), 1)
        self.assertEqual(srecanje([5, 5]), 0.5)
        self.assertEqual(srecanje([6, 5]), 0)
        self.assertEqual(srecanje([10, 11]), 1)
        self.assertEqual(srecanje([0, 0, 0]), 1)
        self.assertEqual(srecanje([1, 0, 0]), 0.5)
        self.assertEqual(srecanje([0, 1, 0]), 1)
        self.assertEqual(srecanje([0, 2, 0]), 1)
        self.assertEqual(srecanje([0, 3, 0]), 1)
        self.assertEqual(srecanje([0, 0, 1]), 1.5)
        self.assertEqual(srecanje([1, 2, 3]), 1)
        self.assertEqual(srecanje([8, 1, 6]), 0.5)
        self.assertEqual(srecanje([8, 1, 7]), 1)
        self.assertEqual(srecanje([0, 0, 0, 0]), 1.5)
        self.assertEqual(srecanje([10, 0, 0, 0]), 0)
        self.assertEqual(srecanje([10, 0, 10, 0]), 1.5)
        self.assertEqual(srecanje([10, 0, 9, 0]), 1)
        self.assertEqual(srecanje([40, 15, 18, 19]), 1)
        self.assertEqual(srecanje([1, 4, 1, 2, 8, 3]), 4)
        self.assertEqual(srecanje([1, 4, 1, 2, 8, 3, 0, 0, 0, 15]), 5)
        self.assertEqual(srecanje([1, 4, 1, 2, 8, 3, 0, 0, 6, 15]), 5.5)
        self.assertEqual(srecanje([1, 4, 1, 2, 8, 3, 0, 1, 6, 15]), 6)
        self.assertEqual(srecanje([6, 2, 8, 10, 4, 1, 0, 0, 8, 6, 11, 1, 1, 1, 1]), 6)
        self.assertEqual(srecanje([6, 2, 8, 10, 4, 1, 0, 0, 8, 6, 11, 1, 0, 1, 0]), 5)
        self.assertEqual(srecanje([6, 3, 8, 9, 12, 4, 1, 0, 0, 8, 6, 11, 1, 0, 1, 0]), 4.5)
        self.assertEqual(srecanje([0, 6, 3, 8, 9, 12, 4, 1, 0, 0, 8, 6, 11, 1, 0, 1, 0]), 5)
        self.assertEqual(srecanje([0, 6, 3, 8, 9, 12, 4, 1, 0, 0, 8, 6, 11, 1, 0, 1, 0, 2]), 6)
        self.assertEqual(srecanje([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 8)
        self.assertEqual(srecanje([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 9)
        self.assertEqual(srecanje([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 10)
        self.assertEqual(srecanje([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 10)
        self.assertEqual(srecanje([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), 11)
        self.assertEqual(srecanje([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), 12)
        self.assertEqual(srecanje([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), 13)
        self.assertEqual(srecanje([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 13)

    def test_najvec_vnukov(self):
        self.assertEqual(najvec_vnukov('a', {'a': []}), 0)
        self.assertEqual(najvec_vnukov('a', {'a': ['b', 'c'], 'b': [], 'c': []}), 0)
        self.assertEqual(najvec_vnukov('a', {'a': ['b', 'c'], 'b': ['d'], 'c': [], 'd': []}), 1)
        self.assertEqual(najvec_vnukov('b', {'a': ['b', 'c'], 'b': ['d'], 'c': [], 'd': []}), 0)
        self.assertEqual(najvec_vnukov('c', {'a': ['b', 'c'], 'b': ['d'], 'c': [], 'd': []}), 0)
        self.assertEqual(najvec_vnukov('a', {'a': ['b', 'c'], 'b': ['d', 'e'], 'c': [], 'd': [], 'e': []}), 2)
        self.assertEqual(
            najvec_vnukov('a', {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': [], 'd': ['g'], 'e': [], 'f': [], 'g': []}),
            3)
        self.assertEqual(najvec_vnukov('a',
                                       {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': [], 'd': ['g', 'h'], 'e': ['i'],
                                        'f': [], 'g': [], 'h': [], 'i': []}), 3)
        self.assertEqual(najvec_vnukov('a', {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': [], 'd': ['g', 'h'],
                                             'e': ['i', 'j'], 'f': [], 'g': [], 'h': [], 'i': [], 'j': []}), 4)
        self.assertEqual(najvec_vnukov('a', {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': [], 'd': ['g', 'h'],
                                             'e': ['i', 'j'], 'f': ['k'], 'g': [], 'h': [], 'i': [], 'j': [], 'k': []}),
                         5)
        self.assertEqual(najvec_vnukov('a', {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': [], 'd': ['g', 'h'],
                                             'e': ['i', 'j'], 'f': ['k'], 'g': [], 'h': [], 'i': [], 'j': [], 'k': []}),
                         5)
        self.assertEqual(najvec_vnukov('a', {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': ['l'], 'd': ['g', 'h'],
                                             'e': ['i', 'j'], 'f': ['k'], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [],
                                             'l': ['m'], 'm': []}), 5)
        self.assertEqual(najvec_vnukov('b', {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': ['l'], 'd': ['g', 'h'],
                                             'e': ['i', 'j'], 'f': ['k'], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [],
                                             'l': ['m'], 'm': []}), 5)
        self.assertEqual(najvec_vnukov('c', {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': ['l'], 'd': ['g', 'h'],
                                             'e': ['i', 'j'], 'f': ['k'], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [],
                                             'l': ['m'], 'm': []}), 1)
        self.assertEqual(najvec_vnukov('d', {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': ['l'], 'd': ['g', 'h'],
                                             'e': ['i', 'j'], 'f': ['k'], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [],
                                             'l': ['m'], 'm': []}), 0)
        self.assertEqual(najvec_vnukov('a', {'a': ['b'], 'b': ['c'], 'c': ['d'], 'd': ['e'], 'e': ['f'], 'f': ['g'],
                                             'g': ['h'], 'h': ['i', 'j', 'k', 'l', 'm'], 'i': [], 'j': [], 'k': [],
                                             'l': ['m'], 'm': []}), 5)
        self.assertEqual(najvec_vnukov('d', {'a': ['b', 'i', 'j', 'k', 'l', 'm'], 'b': ['c'], 'c': ['d'], 'd': ['e'],
                                             'e': ['f'], 'f': ['g'], 'g': ['h'], 'h': [], 'i': [], 'j': [], 'k': [],
                                             'l': ['m'], 'm': []}), 1)
        self.assertEqual(najvec_vnukov('a', {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': ['g', 'h'], 'g': ['i', 'j'],
                                             'h': [], 'd': [], 'e': [], 'f': [], 'i': [], 'j': []}), 5)
        self.assertEqual(najvec_vnukov('c', {'a': ['b', 'c'], 'b': ['d', 'e', 'f'], 'c': ['g', 'h'], 'g': ['i', 'j'],
                                             'h': [], 'd': [], 'e': [], 'f': [], 'i': [], 'j': []}), 2)

        tree = {'Ulrik I.': ['Viljem'], 'Margareta': [], 'Herman I.': ['Herman II.', 'Hans'], 'Elizabeta II.': [],
                'Viljem': ['Ana Poljska'], 'Elizabeta I.': [], 'Ana Poljska': [], 'Herman III.': ['Margareta'],
                'Ana OrtenburĹĄka': [], 'Barbara': [], 'Herman IV.': [], 'Katarina': [], 'Friderik III.': [],
                'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.', 'Elizabeta I.', 'Barbara'],
                'Ulrik II.': ['Herman IV.', 'Jurij', 'Elizabeta II.'], 'Hans': [], 'Ludvik': [],
                'Friderik I.': ['Ulrik I.', 'Katarina', 'Herman I.', 'Ana OrtenburĹĄka'],
                'Friderik II.': ['Friderik III.', 'Ulrik II.'], 'Jurij': []}
        self.assertEqual(najvec_vnukov('Friderik I.', tree), 5)
        self.assertEqual(najvec_vnukov('Ulrik I.', tree), 1)
        self.assertEqual(najvec_vnukov('Viljem', tree), 0)
        self.assertEqual(najvec_vnukov('Herman I.', tree), 5)
        self.assertEqual(najvec_vnukov('Herman II.', tree), 3)
        self.assertEqual(najvec_vnukov('Herman III.', tree), 0)
        self.assertEqual(najvec_vnukov('Friderik II.', tree), 3)

    def test_liki(self):
        x = Liki()
        self.assertIsNone(x.krog(0, 0, 1))
        self.assertIsNone(x.krog(2, 3, 2))
        self.assertAlmostEqual(x.ploscina(), math.pi + math.pi * 4)
        self.assertEqual(x.krogi(3), [(0, 0), (2, 3)])
        self.assertEqual(x.krogi(2), [(0, 0)])
        self.assertEqual(x.krogi(1), [])

        x = Liki()
        self.assertIsNone(x.pravokotnik(1, 2, 3, 5))
        self.assertIsNone(x.pravokotnik(9, 7, 6, 4))
        self.assertAlmostEqual(x.ploscina(), 6 + 9)

        x = Liki()
        self.assertIsNone(x.pravokotnik(3, 2, 1, 5))
        self.assertAlmostEqual(x.ploscina(), 6)

        x1 = Liki()
        x2 = Liki()
        self.assertIsNone(x1.krog(1, 2, 3))
        self.assertIsNone(x1.krog(5, 1, 7))
        self.assertIsNone(x1.krog(0, 0, 4))
        self.assertIsNone(x1.pravokotnik(10, 5, 20, 0))
        self.assertIsNone(x1.pravokotnik(0, 0, 1, 1))
        self.assertIsNone(x1.pravokotnik(2, 2, 0, 0))

        self.assertIsNone(x2.pravokotnik(0, 0, 1, 2))
        self.assertIsNone(x2.pravokotnik(0, 0, 1, 3))
        self.assertIsNone(x2.pravokotnik(0, 0, 4, 1))
        self.assertIsNone(x2.pravokotnik(5, 1, 0, 0))
        self.assertIsNone(x2.pravokotnik(1, 6, 0, 0))

        self.assertAlmostEqual(x1.ploscina(), 287.4778563656447)
        self.assertEqual(x1.krogi(10), [(1, 2), (5, 1), (0, 0)])
        self.assertEqual(x1.krogi(4), [(1, 2)])

        self.assertAlmostEqual(x2.ploscina(), 20)


if __name__ == "__main__":
    unittest.main(verbosity = 2)
