"""
Programmet skal la brukeren skrive inn varenavn og pris slik det
legges inn i en ordbok som allerede har noen verdier. Så printes
ordboken ut i terminalen.
"""
butikk = {"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}
print(butikk)

vare = input("Skriv inn vare:\n>")
vare.lower()
pris = int(input("Hvor mye koster det?\n>"))

vare2 = input("Skriv inn vare:\n>")
vare2.lower()
pris2 = int(input("Hvor mye koster det?\n>"))

butikk[vare] = pris
butikk[vare2] = pris2

print(butikk)
