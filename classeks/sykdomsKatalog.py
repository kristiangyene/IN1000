from sykdom import Sykdom

class SykdomsKatalog:
    def __init__(self, filnavn):
        self._sykdommer = {}
        self._lesFil(filnavn)

    def sjekkMutasjon(self, posisjon):
        for sykdomsnavn in self._sykdommer:
            sykdom = self._sykdommer[sykdomsnavn]
            sykdom.erAssosiert(posisjon)

    def skrivSykdomsTreff(self):
        for sykdomsnavn in self._sykdommer:
            sykdom = self._sykdommer[sykdomsnavn]
            print(sykdomsnavn, ":",sykdom.hentAntallTreff())

    def _lesFil(self, filnavn):
        fil = open(filnavn)
        for line in fil:
            biter = line.split(',')
            posisjon = int(biter[0])
            sykdomsnavn = biter[1].strip()
            if sykdomsnavn in self._sykdommer:
                sykdom = self._sykdommer[sykdomsnavn]
            else:
                sykdom = Sykdom(sykdomsnavn)
                self._sykdommer[sykdomsnavn] = sykdom
            sykdom.leggTilPosisjon(posisjon)

k = SykdomsKatalog()
