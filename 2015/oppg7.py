class Attraksjon:
    def __init__(self, navn, barn, fra, til):
        self._navn = navn
        self._barn = barn
        self._fra = fra
        self._til = til

    def skrivAttr(self):
        print("navn: " + self._navn +
        ". Egnet for barn: " + self._barn + ". Aapen fra " + str(self._fra) +
        " til " + str(self._til) + ".")

    def forBarn(self):
        return self._barn;

    def aapenIPeriode(self, fra, til):
        if fra < self._til and til > self._fra:
            return True
        return False


class Destinasjon:
    def __init__(self, navn, list):
        self._navn = navn
        self._attrList = list

    def hentDestNavn(self):
        print("Navn: " + self._navn)
        for attraksjon in self._attrList:
            attraksjon.skrivAttr()
            print()

    def leggTilAttr(self, nyAttr):
        self._attrList.append(nyAttr)

    def antallAktuelleAttr(self, barn, fra, til):
        counter = 0
        if(barn):
            for attraksjon in self._attrList:
                if(attraksjon.aapenIPeriode(fra, til) and attraksjon.forBarn()):
                    counter+=1
        else:
            for attraksjon in self._attrList:
                if(attraksjon.aapenIPeriode(fra, til)):
                    counter+=1
        return counter


class Katalog:
    def __init__(self, katalogfil):
        self._katalogfil = katalogfil
        self._destKatalog = {}
        self._lesDestinasjonsfil(self._katalogfil)

        #Skal ikke skrives. Leser inn i _destKatalog.
    def _lesDestinasjonsfil(self, filnavn):
        pass

    def skrivDestListe(self):
        print("Alle destinasjoner:")
        for navn, destinasjon in self._destKatalog:
            print(navn)

    def skrivEnDest(self, destNavn):
        for navn, destinasjon in self._destKatalog:
            if navn == destNavn:
                destinasjon.hentDestNavn()

    def nyAttr(self, destNavn, attrNavn, bVennlig, aapenFra, aapenTil):
        for navn, destinasjon in self._destKatalog:
            if navn = destNavn:
                destinasjon.leggTilAttr(Attraksjon(attrNavn, bVennlig,
                aapenFra, aapenTil))
        return

    def nyDestFraFil(self, destNavn, filnavn):
        fil = open(filnavn)
        nyAttrList = []
        count = 0
        for line in fil:
            if count == 0:
                navn = line
                count+=1
            elif count == 1
                barn = False
                if line == "BARN":
                    barn = True
                count+=1
            elif count == 2
                fra = line
                count+=1
            elif count == 3
                til = line
                count+=1
                nyAttrList.append(Attraksjon(navn, barn, fra, til))
            else:
                count == 0;
        if destNavn not in self._katalogfil:
            self._katalogfil[destnavn] = nyAttrList
            return
        for attraksjon in nyAttrList:
            self._katalogfil.get(destNavn).append(attraksjon)


    def finnBesteDest(self, barn, fra, til):
        besteDest = ""
        besteAntall = 0
        for destNavn in self._destKatalog:
        dest = self._destKatalog[destNavn]
        antall = dest.antallAktuelleAttr(barn, fra, til)
        if antall > besteAntall:
        besteDest = destNavn
        besteAntall = antall
        return besteDest
