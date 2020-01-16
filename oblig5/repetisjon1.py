"""
I programmet lager jeg en tom liste. Lager en funksjon som skal konkatenere
to strenger og returnerer resultatet. Lager en funksjon som skriver ut hvert
element i en liste. Deretter lager jeg en whileloop som kjører så lenge
brukerinput ikke er "s". Så lagde jeg en liten meny. Om bruker skriver "i",
vil programmet ta inn to inputs som legges inn som parameterei funksjonen som
slår sammen strenger og legger det i listen. Om bruker skriver "u" så går den
til funksjonen som skriver ut listen. Skriver brukeren "s" så avsluttes
programmet.

"""

mineOrd = []

def slaaSammen(str1, str2):
    sammen = str1 + str2
    return sammen


def skrivUt(liste):
    for e in liste:
        print("Element i liste:", e)

inp = 0
s = 0
while inp != "s":
    print("Hva ønsker du å gjøre?\
    \nFor å slå sammen to ord: tast i\
    \nFor å skrive ut ordene: tast u\
    \nFor å avslutte programmet: tast s")
    inp = input(">")
    if inp == "i":
        tekst1 = input("skriv inn tekst:\n>")
        tekst2 = input("skriv inn en annen tekst:\n>")
        ordet = slaaSammen(tekst1, tekst2)
        mineOrd.append(ordet)
    elif inp == "u":
        skrivUt(mineOrd)

print("Programmet avsluttes")
