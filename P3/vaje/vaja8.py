number = int(input("Vnesi število: "))

delitelj = 2
vsota = 1

while delitelj < number:
    if number % delitelj == 0:
        vsota += delitelj
    delitelj += 1

delitelj = 2
vsota2 = 1

while delitelj < vsota:
    if vsota % delitelj == 0:
        vsota2 += delitelj
    delitelj += 1

if vsota2 == number:
    print(vsota)
else:
    print(number, "nima prijateljev")
