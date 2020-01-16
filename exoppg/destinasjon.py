class Destinasjon:
    def __init__(self, navn, arrayList):
        self._navn = navn
        self._attraksjoner = arrayList

    def hentDestNavn(self):
        return self._navn

    def skrivDest(self):
        print("Attraksjoner:")
        for e in self._attraksjoner:
            print(e)

    def leggTilAttr(self, nyAttr):
        self._attraksjoner.append(nyAttr)

    def antallAktuelleAttr(self, barn, fra, til):
        
