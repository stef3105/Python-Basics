
liste = ["baum", "Maus", "Mütze", "Angel", "Brille"]
x = 0
while x < 4:                                #"Gatekeeper"
    print(x, "oberhalb der for-Schleife")   # Nur zum Testen
    for i in liste:         # Alle Elemente der Liste sind gemeint
        print(i, "loop", x)
    x += 1                  # x = 1
                            # Danach zum Anfang der while-Schleife zurück
                            # x = 2
                            # Alle Elemente der Liste werden ausgegeben
                            # Wieder zu while zurück
                            # usw bis x = 3
                            # Insgesamt 4 Loops 0,1,2,3
print("Ende von While-Schleife 1 --- \n")

liste = ["baum", "Maus", "Mütze", "Angel", "Brille"]
x = 0
while x < 4:    # da x erst nach dem "Gatekeeper" erhöht wird,
    x += 1      # gibt es noch eine Ausgabe loop 4 obwohl 4 nicht kleiner ist als 4
    print(x, "oberhalb der for-Schleife")
    for i in liste:
        print(i, "loop", x)






