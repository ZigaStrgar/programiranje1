from math import sqrt

k = [9, 16, 81, 25, 196, 256]

s = [sqrt(x) for x in k]
r = [r ** 2 for r in k]

imena = ["Aljaž", "Barbi", "Cilka", "Dani", "Ema"]

dolzina = sum([len(ime) for ime in imena]) / len(imena)


podatki = [
    (74, "Anže", False),
    (82, "Benjamin", False),
    (58, "Cilka", True),
    (66, "Dani", False),
    (61, "Eva", True),
    (84, "Franci", False),
]

teze = [teza for teza, ime, zenska in podatki if not zenska]
povp_teza = sum(teze) / len(teze)

sez_imen = [ime for ime in imena if "n" in ime]
sez_imen2 = [ime for ime in imena if ime.endswith("a")]
sez_imen3 = [ime for ime in imena if len(a) < 5]
sez_imen4 = [len(ime) for ime in imena if ime.endswith("a")]
s = sum(sez_imen4) / len(sez_imen4)

stevila = sum([x ** 2 for x in range(1, 101)])
stevila2 = sum([x ** 2 for x in range(1, 101) if x % 7 != 0])
sez_x = [x for x in range(1, 101) if x % 7 != 0 and "7" not in str(x)]

koreni = {x: sqrt(x) for x in range(1, 101)}

