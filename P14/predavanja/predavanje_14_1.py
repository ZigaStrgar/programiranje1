class Vector(list):
    def __init__(self, *v):
        super().__init__(v)

    def __abs__(self):
        from math import sqrt
        return sqrt(sum(x ** 2 for x in self))

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Mismatching vetor lenghts ({} != {})".format(len(self), len(other)))
        return Vector(*[x + y for x, y in zip(self, other)])

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return Vector(*[other * x for x in self])

    # __rmul__ = __mul__

    def __rmul__(self, other):
        return self.__mul__(other)

    def __neg__(self):
        return Vector(*[-x for x in self])


a = Vector(1, 3, 5)
b = Vector(1, 3)

print(a)
print(abs(a))
print(len(a))
print(a + b)
print(a * 3)
print(3 * a)
print(a - b)
print(-a)
print(a[0], a[1], a[2])
