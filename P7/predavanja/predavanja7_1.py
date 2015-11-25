# f = float(input("Vpiši temperaturo v Fahrenheitih: "))
f = 52
c = (f-32) * 5/9

podatki = [
    (74, "Anže", False),
    (82, "Benjamin", False),
    (58, "Cilka", True),
    (66, "Dani", False),
    (61, "Eva", True),
    (101, "Franci", False),
]

for teza, ime, spol in podatki:
    print("{i:_<10}{t:_>3}".format(i=ime, t=teza))

s = "{foo:5.2f} Fahrenheitov je {bar:5.2f} Celzijev".format(foo=f, bar=c)

print(s)
