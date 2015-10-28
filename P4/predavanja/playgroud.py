from math import sqrt


def ploscina(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


def obseg(a, b, c):
    return a + b + c


def ploscina_kv(x):
    return x ** 2


print(ploscina(5, 12, 13))
