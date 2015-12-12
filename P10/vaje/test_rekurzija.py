otroci = {"Adam": ["Matjaž", "Cilka", "Daniel", "Erik"], "Aleksander": [], "Alenka": [], "Barbara": [], "Cilka": [],
          "Daniel": ["Elizabeta", "Hans"], "Erik": [], "Elizabeta": ["Ludvik", "Jurij", "Barbara", "Herman", "Mihael"],
          "Franc": [], "Herman": ["Margareta"], "Hans": [], "Jožef": ["Alenka", "Aleksander", "Petra"],
          "Jurij": ["Franc", "Jožef"], "Ludvik": [], "Margareta": [], "Matjaž": ["Viljem"], "Mihael": [], "Petra": [],
          "Tadeja": [], "Viljem": ["Tadeja"], }

starost = {"Adam": 111, "Matjaž": 90, "Cilka": 88, "Daniel": 85, "Erik": 83, "Viljem": 58, "Tadeja": 20,
           "Elizabeta": 67, "Hans": 64, "Ludvik": 50, "Jurij": 49, "Barbara": 45, "Herman": 39, "Mihael": 32,
           "Franc": 30, "Jožef": 29, "Margareta": 10, "Alenka": 5, "Aleksander": 7, "Petra": 9}

import unittest
from test.support import captured_stdout


def otroci_f(ime):
    return otroci[ime]


def imena_v_rodbini(ime):
    vsa = {ime}
    for otrok in otroci_f(ime):
        vsa = vsa | imena_v_rodbini(otrok)
    return vsa


def izpis_imen_v_rodbini(oseba):
    print(oseba)
    for otrok in otroci_f(oseba):
        izpis_imen_v_rodbini(otrok)


def najmlajsi_v_rodbini(oseba):
    najmlajsi = starost[oseba]
    najmlajsi_ime = oseba
    for otrok in otroci_f(oseba):
        star, ime = najmlajsi_v_rodbini(otrok)
        if star < najmlajsi:
            najmlajsi = star
            najmlajsi_ime = ime
    return najmlajsi, najmlajsi_ime


def globina_do(od, do):
    if od == do:
        return 0
    n = 0
    moji_otroci = otroci_f(od)
    for otrok in moji_otroci:
        if do in imena_v_rodbini(otrok):
            return globina_do(otrok, do) + 1
    return n


def pot_do(od, do):
    imena = [od]
    if od == do:
        return imena
    moji_otroci = otroci_f(od)
    for otrok in moji_otroci:
        if do in imena_v_rodbini(otrok):
            return imena.append(pot_do(otrok, do))



class TestRekurzija(unittest.TestCase):
    def test_izpis_imen_v_rodbini(self):
        def f(ime):
            with captured_stdout() as stdout:
                izpis_imen_v_rodbini(ime)
            return stdout.getvalue().splitlines()

        self.assertCountEqual(['Hans'], f('Hans'))
        self.assertCountEqual(['Herman', 'Margareta'], f('Herman'))
        self.assertCountEqual(['Jurij', 'Franc', 'Jožef', 'Alenka', 'Aleksander', 'Petra'], f('Jurij'))
        self.assertCountEqual(['Viljem', 'Tadeja'], f('Viljem'))
        self.assertCountEqual(
            ['Daniel', 'Elizabeta', 'Ludvik', 'Jurij', 'Franc', 'Jožef', 'Alenka', 'Aleksander', 'Petra', 'Barbara',
             'Herman', 'Margareta', 'Mihael', 'Hans'], f('Daniel'))
        self.assertCountEqual(
            ['Adam', 'Matjaž', 'Viljem', 'Tadeja', 'Cilka', 'Daniel', 'Elizabeta', 'Ludvik', 'Jurij', 'Franc', 'Jožef',
             'Alenka', 'Aleksander', 'Petra', 'Barbara', 'Herman', 'Margareta', 'Mihael', 'Hans', 'Erik'], f('Adam'))

    def test_imena_v_rodbini(self):
        self.assertCountEqual(['Hans'], imena_v_rodbini('Hans'))
        self.assertCountEqual(['Herman', 'Margareta'], imena_v_rodbini('Herman'))
        self.assertCountEqual(['Jurij', 'Franc', 'Jožef', 'Alenka', 'Aleksander', 'Petra'], imena_v_rodbini('Jurij'))
        self.assertCountEqual(['Viljem', 'Tadeja'], imena_v_rodbini('Viljem'))
        self.assertCountEqual(
            ['Daniel', 'Elizabeta', 'Ludvik', 'Jurij', 'Franc', 'Jožef', 'Alenka', 'Aleksander', 'Petra', 'Barbara',
             'Herman', 'Margareta', 'Mihael', 'Hans'], imena_v_rodbini('Daniel'))
        self.assertCountEqual(
            ['Adam', 'Matjaž', 'Viljem', 'Tadeja', 'Cilka', 'Daniel', 'Elizabeta', 'Ludvik', 'Jurij', 'Franc', 'Jožef',
             'Alenka', 'Aleksander', 'Petra', 'Barbara', 'Herman', 'Margareta', 'Mihael', 'Hans', 'Erik'],
            imena_v_rodbini('Adam'))

    def test_najmlajsi_v_rodbini(self):
        self.assertEqual((64, 'Hans'), najmlajsi_v_rodbini('Hans'))
        self.assertEqual((5, 'Alenka'), najmlajsi_v_rodbini('Daniel'))
        self.assertEqual((10, 'Margareta'), najmlajsi_v_rodbini('Herman'))
        self.assertEqual((20, 'Tadeja'), najmlajsi_v_rodbini('Viljem'))
        self.assertEqual((7, 'Aleksander'), najmlajsi_v_rodbini('Aleksander'))
        self.assertEqual((5, 'Alenka'), najmlajsi_v_rodbini('Adam'))

    def test_globina_do(self):
        self.assertEqual(0, globina_do('Hans', 'Hans'))
        self.assertEqual(1, globina_do('Daniel', 'Hans'))
        self.assertEqual(2, globina_do('Adam', 'Hans'))
        self.assertEqual(4, globina_do('Adam', 'Franc'))
        self.assertEqual(5, globina_do('Adam', 'Petra'))
        self.assertEqual(3, globina_do('Elizabeta', 'Aleksander'))
        self.assertEqual(3, globina_do('Adam', 'Tadeja'))
        self.assertEqual(2, globina_do('Daniel', 'Ludvik'))

    def test_pot_do(self):
        self.assertEqual(['Hans'], pot_do('Hans', 'Hans'))
        self.assertEqual(['Daniel', 'Hans'], pot_do('Daniel', 'Hans'))
        self.assertEqual(['Adam', 'Daniel', 'Hans'], pot_do('Adam', 'Hans'))
        self.assertEqual(['Adam', 'Daniel', 'Elizabeta', 'Jurij', 'Franc'], pot_do('Adam', 'Franc'))
        self.assertEqual(['Adam', 'Daniel', 'Elizabeta', 'Jurij', 'Jožef', 'Petra'], pot_do('Adam', 'Petra'))
        self.assertEqual(['Elizabeta', 'Jurij', 'Jožef', 'Aleksander'], pot_do('Elizabeta', 'Aleksander'))
        self.assertEqual(['Adam', 'Matjaž', 'Viljem', 'Tadeja'], pot_do('Adam', 'Tadeja'))
        self.assertEqual(['Daniel', 'Elizabeta', 'Ludvik'], pot_do('Daniel', 'Ludvik'))

    def test_sum(self):
        self.assertEqual(sum([]), 0)
        self.assertEqual(sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum([1, [], [2, 3, [4]], 5]), 15)
        self.assertEqual(sum([1, [], [2, 3, [4]], 5, [[[[10], 6], [[7], 9], 8]]]), 55)

    def test_convert(self):
        self.assertEqual(convert([]), ())
        self.assertEqual(convert([1]), (1, ()))
        self.assertEqual(convert([5, 4, 6, 7, 1]), (5, (4, (6, (7, (1, ()))))))
        self.assertEqual(convert([5, 4, 6, 7, 1, 0]), (5, (4, (6, (7, (1, (0, ())))))))

    def test_length(self):
        self.assertEqual(length(()), 0)
        self.assertEqual(length((1, ())), 1)
        self.assertEqual(length((5, (4, (6, (7, (1, ())))))), 5)
        self.assertEqual(length((5, (4, (6, (7, (1, (0, ()))))))), 6)

    def test_dup(self):
        self.assertEqual(dup((1, (2, ()))), (1, (1, (2, (2, ())))))
        self.assertEqual(dup((5, (4, (6, (7, (1, ())))))), (5, (5, (4, (4, (6, (6, (7, (7, (1, (1, ())))))))))))

    def test_reverse(self):
        self.assertEqual(reverse((5, (4, (6, (7, (1, ())))))), (1, (7, (6, (4, (5, ()))))))


if __name__ == '__main__':
    unittest.main(verbosity = 2)
