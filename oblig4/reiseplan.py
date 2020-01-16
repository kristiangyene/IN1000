"""
Programmet skal la brukeren fylle tre lister med fem strenger. Disse listene
skal settes inn i en ny liste, reiseplan. Så skal det være mulig for brukeren
å finne et element i listen ved å skrive inn indeks.
"""


steder = []
for e in range(5):
    steder.append(input("skriv inn reisemål:\n>"))


klesplagg = []
for e in range(5):
    klesplagg.append(input("skriv inn klesplagg:\n>"))


avreisedatoer = []
for e in range(5):
    avreisedatoer.append(input("skriv inn avreisedatoer:\n>"))

#Legger alle listene i én liste.
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)

print(reiseplan)

for e in reiseplan:
    print("liste:", e)

#Lar brukeren finne element.
s1 = int(input("Skriv inn hvilken liste du ønsker(0-2):\n>"))
s2 = int(input("Skriv inn plassering i listen(0-4):\n>"))
i1 = reiseplan[s1]
i2 = i1[s2]
if s1 < 3 and s2 < 5 and s1 > -1 and s2 > -1:
    print(i2)
else:
    print("Ugyldig input!")
