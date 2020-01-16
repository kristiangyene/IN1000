"""
I programmet skal funksjonen addisjon returnere summen av 2 heltall som jeg
har valgt å sette tall1 = 2 og tall2 = 1 og printe svaret. Deretter gjør den
det samme bare med substraksjon og divisjon, bare nå har jeg satt inn assert
for å sjekke om det fungerer, og om jeg får det svaret jeg forventer. Så lager
jeg en funksjon som sjekker om antallTommer er høyere enn 0 og gange det med
2.54 for å få det i cm. Så kaller jeg på det for å sjekke om det fungerer.
Deretter skal bruker skrive inn 2 tall(flyttall mulig) og bruke de som
parametere i de forrige funksjonene. Printer ut resultatene. Ny brukerinput
der tallet blir omgjort fra tommer til cm.
"""

def addisjon(tall1, tall2):
    return tall1 + tall2

svar = addisjon(2, 1)
print("Summen av 2 og 1 er:", svar)

def substraksjon(tall1, tall2):
    return tall1 - tall2

svar = substraksjon(2, 1)
assert substraksjon(2, 1) == 1
assert substraksjon(-2, -1) == -1
assert substraksjon(-2, 1) == -3

def divisjon(tall1, tall2):
    return tall1 / tall2

assert divisjon(2, 1) == 2
assert divisjon(-2, -1) == 2
assert divisjon(-2, 1) == -2

def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54
print("Fra 32cm til tommer:", tommerTilCm(32))

def skrivBeregninger():
    inp1 = float(input("Skriv inn tall 1:\n>"))
    inp2 = float(input("Skriv inn tall 2:\n>"))
    svar1 = addisjon(inp1, inp2)
    svar2 = substraksjon(inp1,inp2)
    svar3 = divisjon(inp1, inp2)
    print("Resultatet av summering:", svar1)
    print("Resultatet av substrakjonen:", svar2)
    print("Resultatet av divisjonen:", svar3)
    print("Konvertering fra tommer til cm:")
    inp3 = float(input("Skriv inn tall:\n>"))
    iCm = inp3 * 2.54
    print("Resultat = ", iCm)

skrivBeregninger()
