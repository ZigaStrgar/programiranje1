je_sodo = False

stevilke = [5, 13, 7, 42, 5, 11, 28, 25, 7]

for stevilka in stevilke:
    if stevilka % 2 == 0:
        je_sodo = True
        break
if je_sodo:
    print("V seznamu so bila tudi soda števila")
else:
    print("V seznamu ni sodih števil")
