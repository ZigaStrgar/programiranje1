import unittest


def capitalize(sez):
    return [name.capitalize() for name in sez]


def icapitalize(imena):
    for i, ime in enumerate(imena):
        imena[i] = ime.capitalize()


def get_sum(n):
    return sum([int(stevilka) for stevilka in list(str(n))])


def count(n):
    while len(str(n)) > 1:
        n = get_sum(n)
    return n


def delitelji(n):
    return [x for x in range(1, n + 1) if n % x == 0]


def postnina(n):
    sez = []
    delitelji_seznam = delitelji(n)
    for x in delitelji_seznam:
        for y in delitelji_seznam:
            z = int(n / x / y)
            if x * y * z == n and z in delitelji_seznam:
                sez.append(x + y + z)
    return sorted(sez)[0]


def nic_ena(xs):
    i = 0
    prev = xs[0]
    sez = []
    vs = 0
    while i < len(xs):
        if prev != xs[i]:
            sez.append(vs)
            vs = 1
            prev = xs[i]
        else:
            vs += 1
        i += 1
    sez.append(vs)
    numb = sum([sez[x] for x in range(2, len(sez), 2)]) - sez[0]
    if numb < sum([sez[x] for x in range(1, len(sez)-1, 2)]) - sez[len(sez)-1]:
        return numb
    else:
        return sum([sez[x] for x in range(1, len(sez)-1, 2)]) - sez[len(sez)-1]
    return None


class TestNaloge8(unittest.TestCase):
    def test_capitalize(self):
        imena = ['marko', 'Miha', 'maja', 'Monika']
        self.assertEqual(capitalize(imena), ['Marko', 'Miha', 'Maja', 'Monika'])
        self.assertEqual(imena, ['marko', 'Miha', 'maja', 'Monika'])

        imena = ['ana', 'anja', 'alen', 'aljana', 'angelika']
        self.assertEqual(capitalize(imena), ['Ana', 'Anja', 'Alen', 'Aljana', 'Angelika'])
        self.assertEqual(imena, ['ana', 'anja', 'alen', 'aljana', 'angelika'])

    def test_icapitalize(self):
        imena = ['marko', 'Miha', 'maja', 'Monika']
        self.assertIsNone(icapitalize(imena))
        self.assertEqual(imena, ['Marko', 'Miha', 'Maja', 'Monika'])

        imena = ['ana', 'anja', 'alen', 'aljana', 'angelika']
        self.assertIsNone(icapitalize(imena))
        self.assertEqual(imena, ['Ana', 'Anja', 'Alen', 'Aljana', 'Angelika'])

    def test_count(self):
        self.assertEqual(count(1), 1)
        self.assertEqual(count(23), 5)
        self.assertEqual(count(12345), 6)
        self.assertEqual(count(999999999), 9)
        self.assertEqual(count(213413512), 4)
        self.assertEqual(count(2147483647), 1)
        self.assertEqual(count(21499999997483999999964999919997), 2)

    def test_postnina(self):
        self.assertEqual(postnina(1), 3)
        self.assertEqual(postnina(6), 6)
        self.assertEqual(postnina(7), 9)
        self.assertEqual(postnina(10), 8)
        self.assertEqual(postnina(100), 14)
        self.assertEqual(postnina(200), 18)
        self.assertEqual(postnina(300), 21)

    def test_nic_ena(self):
        self.assertEqual(nic_ena([0, 0, 1, 0, 1]), 1)
        self.assertEqual(nic_ena([0, 0, 1, 1, 1]), 0)
        self.assertEqual(nic_ena([0, 1, 0, 1, 0]), 2)
        self.assertEqual(nic_ena([1, 1, 1, 1, 0, 0, 0]), 3)
        self.assertEqual(nic_ena([1, 0, 0, 0, 1, 1, 1, 0]), 2)
        self.assertEqual(nic_ena([0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0]), 6)
        self.assertEqual(nic_ena([0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0]), 9)
        self.assertEqual(nic_ena([1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]), 10)

    def test_mask(self):
        self.assertCountEqual(mask(0), [[]])
        self.assertCountEqual(mask(1), [[0], [1]])
        self.assertCountEqual(mask(2), [[0, 0], [0, 1], [1, 0], [1, 1]])
        self.assertCountEqual(mask(3),
                              [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
        self.assertEqual(len(mask(10)), 1024)
        self.assertEqual(len(mask(16)), 65536)

    def test_knjige(self):
        self.assertTrue(knjige([10, 20, 30]))
        self.assertTrue(knjige([10, 20, 30, 40]))
        self.assertTrue(knjige([11, 20, 12, 42, 20, 20, 11, 20, 20, 20, 4]))
        self.assertTrue(knjige([23, 51, 51, 153, 20, 25, 51, 59, 39, 35, 91]))
        self.assertTrue(knjige([33, 9, 15, 14, 7, 35, 13, 8, 38, 10, 60, 14, 12, 56]))
        self.assertTrue(knjige([101, 42, 132, 41, 120, 301, 401, 180, 150, 11, 11]))

        self.assertFalse(knjige([10, 20, 30, 40, 50]))
        self.assertFalse(knjige([11, 20, 12, 42, 22, 20, 11, 20, 20, 20, 4]))
        self.assertFalse(knjige([23, 51, 51, 153, 25, 51, 59, 39, 35, 91]))
        self.assertFalse(knjige([101, 42, 132, 41, 120, 301, 401, 180]))


if __name__ == '__main__':
    unittest.main(verbosity = 2)
