x = 0               #Erste Schritte in Python

while x < 3:
    x += 1
    print("Start Durchlauf Nr.", x)
    Eingabe_vom_User = input("Gib bitte irgendwas ein. 'ende' um abzubrechen. \n ")
    print(Eingabe_vom_User, ":Das ist der eingegebene Wert.\n")
    if Eingabe_vom_User == "ende":
        print("Programm durch Nutzereingabe beendet. Schönen Tag noch!")
        break

    else:
        try:
            Umwandlung1 = float(Eingabe_vom_User)
            print(Umwandlung1, ":Nach Umwandlung in Float.")
        except:
            print("Fehler: Eingabe lässt sich nicht in Float umwandeln.\n ")
        try:
            Umwandlung2 = tuple(Eingabe_vom_User)
            print(Umwandlung2, ":Nach Umwandlung in Tupel.")
        except ValueError as e:
            print(e)
        try:
            Umwandlung3 = bool(Eingabe_vom_User)
            print(Umwandlung3, ":Nach Umwandlung in Bool.")
        except ValueError as f:
            print(f)
        try:
            Umwandlung4 = list(Eingabe_vom_User)
            print(Umwandlung4, ":In Listenform.")
        except ValueError as g:
            print(g)
        try:
            t1 = Eingabe_vom_User
            t2 = t1
            Umwandlung5 = dict(zip(t1, t2))
            print(Umwandlung5, ":Als Dictionary.")
        except ValueError as h:
            print(h)
        finally:
            print("Hier steht der Finally-Teil.")
            print("Das war Durchlauf Nr.", x)
            print(" ")
if x == 3:
    print("Ende")
    print("Have a nice day!")
















