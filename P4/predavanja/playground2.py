def delitelji(stevilo):
    d = []
    for i in range(1, stevilo):
        if stevilo % i == 0:
            d.append(i)
    return d


def vsota(seznam):
    v = 0
    for stevilka in seznam:
        v += stevilka
    return v


def popolno(stev):
    return stev == vsota(delitelji(stev))


def vsa_popolna(n):
    s = []
    for i in range(1, n + 1):
        if popolno(i):
            s.append(i)
    return s


def prastevilo(n):
    return len(delitelji(n)) == 1


def vsa_prastevila(n):
    s = []
    for i in range(1, n + 1):
        if prastevilo(i):
            s.append(i)
    return s

print(vsa_prastevila(100))


