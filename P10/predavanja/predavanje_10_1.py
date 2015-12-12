rodbina = {"Adam": ["Matjaž", "Cilka", "Daniel", "Erik"], "Aleksander": [], "Alenka": [], "Barbara": [], "Cilka": [],
           "Daniel": ["Elizabeta", "Hans"], "Erik": [], "Elizabeta": ["Ludvik", "Jurij", "Barbara", "Herman", "Mihael"],
           "Franc": [], "Herman": ["Margareta"], "Hans": [], "Jožef": ["Alenka", "Aleksander", "Petra"],
           "Jurij": ["Franc", "Jožef"], "Ludvik": [], "Margareta": [], "Matjaž": ["Viljem"], "Mihael": [], "Petra": [],
           "Tadeja": [], "Viljem": ["Tadeja"]}

starost = {"Adam": 111, "Matjaž": 90, "Cilka": 88, "Daniel": 85, "Erik": 83, "Viljem": 58, "Tadeja": 20,
           "Elizabeta": 67, "Hans": 64, "Ludvik": 50, "Jurij": 49, "Barbara": 45, "Herman": 39, "Mihael": 32,
           "Franc": 30, "Jožef": 29, "Margareta": 10, "Alenka": 5, "Aleksander": 7, "Petra": 9}


def otroci(oseba):
    return rodbina[oseba]


def st_vnukov(oseba):
    sk = 0
    for otrok in otroci(oseba):
        sk += len(otroci(otrok))
    return sk


def velikost_rodbine(oseba):
    velikost = 1
    for otrok in otroci(oseba):
        velikost += velikost_rodbine(otrok)
    return velikost


def velikost_rodbine(oseba):
    return 1 + sum(velikost_rodbine(otrok) for otrok in otroci(oseba))


def obstaja(oseba, ime):
    if oseba == ime:
        return True
    for otrok in otroci(oseba):
        if obstaja(otrok, ime):
            return True
    return False


def obstaja(oseba, ime):
    return oseba == ime or any(obstaja(otrok, ime) for otrok in otroci(oseba))


def najvecja(oseba):
    moji_otroci = otroci(oseba)
    n = len(moji_otroci)
    for otrok in moji_otroci:
        no = najvecja(otrok)
        if no > n:
            n = no
    return n


def imena(oseba):
    vsa = {oseba}
    for otrok in otroci(oseba):
        vsa = vsa | imena(otrok)
    return vsa


def st_potomci(oseba):
    return sum(velikost_rodbine(otrok) for otrok in otroci(oseba))


print(st_potomci("Jurij"))
