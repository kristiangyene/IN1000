"""
Programmet skal åpne en fil der det er lagt inn en del verdier for temperatur
hver mnd i et år. Bruker en for-løkke for å skrive ut hver enkelt temperatur.
Alle temperaturene legges inn i en liste som også skrives ut.
Så lager jeg en funksjon som legger sammen hver enkelt verdi og deler det på
antall måneder slik at jeg får en gjennomsnittstemperatur det året.
Gjennomsnittstemperaturen printes ut. 
"""

tempListe = []
print("Gjennomsnittstemperatur gjennom ett år pr. mnd:")
minFil = open("temperatur.txt")
mnd = 1
temp = 0
for temp in minFil:
    print("I", str(mnd) + "." + "mnd","er", str(temp))
    mnd += 1
    tempListe.append(int(temp))
print()
print("Liste med temperaturer:")
print(tempListe)


def gjennomsnitt(liste):
    teller = 0
    minSum = 0
    if teller != 12:
        for e in liste:
            minSum += e
            teller += 1
    return minSum / len(tempListe)


print("Gjennomsnittstempertatur i året:", gjennomsnitt(tempListe))
