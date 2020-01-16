"""
Programmet skal være et verktøy for en skredder. Det skal ta imot en fil der
kunden har oppgitt navnet på målet og mål i cm. Dette skal legges inn i en
ordbok. Deretter skal det gjøre om målet fra cm til tommer og legge disse
målene inn i en ny ordbok. Jeg har laget en lobby der man får Alternativer
hvor man enten kan vise mål i cm, vise mål i tommer, sette inn en ny fil, eller
avslutte programmet.
"""
#Lager en hovedprosedyre.
def main():
    import time
    ordbokCm = {}
    ordbokTommer = {}
    #definerer funksjonen som legger inn i ordbok og gjør om til tommer.
    def funk():
        fil = input("Skriv inn fil for beregning av mål:\n>")
        målFil = open(fil)
        for linjer in målFil:
            biter = linjer.split()
            navn = biter[0]
            lengdeCm = int(biter[1])
            lengdeTommer = int(biter[1]) * 2.54
            ordbokCm[navn] = lengdeCm
            ordbokTommer[navn] = lengdeTommer

    #Kjører funksjonen etter å ha kjørt hovedprosedyra.
    funk()

    #Definerer hovedsiden der bruker får velge hva programmet skal gjøre.
    def lobby():
        print("Alternativer:")
        valg = input("Se mål i cm: tast 1\
        \nSe mål i tommer: tast 2\
        \nVelge ny fil: tast 3\
        \nAvslutte programmet: tast 0\
        \n>")
        if valg == "1":
            print("Målene kunden har oppgitt i cm:\n", ordbokCm)
            time.sleep(2)
            lobby()
        elif valg == "2":
            print("Målene kunden har oppgitt i tommer:\n", ordbokTommer)
            time.sleep(2)
            lobby()
        elif valg == "3":
            main()
        elif valg == "0":
            print("Programmet avsluttes")
    #Kjører hovedsiden til slutt.
    lobby()
#Kjører hovedprosedyre til å starte med.
main()
