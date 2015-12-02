def delitelji(n):
    return [x for x in range(1, n) if n % x == 0]


def popolno(n):
    return n == sum(delitelji(n))


def vsa_popolna(n):
    return [i for i in range(1, n) if popolno(i)]


def prastevilo(n):
    return delitelji(n) == [1]


def vsa_prastevila(n):
    return [i for i in range(1, n) if prastevilo(i)]


print(delitelji(28))
