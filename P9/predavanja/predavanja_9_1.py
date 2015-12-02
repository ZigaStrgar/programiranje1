t = [1, 2, 3]
u = [1, 2, 3]
v = [1, 2, 3]

t is v
e = []
t = [e]
t[0] is e  # True
t[0].append(2)  # Spremeni e

e = [1, 2, 3]  # T ostane [[1, 2]], e dobi nov objekt

t = ["Ana"] + ["Ana"] + ["Ana"]  # Ustvari 3 objekte "Ana"
print(t)
t = ["Ana"] * 3  # Ustvari objekt, ki 3x kaže na en objekt
print(t)

e = []
t = [e] * 3
e.append(1)
print(t)
