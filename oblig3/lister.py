"""
Programmet skal skrive ut 1. og 3. element fra en liste jeg har
 laget selv.
"""
#Setter inn random verdier i listen og utvider med et til.
minListe = [7, 12, 4]
minListe.append(32)

#Printer ut verdiene.
element1 = print("1. element er", minListe[0])
element2 = print("3. element er", minListe[2])


navnListe = []
print("Skriv inn fire navn du ønsker i listen.")
print()
navn1 = input("1. navn:\n>")
navnListe.append(navn1)
navn1.lower
print()
navn2 = input("2. navn:\n>")
navnListe.append(navn2)
navn2.lower
print()
navn3 = input("3. navn:\n>")
navnListe.append(navn3)
navn3.lower
print()
navn4 = input("4. navn:\n>")
navnListe.append(navn4)
navn4.lower
print()
print(navnListe)
if navn1 == "kristian" or navn2 == "kristian" or navn3 == "kristian" or navn4 == "kristian":
    print("Du husket meg!")
else:
    print("Glemte du meg?")


nyListe = minListe + navnListe
nyListe.pop(-1)
nyListe.pop(-1)

print(nyListe)
