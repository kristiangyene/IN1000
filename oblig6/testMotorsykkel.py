"""
Programmet skal importere classen Motorsykkel der objektet ​motorsykkel har​ ​et​
​merke, et​ ​registreringsnummer​ ​og​ ​en​ ​kilometerstand​ ​som​ ​viser​ ​hvor​ ​langt​ ​den​
​har kjørt.
Legger inn tre forskjellige motorsykkelobjekter og skriver de ut ved å kalle
på 'skrivUt()' med alle tre. Den siste motorsykkelen legger jeg til 10km
ved hjelp av 'kjor()' og printer dette med 'hentKilometerstand' for å vise at
det har blitt lagt til.
"""
from motorsykkel import Motorsykkel

def hovedprogram():
    mot1 = Motorsykkel("A", "XX 12345", "10000")
    mot2 = Motorsykkel("B", "ZX 12345", "10000")
    mot3 = Motorsykkel("C", "ZZ 12345", "10000")

    mot1.skrivUt()
    mot2.skrivUt()
    mot3.skrivUt()
    mot3.kjor(10)
    print("Lagt på 10km på mot3:", mot3.hentKilometerstand())

hovedprogram()
