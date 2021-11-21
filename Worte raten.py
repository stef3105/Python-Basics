# Worte raten

import random

wortliste = ['zimmer', 'bahnhof', 'kleiderschrank', 'regal', 'turnschuh', 'brötchen', 'kugelschreiber', 'taschenrechner',
         'handschuh', 'tiefkühlpizza', 'radiergummi', 'bildschirm', 'murmel', 'globus', 'brücke', 'müsliriegel']

# Wort wird zufällig generiert und in einzelnen Buchstaben in gesuchte_buchstaben gespeichert.
# Danach für eine schönere Ausgabe wieder durch join zusammengesetzt in loesung

gesuchtes_wort = random.choice(wortliste)
gesuchte_buchstaben = list(gesuchtes_wort)
loesung = "".join(gesuchte_buchstaben)
# print(loesung)
# print(gesuchte_buchstaben)

wort_erraten = False
bisher_erraten = []
falsche_tipps = []
alle_tipps = []
versuch = 0
anzahl_treffer = 0

while versuch < 7:
    treffer = False
    versuch += 1
    print("Versuch", versuch)
    user_eingabe = input("Bitte gib deinen Tipp ein! ende um abzubrechen")
    for element in range(len(gesuchte_buchstaben)):
        if user_eingabe == gesuchte_buchstaben[element]:
            bisher_erraten.append(user_eingabe)
            print("Treffer an der Stelle", element)
            treffer = True
            anzahl_treffer += 1

    if treffer == False:
        # print("loop", element)
        falsche_tipps.append(user_eingabe)
        # print(falsche_tipps)

    if anzahl_treffer == len(gesuchtes_wort):
        alle_tipps.append(user_eingabe)
        wort_erraten = True
        print("Glückwunsch! Du hast das Wort erraten!")
        print("Das gesuchte Wort ist: ", gesuchtes_wort)
        break

    if user_eingabe == "ende":
        print("Programm beendet.") # , element)
        break

    print("Bisher richtig:", bisher_erraten)
    alle_tipps.append(user_eingabe)
    # print("alle tipps", alle_tipps)
    print("Falsche Tipps", falsche_tipps)
    print("Anzahl Treffer", anzahl_treffer)
    # print("Ende von Versuch", versuch)
    print()

print("Alle Tipps:", alle_tipps)
print("Falsche Tipps:", falsche_tipps)
print("Treffer erzielt: ", anzahl_treffer)
print("Das gesuchte Wort war:", loesung)
print("Ende")

# Geplant sind noch Sachen wie die richtigen Treffer in der Form B_U_H_US auszugeben.
# Vllt auch noch eine graphische Overfläche.



