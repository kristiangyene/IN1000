"""
Programmet skal la brukeren skrive inn tall helt til brukeren skriver "0" og
legger det i en liste. Alle elemter blir skrevet ut hver for seg. Summen av
tallene, det største tallet, og det minste blir også skrevet ut ved hjelp av
for-løkker.
"""

liste = []

tall = 1
while tall != 0:
    tall = int(input("Skriv inn tall:\n>"))
    if tall == 0:
        break
    liste.append(tall)

for e in liste:
    print("Tall i liste:", e)

minSum = 0
if tall == 0:
    for e in liste:
        minSum += e
    print("Summen i listen:", minSum)

minst = liste[0]
for e in liste:
    if e < minst:
        minst = e
print("Det minste tallet i listen er:", minst)

størst = liste[0]
for e in liste:
    if e > størst:
        størst = e
print("Det største tallet i listen er:", størst)

print("Programmet avsluttes")
