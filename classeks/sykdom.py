class Sykdom:
    def __init__(self, navn):
        self._navn = navn
        self._posisjoner = []
        self._antallTreff = 0

    def leggTilPosisjon(self, posisjon):
        self._posisjoner.append(posisjon)

    def erAssosiert(self, posisjon):
        if posisjon in self._posisjoner:
            self._antallTreff += 1

    def hentAntallTreff(self):
        return self._antallTreff
