
import requests     # ermöglicht HTTP requests einfach zu senden
                    # ohne dass man query strings zur url hinzufügen muss
                    # form-encode POST data fällt auch weg

import json
'''
catfacts = requests.get('https://blibla')
data_cat = catfacts.json()
'''
bored = requests.get('https://www.xyz')
data_bored = bored.json()
print(json.dumps(data_bored, indent=4))

print(data_bored)
print(type(bored))
print(type(data_bored))

# for key, value in data_bored.items():             # alternative Ausgabe
  #   print(key, ' : ', value)

# print(json.dumps(catfacts, indent=4))              # geht so nicht






