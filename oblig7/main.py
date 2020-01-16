"""I hovedprosedyra spoer jeg brukeren om dimensjoner. Her bruker jeg split og
legger de to verdiene i Spillebrett. generer() har jeg lagt utenfor while-loopen
for den skal kun brukes en gang på starten for å få noen random levende celler.
 I while-loopen har jeg det som trengs for å skrive ut brettet og oppdatere det.
 generasjonnummer og antallLevende er også der. """

import time
from spillebrett import Spillebrett

def main():
    storrelse = input("Skriv inn dimensjoner du ønsker(eks.30x40):\n>")
    a, b = storrelse.split("x")
    brett = Spillebrett(int(a), int(b))
    brett.generer()
    inp = ""
    while inp != "q":
        for e in range(100):
            print()
        brett.tegnBrett()
        antallLevende = brett.finnAntallLevende()
        genNr = brett.oppdatering()
        #print("Dette er generasjon:", genNr)
        #print("Antall levende celler:", antallLevende)
        #print("""Trykk enter for neste generasjon.
#Trykk q for å avslutte.""")
        #inp = input(">")
        time.sleep(0.1)




main()
