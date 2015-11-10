# Zelo dodatna naloga spodaj :)

import re
import urllib.request


def v_sekunde(time):
    seconds = 0
    multiply = 3600
    for part in time.split(":"):
        seconds += int(part) * multiply
        multiply /= 60
    return int(seconds)


def iz_sekund(time):
    hours = time // 3600
    time -= hours * 3600
    minutes = time // 60
    time -= minutes * 60
    return str(hours) + ":" + str(minutes) + ":" + str(time)


def podatki(s):
    sez = []
    elements = s.split("\t")
    sez.append(elements[2])
    sez.append(int(elements[3]))
    sez.append(v_sekunde(elements[5]))
    sez.append(v_sekunde(elements[6]))
    return tuple(sez)


def pospesek(row):
    return (podatki(row)[3] - podatki(row)[2]) / podatki(row)[2]


def naj_pospesek(rows):
    highest = None
    runner = []
    for row in rows:
        current = pospesek(row)
        if not highest or current < highest:
            highest = current
            runner = podatki(row)
    return runner[0]


def vsi_pospeseni(rows, factor):
    sez = []
    for row in rows:
        if pospesek(row) <= factor:
            sez.append(podatki(row)[0])
    return sez


def leta(rows):
    years = []
    for row in rows:
        if podatki(row)[1] not in years:
            years.append(podatki(row)[1])
    return sorted(years)


def tekaci_leta(rows, year):
    sez = []
    for row in rows:
        runner = podatki(row)
        if runner[1] == year:
            sez.append(runner[0])
    if len(sez) > 1:
        return ", ".join(sez[:-1]) + " in " + sez[-1]
    else:
        return ", ".join(sez)


def najboljsi_po_letih(rows):
    sez_rows = []
    for row in rows:
        sez_rows.append(row)
    years = leta(sez_rows)
    sez = []
    for year in years:
        best = None
        best_name = None
        for row in sez_rows:
            data = podatki(row)
            if data[1] == year:
                if not best or best > data[3]:
                    best = data[3]
                    best_name = data[0]
        sez.append((year, best_name))
    return sez


def get_data(url):
    req = urllib.request.Request(url)
    req.add_header("Content-Type", "text/html; charset=utf-8")
    req.add_header('Accept-Encoding', 'utf-8')
    resp = urllib.request.urlopen(req)
    respdata = resp.read().decode("windows-1250")
    return re.findall('<TR class=r0>(.*?)</TR>', str(respdata))


def file_name(url):
    name = url.split("/")
    name = name[-1]
    name = name.split(".")
    return name[0].lower() + ".txt"


def correct_data(row):
    row = row.replace("<TD>", "<td>")
    row = row.replace("</TD>", "</td>")
    row = row.replace("<td>", "")
    row = row.split("</td>")
    return row


def dodatna(url):
    data = get_data(url)  # Create and send request
    file = open(file_name(url), 'w+')  # Trying to create a new file or open one

    for row in data:
        row = correct_data(row)  # Correctly split and replace data in table
        count = 0
        line = []
        while count < len(row) - 2:
            line.append(row[count])
            count += 1
        string = "\t".join(line)
        file.write(string + "\n")
    file.close()

# dodatna("http://timingljubljana.si/lm/42M.asp")  # Moški 42km
# dodatna("http://timingljubljana.si/lm/42Z.asp")  # Ženske 42km
# dodatna("http://timingljubljana.si/lm/21M.asp")  # Moški 21km
# dodatna("http://timingljubljana.si/lm/21Z.asp")  # Ženske 21km
# dodatna("http://timingljubljana.si/lm/10M.asp")  # Moški 10km
# dodatna("http://timingljubljana.si/lm/HM.asp")  # Handbike moški 21km
# dodatna("http://timingljubljana.si/lm/HZ.asp")  # Handbike ženske 21km
# dodatna("http://timingljubljana.si/lm/DPMC.asp")  # Državno prvenstvo moški 42km
# dodatna("http://timingljubljana.si/lm/DPZC.asp")  # Državno prvenstvo ženske 42km
# dodatna("http://timingljubljana.si/lm/RZ.asp")  # Rolerji moški
# dodatna("http://timingljubljana.si/lm/RM.asp")  # Rolerji ženske


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
