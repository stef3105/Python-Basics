def Add(self, a, b):
    return a + b

class Baum:
    def __init__(self, n, a, h):
        self.name = n
        self.alter = a
        self.hoehe = h

    def __index__(self, n, p): #überladen geht wohl nicht in python
        self.name = n
        self.preis = p

    def wachsen(self):
        print("Der Baum wächst.")

    def show(self):
        print("{0} ist {1} Jahre alt und {2} Meter hoch.".format(self.name, self.alter, self.hoehe))
        # print(f"{self.name} ist {self.alter} Jahre alt und {self.hoehe} Meter hoch.")

baum1 = Baum("Eiche", 25, 12)
print(baum1.name)
baum1.name = "Eiche_neu"
print(baum1.name)
baum1.show()

baum2 = Baum("Ahorn", 4, 2.5)
baum2.show()

baum1.wachsen()

baum3 = Baum(1, 2, 3)
baum3.show()






