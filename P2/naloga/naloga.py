x = 0
num = 2
while x < 4:
    delitelj = 2
    vsota = 1
    while delitelj < num:
        if num % delitelj == 0:
            vsota += delitelj
        delitelj += 1
    if vsota == num:
        print(num)
        x += 1
    num += 1
