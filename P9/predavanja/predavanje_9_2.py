# Don't do it

t = [1, 2]
x = 42


def f():
    x = 12
    t.append(3)


f()
print(x, t)

