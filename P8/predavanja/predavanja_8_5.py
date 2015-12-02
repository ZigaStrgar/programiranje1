from math import sqrt


def delitelji(n):
    return [x for x in range(1, n) if n % x == 0]


def delitelji(n):
    return ([x for x in range(1, n) if n % x == 0])  # Dobim generator


def delitelji(n):
    for i in range(1, n):
        if n % i == 0:
            yield i


# Finta
def deliteji(n):
    ostali = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            yield i
            if i ** 2 != n:
                ostali.append(n // i)
    for i in reversed(ostali):
        yield i


def popolno(n):
    return n == sum(delitelji(n))
