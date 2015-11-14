def koodrinate(kraj, kraji):
    for ime, x, y in kraji:
        if ime == kraj:
            return x, y


kraji = {
    'Brežice': (68.66, 7.04),
    'Lenart': (85.20, 78.75),
    'Rateče': (-65.04, 70.04),
    'Ljutomer': (111.26, 71.82),
    'Rogaška Slatina': (71.00, 42.00),
    'Ribnica': (7.10, -10.50),
    'Dutovlje': (-56.80, -6.93),
    'Lokve': (-57.94, 19.32),
    'Vinica': (43.81, -38.43),
    'Brtonigla': (-71.00, -47.25),
    'Kanal': (-71.00, 26.25),
    'Črnomelj': (39.05, -27.93),
    'Trbovlje': (29.61, 35.07),
    'Beltinci': (114.81, 80.54),
    'Domžale': (-2.34, 31.50)
}


def koodrinate(kraj, kraji):
    return kraji.get(kraj)


napis = "KRNEKI"

vrednost = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

vsota = 0

for c in napis:
    vsota += vrednost.get(c, 0)

print(sum(vrednost.get(c, 0) for c in napis))

for c in napis:
    if c == "I":
        vsota += 1
    elif c == "V":
        vsota += 5
    elif c == "X":
        vsota += 10
    elif c == "L":
        vsota += 50
    elif c == "C":
        vsota += 100
    elif c == "D":
        vsota += 500
    elif c == "M":
        vsota += 1000
