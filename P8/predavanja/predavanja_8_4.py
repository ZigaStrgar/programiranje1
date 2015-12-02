from math import sqrt

beseda = "MELODIJA"
beseda2 = "DELODAJALEC"

ujemanje = sum([c1 == c2 for c1, c2 in zip(beseda, beseda2)])
print(ujemanje)

a = [2, 1, -3]
b = [3, 5, 4]

vektorji = sqrt(sum([(ai - bi) ** 2 for ai, bi in zip(a, b)]))
print(vektorji)

n = 42

all([n % i for i in range(2, n)])  # Ali je n praštevilo

t = (sqrt(x) for x in range(1, 101))  # Ni terka, je veliko bolj zanimiva. Ta stvar "blefira", ne moreš zahtevat samo xyz element iz objekta. Lahko samo iteriraš z for. Pa še to samo enkrat. GENERATOR

t = (sqrt(x) for x in range(10))


def nad50(s):
    for e in s:
        if e > 50:
            return e
