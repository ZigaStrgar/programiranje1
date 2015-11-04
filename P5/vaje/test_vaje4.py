def najdaljsa(s):
    naj = None
    naj_be = ""
    for beseda in s.split():
        dolzina = len(beseda)
        if naj is None:
            naj = dolzina
            naj_be = beseda
        elif dolzina > naj:
            naj = dolzina
            naj_be = beseda
    return naj_be


def najkrajsa(besede):
    najkraj = ""
    najmanj = None
    for beseda in besede:
        dolzina = len(beseda)
        if najmanj is None:
            najmanj = dolzina
            najkraj = beseda
        elif dolzina < najmanj:
            najmanj = dolzina
            najkraj = beseda
    return najkraj


def podobnost(s1, s2):
    ujemanje = 0
    if len(s1) < len(s2):
        krajsa = s1
        daljsa = s2
    else:
        krajsa = s2
        daljsa = s1

    for i, char in enumerate(list(krajsa)):
        if char == daljsa[i]:
            ujemanje += 1
    return ujemanje


def sumljive(s):
    sumljive_besede = []
    for word in s.split():
        if word.count("a") > 0 and word.count("u") > 0:
            sumljive_besede.append(word)
    return sumljive_besede


def vsi(xs):
    for x in xs:
        if not x:
            return False
    return True


def vsaj_eden(xs):
    for x in xs:
        if x:
            return True
    return False


def domine(xs):
    new_seznam = list(zip(xs[:-1], xs[1:]))
    for element in new_seznam:
        first = element[0]
        last = element[1]
        if first[1] == last[0]:
            continue
        else:
            return False
    return True


def vsota(sez):
    vs = 0
    for num in sez:
        vs += num
    return vs


def vsota_seznamov(xss):
    seznam = []
    while len(xss) > 0:
        vs = 0
        for num in xss.pop(0):
            vs += num
        seznam.append(vs)
    return seznam


def najvecji_podseznam(xss):
    seznam = []
    naj = None
    for e in xss:
        vs = vsota(e)
        if not naj:
            naj = vs
            seznam = e
        elif naj < vs:
            naj = vs
            seznam = e
    return seznam


def cezar(s):
    words = []
    for word in s.split(" "):
        new = ""
        for char in list(word):
            count = 0
            unic = ord(char)
            while count < 3:
                unic += 1
                if unic > 122:
                    unic = 97
                count += 1
            new += chr(unic)
        words.append(new)
    return " ".join(words)


def mrange(start, faktor, dolzina):
    seznam = []
    while dolzina > 0:
        seznam.append(start)
        start = start * faktor
        dolzina -= 1
    return seznam


def slikaj(f, xs):
    seznam = []
    for e in xs:
        seznam.append(f(e))
    return seznam

### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest


def fail_msg(args):
    return 'Failed on input: {}'.format(repr(args))


class TestVaje4(unittest.TestCase):
    def test_najdaljsa(self):
        in_out = [
            ('beseda', 'beseda'),
            ('an ban', 'ban'),
            ('an ban pet podgan', 'podgan'),
            ('an ban pet podgan stiri misi', 'podgan'),
            ('ta clanek je lepo napisan', 'napisan'),
            ('123456 12345 1234 123 12 1', '123456'),
            ('12345 123456 12345 1234 123 12 1', '123456'),
            ('1234 12345 123456 12345 1234 123 12 1', '123456'),
        ]

        for i, o in in_out:
            self.assertEqual(najdaljsa(i), o, fail_msg(i))

    def test_podobnost(self):
        in_out = [
            (('sobota', 'robot'), 4),
            (('', 'robot'), 0),
            (('sobota', ''), 0),
            (('', ''), 0),
            (('a', 'b'), 0),
            (('a', 'a'), 1),
            (('aaa', 'a'), 1),
            (('amper', 'amonijak'), 2),
            (('1000 let', 'tisoc let'), 0),
            (('hamming distance', 'haming  distance'), 12)
        ]

        for i, o in in_out:
            self.assertEqual(podobnost(*i), o, fail_msg(i))
            self.assertEqual(podobnost(*i[::-1]), o, fail_msg(i))

    def test_sumljive(self):
        in_out = [
            ('', []),
            ('aa uu', []),
            ('aa uu au', ['au']),
            ('muha', ['muha']),
            ('Muha pa je rekla: "Tale juha se je pa res prilegla, najlepša huala," in odletela.',
             ['Muha', 'juha', 'huala,"']),
            ('ameba nima aja in uja, ampak samo a', ['uja,']),
        ]

        for i, o in in_out:
            self.assertListEqual(sumljive(i), o, fail_msg(i))

    def test_vsi(self):
        in_out = [
            ([True, True, False], False),
            ([True, True], True),
            ([1, 2, 3, 0], False),
            (['foo', 42, True], True),
            (['foo', '', 42, True], False),
            (['foo', 0.0, 42, True], False),
            (['foo', None, 42, True], False),
            (['foo', (), 42, True], False),
            (['foo', [], 42, True], False),
            ([], True),
        ]

        for i, o in in_out:
            f = self.assertTrue if o else self.assertFalse
            f(vsi(i), fail_msg(i))

    def test_vsaj_eden(self):
        in_out = [
            ([2, 3, 0], True),
            ([], False),
            ([True, False, False], True),
            ([False, False], False),
            (['foo', 42, True], True),
            ([False, 0, 0.0, '', None, (), []], False),
            ([False, 0, 0.42, '', None, (), []], True),
            ([False, 0, 0.0, '', None, (), [42]], True),
        ]

        for i, o in in_out:
            f = self.assertTrue if o else self.assertFalse
            f(vsaj_eden(i), fail_msg(i))

    def test_domine(self):
        in_out = [
            ([], True),
            ([(2, 4), (4, 4)], True),
            ([(2, 4), (4, 4), (4, 2)], True),
            ([(2, 4), (4, 4), (4, 2), (2, 9), (9, 1)], True),
            ([(2, 4), (4, 3), (4, 2), (2, 9), (9, 1)], False),
            ([(3, 6), (6, 6), (6, 1), (1, 0)], True),
            ([(3, 6), (6, 6), (2, 3)], False),
        ]

        for i, o in in_out:
            f = self.assertTrue if o else self.assertFalse
            f(domine(i), fail_msg(i))

    def test_vsota_seznamov(self):
        in_out = [
            ([], []),
            ([[]], [0]),
            ([[0]], [0]),
            ([[1, 2]], [3]),
            ([[1, 2], [], [0]], [3, 0, 0]),
            ([[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]], [7, 4, 0, 10, 4]),
            ([[5, 3, 6, 3], [1, 2, 3, 4], [5, -1, 0]], [17, 10, 4]),
        ]

        for i, o in in_out:
            self.assertEqual(vsota_seznamov(i), o, fail_msg(i))

    def test_najvecji_podseznam(self):
        in_out = [
            ([[0]], [0]),
            ([[1, 2]], [1, 2]),
            ([[1, 2], [], [0]], [1, 2]),
            ([[2, 4, 1], [3, 1], [], [8, 2], [1, 1, 1, 1]], [8, 2]),
            ([[5, 3, 6, 3], [1, 2, 3, 4], [5, -1, 0]], [5, 3, 6, 3]),
        ]

        for i, o in in_out:
            self.assertEqual(najvecji_podseznam(i), o, fail_msg(i))

    def test_cezar(self):
        in_out = [
            ('', ''),
            ('a', 'd'),
            ('aa', 'dd'),
            ('ab', 'de'),
            ('z', 'c'),
            ('xyz', 'abc'),
            (' ', ' '),
            ('a  a', 'd  d'),
            ('julij cezar je seveda uporabljal cezarjevo sifro',
             'mxolm fhcdu mh vhyhgd xsrudeomdo fhcdumhyr vliur'),
            ('the quick brown fox jumps over the lazy dog',
             'wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj'),
        ]

        for i, o in in_out:
            self.assertEqual(cezar(i), o, fail_msg(i))

    def test_mrange(self):
        in_out = [
            ((32, 2, 0), []),
            ((32, 2, 1), [32]),
            ((32, 2, 2), [32, 64]),
            ((42, -1, 5), [42, -42, 42, -42, 42]),
            ((7, 4, 7), [7, 28, 112, 448, 1792, 7168, 28672]),
        ]

        for i, o in in_out:
            self.assertListEqual(mrange(*i), o, fail_msg(i))

    def test_slikaj(self):
        in_out = [
            ((abs, [-5, 8, -3, -1, 3]), [5, 8, 3, 1, 3]),
            ((len, 'Daydream delusion limousine eyelash'.split()), [8, 8, 9, 7]),
            ((int, '1 3 5 42'.split()), [1, 3, 5, 42]),
        ]

        for i, o in in_out:
            self.assertListEqual(slikaj(*i), o, fail_msg(i))


if __name__ == '__main__':
    unittest.main(verbosity = 2)
