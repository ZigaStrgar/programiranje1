import math

math.sqrt(12)
math.pi

import random

random.random()

random.randint(10, 20)  # Meje so vključene

imena = ["Ana", "Berta", "Cilka", "Dani"]

random.choice(imena)  # Nakjljučno izbere iz seznama

random.shuffle(imena)  # Zmešaj seznam

import os

os.listdir("/users/zigastrgar/desktop")

os.listdir(".")

os.getswd()  # Trenutni direktorij

os.chdir("/nekineki")  # Zamenjaj direktorij

os.path.splitext("datoteka.txt")  # Vrne terko ("datoteka", ".txt")

os.remove("./Pot/datoteka")  # Brisanje datoteke

os.rename(".sh_hisotry", "sh_history")
