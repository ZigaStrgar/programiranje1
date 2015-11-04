ime = "Benjamin"

ime.startswith("B")
ime.find("nj")

kraj = "ljubljana"

kraj.index("lj")  # 0
kraj.rindex("lj")  # 4

kraj.upper()  # Vrne z velikimi črkami
kraj.lower()  # Vrne z malimi črkami
kraj.capitalize()  # Vrne z veliko prvo črko

"Benjamin".count("n")  # Tut dela

kraj.lower().count("l")

ime.replace("min", "maks")

stavek = "    Tole je stavek brez posebnega navdiha      "
stavek = "Tole je stavek brez posebnega navdiha"
stavek.strip()
stavek.split()  # Zelo pametna funkcija :)

stevilka = "713-789-8086"
stevilka.split("-")

besede = stevilka.split()
", ".join(besede[:-1]) + " in " + besede[-1]  # Ne dela s števili
", ".join(map(str, [1, 2, 3]))  # Izpiše: 1, 2, 3

imena = ["Ana", "Berta", "Cilka", "Dani", "Eva", "Fanči"]
for kje, ime in enumerate(imena):
    if ime.count("i") > 0:
        del ime[kje]

# Ne poganjaj for zanke na objektu, ki spreminjaš
kje = 0
while kje < len(imena):
    if "i" in imena[kje]:
        del imena[kje]
    else:
        kje += 1

imena = ["Ana", "Berta", "Cilka", "Ana", "Dani", "Eva", "Fanči"]
for i, ime in enumerate(imena):
    if ime == "Ana":
        print(i)

imena.extend(["Greta", "Helga"])
