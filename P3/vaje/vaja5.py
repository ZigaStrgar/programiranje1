xs = [42, 5, 4, -7, 2, 12, -3, -4, 11, 42, 2]
contains = True

for number in xs:
    if 42 % number != 0:
        contains = False
        break
print(contains)

