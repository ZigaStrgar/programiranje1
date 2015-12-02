def fibo(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibo():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


for i, e in enumerate(fibo()):
    if e % 112 == 0:
        print(i, e)
        break


def tri():
    yield 1
    print("A spet?")
    yield 2
    print("Ta bo zadnja!")
    yield 3


g = tri()
print(tri())

# print(fibo(100))
