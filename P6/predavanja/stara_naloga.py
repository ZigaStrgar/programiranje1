import collections


def v_sekunde(s):
    h, m, s = s.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


def podatki(vrstica):
    mesto, stevilka, ime, leto, drzava, cas1, cas2 = vrstica.split("\t")
    return ime, int(leto), v_sekunde(cas1), v_sekunde(cas2)


def pospesek(vrstica):
    ime, leto, cas1, cas2 = podatki(vrstica)
    return (cas2 - cas1) / cas1


def naj_pospesek(vrstice):
    return podatki(min(vrstice, key = pospesek))[0]


def vsi_pospeseni(vrstice, faktor):
    pospeseni = []
    for vrsica in vrstice:
        ime, leto, cas1, cas2 = podatki(vrsica)
        if cas2 - cas1 <= cas1 * faktor:
            pospeseni.append(ime)
    return pospeseni


def vsi_pospeseni(vrstice, faktor):
    return [podatki(vrstica)[0] for vrstica in vrstice if pospesek(vrstica) <= faktor]


def leta(vrstice):
    s = []
    for vrstica in vrstice:
        ime, leto, cas1, cas2 = podatki(vrstica)
        if not leto in s:
            s.append(leto)
    return sorted(s)


def tekaci_leta(vrstice, leto):
    imena = []
    for vrstica in vrstice:
        ime, leto1, cas1, cas2 = podatki(vrstica)
        if leto1 == leto:
            imena.append(ime)
    if not imena:
        return ""
    if len(imena) == 1:
        return imena[0]
    return ", ".join(imena[:-1]) + " in " + imena[-1]


def najboljsi_po_letih(vrstice):
    rekordeji = []
    for vrstica in vrstice:
        ime, leto, cas1, cas2 = podatki(vrstica)
        for i, (leto1, ime2, cas) in enumerate(rekordeji):
            if leto == leto1:
                if cas2 < cas:
                    rekordeji[i] = (leto, ime2, cas2)
                break
        else:
            rekordeji.append((leto, ime, cas2))
    po_letih = []
    for leto, ime, cas in rekordeji:
        po_letih.append((leto, ime))
    return sorted(po_letih)


def najboljsi_po_letih(vrstice):
    rekorderji = [("", 42)] * 115
    for vrstica in vrstice:
        ime, leto, cas1, cas2 = podatki(vrstica)
        naj_ime, naj_cas = rekorderji[leto - 1900]
        if naj_ime == "" or cas2 < naj_cas:
            rekorderji[leto - 1900] = ime, cas2
    po_letih = []
    for leto, (ime, cas) in enumerate(rekorderji):
        if ime:
            po_letih.append((leto + 1900, ime))
    return po_letih


def leta(vrstice):
    vsa_leta = set()
    for vrstica in vrstice:
        ime, leto, cas1, cas2 = podatki(vrstica)
        vsa_leta.add(leto)
    return sorted(vsa_leta)


vrstice = open("10z.txt")

# Navadi se uporabljat defaultdict
# Slaba navada
# po_letih = {}
# for vrstica in vrstice:
#    ime, leto, cas1, cas2 = podatki(vrstica)
#    if leto in po_letih:
#        po_letih[leto].append(ime)
#    else:
#        po_letih[leto] = [ime]

# Dobra navada
po_letih = collections.defaultdict(list)
for vrstica in vrstice:
    ime, leto, cas1, cas2 = podatki(vrstica)
    po_letih[leto] += [ime]
print(po_letih[1985])

print(sorted(po_letih))  # Zanka for izpisuje ključe, tako da to dela

meti = [5, 1, 6, 1, 3, 6, 4, 4, 2]

pogostosti = collections.Counter(meti)

pogostosti = collections.Counter(meti)

import unittest


class TestMaraton(unittest.TestCase):
    def test_v_sekunde(self):
        self.assertEqual(v_sekunde("00:00:00"), 0)
        self.assertEqual(v_sekunde("00:00:01"), 1)
        self.assertEqual(v_sekunde("00:00:02"), 2)
        self.assertEqual(v_sekunde("00:01:00"), 60)
        self.assertEqual(v_sekunde("00:02:00"), 120)
        self.assertEqual(v_sekunde("02:00:00"), 7200)
        self.assertEqual(v_sekunde("02:02:02"), 7322)
        self.assertEqual(v_sekunde("1:03:46"), 3826)
        self.assertEqual(v_sekunde("01:03:46"), 3826)
        self.assertEqual(v_sekunde("01:3:46"), 3826)
        self.assertEqual(v_sekunde("01:30:6"), 5406)
        self.assertEqual(v_sekunde("01:2:15"), 3735)

    def test_iz_sekund(self):
        self.assertEqual(iz_sekund(0), "0:0:0")
        self.assertEqual(iz_sekund(1), "0:0:1")
        self.assertEqual(iz_sekund(60), "0:1:0")
        self.assertEqual(iz_sekund(61), "0:1:1")
        self.assertEqual(iz_sekund(62), "0:1:2")
        self.assertEqual(iz_sekund(122), "0:2:2")
        self.assertEqual(iz_sekund(3600), "1:0:0")
        self.assertEqual(iz_sekund(3666), "1:1:6")

    def test_podatki(self):
        self.assertEqual(podatki("1\t14895\tROMAN SONJA\t1979\tSLO\t0:16:39\t0:33:32"),
                         ("ROMAN SONJA", 1979, 999, 2012))
        self.assertEqual(podatki("1\t14895\tROMAN B. SONJA\t1979\tSLO\t0:16:39\t0:33:32"),
                         ("ROMAN B. SONJA", 1979, 999, 2012))

    def test_razlika(self):
        self.assertEqual(pospesek("1\t14895\tROMAN SONJA\t1979\tSLO\t0:16:10\t0:32:20"), 1)
        self.assertEqual(pospesek("1\t14895\tROMAN SONJA\t1979\tSLO\t0:16:10\t0:48:30"), 2)
        self.assertEqual(pospesek("1\t14895\tROMAN SONJA\t1979\tSLO\t0:16:10\t0:24:15"), 0.5)

    @property
    def realdata(self):
        return open("10z.txt", encoding = "utf-8")

    def test_naj_razlika(self):
        self.assertEqual(naj_pospesek(self.realdata), "GRUDEN SONJA")

    def test_vsi_pospeseni(self):
        self.assertEqual(
            vsi_pospeseni(self.realdata, 0.85),
            ['GRUDEN SONJA', 'DEBELJAK MOJCA', 'MESTNIK LARA', 'BALANT ZDENKA', 'HOSTA ANJA'])

    def test_leta(self):
        self.assertEqual(
            leta(self.realdata),
            [1937, 1938, 1942, 1943] + list(range(1946, 2004)) + [2005, 2006])

    def test_tekaci_leta(self):
        self.assertEqual(tekaci_leta(self.realdata, 1948), 'JAGER JOŽICA, KOČEVAR MILA in RUPAR ALENKA')
        self.assertEqual(tekaci_leta(self.realdata, 1947), "BOLE MARIJA")
        self.assertEqual(tekaci_leta(self.realdata, 1945), "")

    def test_najboljsi_po_letih(self):
        self.assertEqual(
            najboljsi_po_letih(self.realdata),
            [(1937, 'MCNALLY ETHEL'), (1938, 'PUHAR MIRA'),
             (1942, 'LOUHI REJEC LEENA'), (1943, 'GOLOB IVANA'),
             (1946, 'ŠUŠTERŠIČ DUNJA'), (1947, 'BOLE MARIJA'),
             (1948, 'JAGER JOŽICA'), (1949, 'ŽNIDARŠIČ JOŽICA'),
             (1950, 'KRMAVNAR dAMJANA'), (1951, 'GOMIVNIK VIDA'),
             (1952, 'STRAŠEK DRAGICA'), (1953, 'RINK MARJETA'),
             (1954, 'DOLENEC IRENA'), (1955, 'JERAJ MARIJA'),
             (1956, 'VRTAČNIK BOKAL EDA'), (1957, 'HERMAN EMILIJA'),
             (1958, 'HIRŠMAN ALENKA'), (1959, 'PŠAKER MARIJA'),
             (1960, 'MOČIVNIK ŠKEDELJ BARBKA'), (1961, 'PERAK LUCIJA'),
             (1962, 'NAHTIGAL BRIGITA'), (1963, 'RUPNIK SONJA'),
             (1964, 'OBRČ TEA'), (1965, 'BERKOPEC MARTA'),
             (1966, 'SELJAK BERNARDA'), (1967, 'ČRNILOGAR VESNA'),
             (1968, 'RUPNIK ANDREJA'), (1969, 'ŠTEVANEC MARIJA'),
             (1970, 'AHČIN MATEJKA'), (1971, 'ŽGAJNER MAJDA'),
             (1972, 'HELENA VALAS'), (1973, 'Pirc Alenka'),
             (1974, 'RADIVO MANICA'), (1975, 'CONRADI MARJETKA'),
             (1976, 'VESEL HELENA'), (1977, 'STRUNA NINA'),
             (1978, 'PRAPROTNIK ZALA'), (1979, 'ROMAN SONJA'),
             (1980, 'BRODNIK NIKA'), (1981, 'LEMUT KLEMENTINA'),
             (1982, 'PAVLIČ MARY'), (1983, 'MUŠIČ RADEJ NINA'),
             (1984, 'FAJDIGA ANJA'), (1985, 'PLANOVŠEK ANA'),
             (1986, 'ŽUNIČ KATJA'), (1987, 'MIKLAVŽIN MAJA'),
             (1988, 'BERČIČ KATJA'), (1989, 'KOPAČ POLONA'),
             (1990, 'MUŠIČ MATEJA'), (1991, 'VIDMAR SARA'),
             (1992, 'MEJAČ ANJA'), (1993, 'KOZJEK TINA'),
             (1994, 'MIŠMAŠ MARUŠA'), (1995, 'ŽGAJNER JERNEJA'),
             (1996, 'VAN DE VOORDE MAGDALENA'), (1997, 'GUZELJ BLATNIK LAURA'),
             (1998, 'LEŠNJAK ANA'), (1999, 'ČESNIK TINA'),
             (2000, 'STAUBER LAURA'), (2001, 'MIHEVC LARA'),
             (2002, 'MALI KLARA'), (2003, 'FERJANČIČ MAŠA'),
             (2005, 'SLAPNIK AŠA'), (2006, 'MEGLIČ AJŠA')])


if __name__ == "__main__":
    unittest.main()
