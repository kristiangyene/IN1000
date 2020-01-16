class Gave:
    def __init__(self, navn, pris):
        self._gaveNavn = navn
        self._gavePris = int(pris)

    def retPris(self):
        return self._gavePris

    def retNavn(self):
        return self._gaveNavn

    def __str__(self):
        return self._gaveNavn + " koster " + str(self._gavePris) + "kr"
