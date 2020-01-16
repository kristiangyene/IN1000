
a = "5"
b = "5"
print(a + b)

a = "5"
b = "5"
print(int(a)+int(b))
---
innlest = input("skriv et tall: ")
tall = int(innlest)
print(tall*2)
---
tall = 4 + (3 * 2)
tall = tall - 1
print(tall)
---
Fart = int(input())
if fart <= 60:
    svar: "fart: " + str(fart)
else:
    svar: "fart: over 60"
---
svar = input(input("spørsmål: "))
print("Du svarte: " + svar)
---

tall1 = int(input("skriv tall 1: "))
tall2 = int(input("skriv tall 2: "))

if tall1<tall2:
    minst = tall1
else:
    minst = tall2

print(minst)
---


alder = int(input("Hvor gammel er du? Svar: "))
if alder<3:
    print("lek i lekegrinda")
else:
    print("lek i skogen")
