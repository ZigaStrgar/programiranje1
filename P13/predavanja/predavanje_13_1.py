class Oseba:
    def __init__(self, ime, spol):
        self.ime = ime
        self.spol = spol

    def pozdravi(self):
        print("Pozdravljeni, jaz sem {} in sem {}".format(self.ime, self.naziv()))

    def naziv(self):
        return "gospod" if self.spol == "M" else "gospa"


class Student(Oseba):
    def __init__(self, ime, spol):
        super().__init__(ime, spol)
        self.ocene = {}

    def naziv(self):
        return "študentka" if self.spol == "Ž" else "študent"

    def prejmi_oceno(self, predmet, ocena):
        self.ocene[predmet] = ocena


class Ucitelj(Oseba):
    def __init__(self, ime, spol, title):
        super().__init__(ime, spol)
        self.title = title

    def naziv(self):
        return self.title


class Snazilka(Oseba):
    def __init__(self, ime):
        super().__init__(ime, 'Ž')


class Hisnik(Oseba):
    def __init__(self, ime):
        super().__init__(ime, 'M')


class Vratar(Oseba):
    def __init__(self, ime, spol):
        super().__init__(ime, spol)


ben = Oseba('Benjamin', 'M')
cil = Student('Cilka', 'Ž')
dani = Ucitelj('Dani', 'M', 'Docent')
eva = Student('Eva', 'Ž')
franci = Student('Franci', 'M')
greta = Student('Greta', 'Ž')
fata = Snazilka('Fata')
andrej = Hisnik('Andrej')
elvis = Vratar('Elvis', 'M')

studenti = [cil, eva, franci, greta, dani, fata, andrej, elvis]

for student in studenti:
    student.pozdravi()
