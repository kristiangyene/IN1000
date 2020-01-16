from sykdomsKatalog import SykdomsKatalog

class Pasient:
    def __init__(self, filnavn):
        self._mutasjoner = []
        self._lesFil(filnavn)

    def alleMutasjoner(self):
        return self._mutasjoner

    def _lesFil(self, filnavn):
        fil = open(filnavn)
        for linje in fil:
            posisjon = int(linje)
            self._mutasjoner.append(posisjon)
