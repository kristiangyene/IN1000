 """
 ​program​met skal ​ta ​inn​ ​data​ ​fra​ en ​fil​ ​og​ ​skrive ​ut​ ​statistikk​ ​for et​
 telefonsalg-firma. Navnene og verdien blir satt inn i en ordbok.
 maanedensSalgsperson finner den største verdien i ordboka slik
 at man finner den personen som har solgt mest denne maaneden.
 totaltAntallSalg tar alle verdiene og legger de sammen og gjennomsnittSalg
 tar gjennomsnittet av summen.
 Hovedprogrammet leser inn filen og kjører alle funksjoner og printer
 ut alle return-verdiene + kjører prosedyren maanedensSalgsperson.
 """
ordbok = {}
def innlesing(filnavn):
    fil = open(filnavn)
    for linjer in fil:
        biter = linjer.split()
        navn = biter[0]
        salg = int(biter[1])
        ordbok[navn] = salg
    return ordbok




def maanedensSalgsperson():
    størst = max(ordbok, key=lambda k: ordbok[k])

    print("Maanedens ansatte er", størst, "med", ordbok[størst], "salg.")


def totaltAntallSalg(dictionary):
    summen = sum(ordbok.values())
    return summen

def gjennomsnittSalg(gjennomsnitt):
    snitt = totaltAntallSalg(ordbok)/8
    return snitt

def hovedprogram():
    innlesing("salgstall.txt")
    maanedensSalgsperson()
    print()
    selgere = int(len(ordbok))
    print("aktive selgere denne måneden:", selgere)


    print("Summen av antall salg:",totaltAntallSalg(ordbok))
    print("Gjennomsnittet av salgene:", gjennomsnittSalg(ordbok))

hovedprogram()
