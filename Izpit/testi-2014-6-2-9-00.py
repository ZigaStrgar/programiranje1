# Razreda Racunalnik_Sodo in Racunalnik_Sudo lahko napisete kar pod tem
# razredom.

class Racunalnik:
    def izracunaj(self, a, b, geslo):
        if self.preveri_geslo(geslo):
            return a + b

    def preveri_geslo(self, geslo):
        return True


# ---> Tule prideta Racunalnik_Sodo in Racunalnik_Sudo


def ostanki(vrt, pot):
    vrt2 = vrt.copy()
    x = 0
    vrt2[0] = 0
    for move in pot:
        x += move
        if vrt2[x] == 0:
            break
        vrt2[x] = 0
    return sum(vrt2)


def pretakanje(s):
    cups = {"A": 0, "B": 1, "P": 2}
    sizes = 5, 8, 1000
    content = [0, 0, 1000]
    for x in s:
        x = x.split("->")
        iz, v = cups[x[0]], cups[x[1]]
        if content[iz] + content[v] < sizes[v]:
            content[v] += content[iz]
            content[iz] = 0
        else:
            content[iz] -= sizes[v] - content[v]
            content[v] = sizes[v]
    return content[0], content[1]


def izplacilo(bankovci, znesek):
    for bankovec, kolicina in sorted(bankovci.items(), reverse = True):
        if znesek >= bankovec:
            st = znesek // bankovec
            if st >= bankovci[bankovec]:
                st = bankovci[bankovec]
                del bankovci[bankovec]
            else:
                bankovci[bankovec] -= st
            znesek -= bankovec * st


def crv(drevo):
    st = 0
    for veja, moznosti in drevo.items():
        if veja == "zelena":
            st = max(st, crv(moznosti) + 1)
    return st


class Racunalnik_Sudo(Racunalnik):
    def preveri_geslo(self, geslo):
        return geslo == "sudo"


class Racunalnik_Sodo(Racunalnik):
    def preveri_geslo(self, geslo):
        return geslo % 2 == 0


import unittest


class Test_1_Ostanki(unittest.TestCase):
    def test_konec_poti(self):
        self.assertEqual(ostanki([2, 4, 6, 1, 3, 5], []), 19)
        self.assertEqual(ostanki([2, 4, 6, 1, 3, 5], [1]), 15)
        self.assertEqual(ostanki([2, 4, 6, 1, 3, 5], [4]), 16)
        self.assertEqual(ostanki([2, 4, 6, 1, 3, 5], [1, 4, -2]), 9)
        self.assertEqual(ostanki([2, 4, 6, 1, 3, 5], [1, 4, -2, 1]), 6)

    def test_na_prazno(self):
        self.assertEqual(ostanki([0, 4, 6, 1, 3, 5], []), 19)
        self.assertEqual(ostanki([2, 4, 6, 1, 3, 5], [0]), 19)
        self.assertEqual(ostanki([2, 4, 0, 1, 3, 5], [2]), 13)
        self.assertEqual(ostanki([2, 4, 6, 1, 3, 5], [2, -2]), 13)
        self.assertEqual(ostanki([2, 4, 6, 1, 3, 5], [1, 2, 1, -2, -1, 4]), 5)

    def test_vse(self):
        self.assertEqual(ostanki([2, 4, 6, 1, 3], [1, 1, 1, 1]), 0)
        self.assertEqual(ostanki([2, 4, 6, 1, 3], [4, -1, -1, -1]), 0)
        self.assertEqual(ostanki([2, 4, 6, 1, 3], [4, -1, -1, -1, 1]), 0)


class Test_2_Pretakanje(unittest.TestCase):
    def test_prazno(self):
        self.assertEqual(pretakanje([]), (0, 0))

    def test_na_prazno(self):
        self.assertEqual(pretakanje(["A->B"]), (0, 0))
        self.assertEqual(pretakanje(["B->A"]), (0, 0))

    def test_na_polno(self):
        self.assertEqual(pretakanje(["P->A", "P->A"]), (5, 0))
        self.assertEqual(pretakanje(["P->B", "P->B"]), (0, 8))
        self.assertEqual(pretakanje(["P->A", "P->B", "A->B"]), (5, 8))

    def test_razno(self):
        self.assertEqual(pretakanje(["P->A", "A->B"]), (0, 5))
        self.assertEqual(pretakanje(["P->A", "A->B", "P->A"]), (5, 5))
        self.assertEqual(pretakanje(["P->A", "A->B", "P->A", "A->B"]), (2, 8))
        self.assertEqual(pretakanje(["P->A", "A->B", "P->A", "A->B", "B->P"]), (2, 0))
        self.assertEqual(pretakanje(["P->A", "A->B", "P->A", "A->B", "B->P", "A->B"]), (0, 2))
        self.assertEqual(pretakanje(["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A"]), (5, 2))
        self.assertEqual(pretakanje(["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B"]), (0, 7))
        self.assertEqual(pretakanje(["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "B->A"]), (5, 2))
        self.assertEqual(pretakanje(["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A"]), (5, 7))
        self.assertEqual(pretakanje(["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A", "A->B"]),
                         (4, 8))
        self.assertEqual(
                pretakanje(["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A", "A->B", "A->P"]),
                (0, 8))
        self.assertEqual(
                pretakanje(["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A", "A->B", "B->P"]),
                (4, 0))
        self.assertEqual(pretakanje(
                ["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A", "A->B", "B->P", "P->A"]),
                (5, 0))
        self.assertEqual(pretakanje(
                ["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A", "A->B", "B->P", "A->B"]),
                (0, 4))
        self.assertEqual(pretakanje(
                ["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A", "A->B", "B->P", "A->B",
                 "B->P"]), (0, 0))
        self.assertEqual(pretakanje(
                ["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A", "A->B", "B->P", "A->B",
                 "P->A"]), (5, 4))
        self.assertEqual(pretakanje(
                ["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A",
                 "A->B"]), (1, 8))
        self.assertEqual(pretakanje(
                ["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A",
                 "A->B", "B->P"]), (1, 0))
        self.assertEqual(pretakanje(
                ["P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A", "A->B", "P->A", "A->B", "B->P", "A->B", "P->A",
                 "A->B", "B->P", "A->B"]), (0, 1))


class Test_3_Izplacilo(unittest.TestCase):
    def test_blagajna(self):
        # Nasvet "goljufom": ne poskusite uporabljati 'global blagajna'.
        # Ne bo delovalo. Ne more, ker imajo testi *lokalno* spremenljivko
        # blagajna in le-te ne morete spremeniti v globalno.
        blagajna = {}
        self.assertIsNone(izplacilo(blagajna, 0))
        self.assertEqual(blagajna, {})

        blagajna = {100: 8, 20: 7, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 130))
        self.assertEqual(blagajna, {100: 7, 20: 6, 10: 3})

        blagajna = {100: 8, 20: 7, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 700))
        self.assertEqual(blagajna, {100: 1, 20: 7, 10: 4})

        blagajna = {100: 8, 20: 7, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 800))
        self.assertEqual(blagajna, {20: 7, 10: 4})

        blagajna = {100: 8, 20: 7, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 900))
        self.assertEqual(blagajna, {20: 2, 10: 4})

        blagajna = {100: 8, 20: 7, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 910))
        self.assertEqual(blagajna, {20: 2, 10: 3})

        blagajna = {100: 8, 20: 7, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 940))
        self.assertEqual(blagajna, {10: 4})

        blagajna = {100: 8, 20: 7, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 950))
        self.assertEqual(blagajna, {10: 3})

        blagajna = {100: 8, 20: 7, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 980))
        self.assertEqual(blagajna, {})

        blagajna = {100: 8, 50: 7, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 260))
        self.assertEqual(blagajna, {100: 6, 50: 6, 10: 3})

        blagajna = {100: 8, 50: 7, 20: 3, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 260))
        self.assertEqual(blagajna, {100: 6, 50: 6, 20: 3, 10: 3})

        blagajna = {100: 8, 50: 7, 20: 3, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 270))
        self.assertEqual(blagajna, {100: 6, 50: 6, 20: 2, 10: 4})

        blagajna = {100: 8, 50: 7, 20: 3, 10: 4}
        self.assertIsNone(izplacilo(blagajna, 280))
        self.assertEqual(blagajna, {100: 6, 50: 6, 20: 2, 10: 3})


class Test_4_Crv(unittest.TestCase):
    def test_crv(self):
        self.assertEqual(crv({}), 0)
        self.assertEqual(crv({"zelena": {}}), 1)
        self.assertEqual(crv({"suha": {}}), 0)
        self.assertEqual(crv({"suha": {"zelena": {"zelena": {}}}}), 0)
        self.assertEqual(crv({"zelena": {}, "suha": {}}), 1)
        self.assertEqual(crv({"zelena": {"zelena": {}}}), 2)
        self.assertEqual(crv({"zelena": {"zelena": {"zelena": {}}}}), 3)
        self.assertEqual(crv({"zelena": {"zelena": {"zelena": {"zelena": {}}}}}), 4)
        self.assertEqual(crv({"zelena": {"zelena": {"zelena": {"zelena": {"zelena": {}}}}}}), 5)
        self.assertEqual(crv({"suha": {}, "zelena": {"zelena": {"zelena": {"zelena": {"zelena": {}}}}}}), 5)
        self.assertEqual(crv({"suha": {}, "zelena": {"zelena": {"suha": {}, "zelena": {"zelena": {"zelena": {}}}}}}), 5)
        self.assertEqual(
                crv({"suha": {}, "zelena": {"zelena": {"suha": {}, "zelena": {"zelena": {"zelena": {}}, "suha": {}}}}}),
                5)
        self.assertEqual(crv({"suha": {}, "zelena": {
            "zelena": {"suha": {}, "zelena": {"zelena": {"zelena": {"suha": {}}}, "suha": {}}}}}), 5)
        self.assertEqual(crv({"suha": {}, "zelena": {
            "zelena": {"suha": {}, "zelena": {"zelena": {"zelena": {"suha": {}, "zelena": {}}}, "suha": {}}}}}), 6)
        self.assertEqual(crv({"zelena": {"zelena": {"zelena": {"suha": {}}}}}), 3)
        self.assertEqual(crv({"zelena": {"zelena": {"zelena": {"suha": {"zelena": {}}}}}}), 3)

        d1 = {"zelena": {"suha": {"zelena": {"zelena": {}, "zelena": {}}, "suha": {}},
                         "zelena": {"zelena": {"suha": {}, "zelena": {}}, "suha": {}, "suha": {}}}}
        self.assertEqual(crv(d1), 4)


class Test_5_Izracun(unittest.TestCase):
    def test_sodo(self):
        r = Racunalnik_Sodo()
        self.assertIsNone(r.izracunaj(1, 2, 13))
        self.assertEqual(r.izracunaj(1, 2, 42), 3)

    def test_sudo(self):
        r = Racunalnik_Sudo()
        self.assertIsNone(r.izracunaj(1, 2, 13))
        self.assertIsNone(r.izracunaj(1, 2, "foo"))
        self.assertEqual(r.izracunaj(1, 2, "sudo"), 3)
