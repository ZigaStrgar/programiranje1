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
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def obstaja_sodo(s):  # Ob praznem seznamu vrne False
    for e in s:
        if e % 2 == 0:
            return True
    return False


def vsa_prastevila(n):
    s = []
    for i in range(1, n + 1):
        if prastevilo(i):
            s.append(i)
    return s


def kvadrat_kub(x):
    return x ** 2, x ** 3

# x, y = kvadrat_kub(x)


print(vsa_prastevila(100))
