from bud import Bud
class Annonse:
    def __init__(self, annTekst):
        self._annTekst = annTekst
        self._bud = []


    def hentTekst(self):
        return self._annTekst


    def giBud(self, hvem, belop):
        self._bud.append(Bud(hvem, belop))


    def antBud(self):
        return len(self._bud)


    def hoyesteBud(self):
        størst = self._bud[0].hentBudStr()
        for e in self._bud:
            e = e.hentBudStr()
            if e > størst:
                størst = e
        return størst


    def kraftBud(self, hvem, belop, maks):
        for e in self._bud:
            e = e.hentBudStr()
            if belop > e:
                b = Bud(hvem, belop)
            elif belop == e:
                belop += 1
                if belop <= maks:
                    b = Bud(hvem, belop)
            elif belop < e:
                belop = e + 1
                b = Bud(hvem, belop)
        self._bud.append(b)
