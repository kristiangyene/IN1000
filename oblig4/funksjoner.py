"""
Programmet skal la brukeren skrive inn to heltall og returnere summen av de.
denne funksjonen blir kalt på to ganger. Så lar det brukeren skrive tekst og
en bokstav, og finner ut hvor mange ganger den bokstaven forekommer i teksten.
"""
def adder(tall1, tall2):
    summen = tall1 + tall2
    print("Summen av", str(tall1), "og", str(tall2), "er lik", str(summen))
    return summen
s1 = adder(int(input("skriv inn et heltall:\n>")), int(input("skriv inn et\
 annet heltall:\n>")))
s2 = adder(int(input("skriv inn et heltall:\n>")), int(input("skriv inn et\
 annet heltall:\n>")))

#Deloppgave 2
"""streng = input("Skriv et ord\n>")
bokstav = input("Skriv en bokstav:\n>​")
teller = 0
for e in streng:
    if bokstav == e:
        teller += 1
print("Antall ganger bokstaven forekommer i ordet:", teller)"""


def tellForekomst(minTekst, minBokstav):
    teller = 0
    for e in minTekst:
        if minBokstav == e:
            teller += 1
    return teller

funk = tellForekomst(input("Skriv et ord\n>"), input("Skriv en bokstav:\n>​"))
print("Antall ganger bokstaven forekommer i ordet:", funk)
