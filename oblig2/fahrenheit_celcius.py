"""
Programmet skal konvertere​ ​en​ ​temperatur​ ​fra​ ​fahrenheit​ gitt via
brukerinnput ​til​ celcius. Verdien brukeren skriver vil bli gjort
om til Celcius og lagt som en egen variabel. Så printes det ut.
Jeg også har brukt commandoen round() for å få to desimaler.
"""
#Brukerens input i egen variabel.
F = int(input("Skriv inn temperatur i ​fahrenheit:\n>"))

#Gjør om fahrenheit til celcius og skriver ut.
C = (F - 32) * 5/9
print("Temperatur i celcius:", str(round(C, 2)))
