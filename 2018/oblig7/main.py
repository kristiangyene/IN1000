from spillebrett import Spillebrett
def main():
    storrelse = input("Skriv inn dimensjoner du ønsker(eks.30x40):\n>")
    a, b = storrelse.split("x")
    brett = Spillebrett(int(a), int(b))
    brett.generer()
    inp = ""
    while inp != "q":
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
