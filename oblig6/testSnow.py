"""
Programmet skal være en oversikt over triks man kan som en snowboarder.
Skriv en klasse Snowboarder med en konstruktør som tar imot navn og alder.
Konstruktøren skal også ha en tom liste 'triks'. Skriv en metode 'leggTilTriks'
som tar imot en tekststreng og legger den til i triks-listen. Skriv en metode
'slettTriks' som tar imot en tekstreng som fjernes fra listen. skriv en metode
 som skriver ut navn og alder. Når brukeren har skrevet inn triks, skal
 programmet skrive ut navn, alder og listen med triks.
"""

from snow import Snowboarder

def hovedprogram():
    inp1 = input("Skriv inn ditt navn:\n>")
    inp2 = int(input("Skriv inn din alder:\n>"))
    snow = Snowboarder(inp1, inp2)
    print("Tast 'enter' når du er ferdig")
    inp3 = input("Skriv inn triks du kan:\n>")
    while inp3 != "":
        snow.leggTilTriks(inp3)
        inp3 = input(">")

    snow.skrivUt()
    print(snow.triks)

    inp4 = input("""ønsker du å legge til fler eller slette?
    For å legge til: tast l
    For å slette: tast s\n>""")
    if inp4 == "l":
        print("Tast 'enter' når du er ferdig")
        inp3 = input("Skriv inn triks du kan:\n>")
        while inp3 != "":
            snow.leggTilTriks(inp3)
            inp3 = input(">")
    elif inp4 == "s":
        print("Tast 'enter' når du er ferdig")
        inp3 = input("Skriv inn triks du vil slette:\n>")
        while inp3 != "":
            snow.slettTriks(inp3)
            inp3 = input(">")

    snow.skrivUt()
    print(snow.triks)


hovedprogram()
