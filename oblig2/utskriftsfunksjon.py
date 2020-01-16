"""
Program​met ​skal​ ​kommunisere ​med​ ​brukeren​ ​slik​ ​at​ ​det​ ​tar​ ​inn​ ​et​ ​navn​ ​og​ ​
et bosted​ fra​ ​terminalen tre ganger. Først lager jeg en prosedyre der
brukeren kan skrive inn navn og bosted. Dermed Kaller programmet på
prosedyren tre ganger så man kan skrive inn til sammen tre navn og tre
bosted.
"""
#Definerer prosedyren.
def minProsedyre():
    navn = input("Skriv inn navn: ")

    bosted = input("Hvor kommer du fra? ")

    print("Hei,", navn + "!", "Du er fra", bosted + ".")

#Kaller på prosedyren 3 ganger.
minProsedyre()
minProsedyre()
minProsedyre()
