"""x = 1
najv = 0
while x != 0:
    x = int(input("Vnesi število: "))
    if x > najv:
        najv = x
print(najv)"""

teze = [74, 82, 58, 66, 61, 84]
imena = ["Anže", "Benjamin", "Cilka", "Dani", "Eva", "Franc"]
studentka = [False, False, True, False, True, False]

podatki = [
    (74, "Anže", False),
    (82, "Benjamin", False),
    (58, "Cilka", True),
    (66, "Dani", False),
    (61, "Eva", True),
    (84, "Franci", False),
]

for ime, teza in zip(imena, teze):
    print(ime, "tehta", teza, "kg")

for teza, ime, studentka in podatki:
    print(ime, "tehta", teza, "kg")

"""
prazen = []
vsota = 0
for x in teze:
    vsota += x
print(vsota / len(teze))"""

#print(podatki)
