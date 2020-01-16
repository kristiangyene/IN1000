"""
Dette er ikke en lovlig kode fordi vi kan ikke legge sammen integer og
string. For å kunne få det ønsket svaret, må man gjøre om b til en string på
denne måten: str(b), slik at vi får inn teksten 10.
Et annet problem i programmet er at om man taster inn et tall >= 10 så kommer
det ikke ut noe svar, dermed vil det være lurt å ha en else i tillegg.
"""
#Løsning til å få programmet til å kjøre.
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(str(b) + "Hei!")
