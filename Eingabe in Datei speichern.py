from datetime import datetime
import pytz

liste1 =[]

zz_Berlin = pytz.timezone('Europe/Berlin')
datum_BLN = datetime.now(zz_Berlin)
print("Berlin Uhrzeit:", datum_BLN.strftime("%H:%M:%S"))
datum_BLN2 = str(datum_BLN)
datum_BLN3 = datum_BLN2[:19]

liste1.append(datum_BLN3)

benutzer_eingabe = input("Wieviele Kaffees hast du getrunken?")
liste1.append(benutzer_eingabe)

leerzeile = "..."
liste1.append(leerzeile)

print(liste1," \n")

try:
    print(liste1[0], "Element 0")
    print(liste1[1], "Element 1")
    print(liste1[2], "Element 2")
    print(liste1[3], "Element 3")
except:
    print("Fehler")

textdatei = open("kaffe_datei.txt", "a")
for element in liste1:
    textdatei.write(element + "\n")
textdatei.close()






