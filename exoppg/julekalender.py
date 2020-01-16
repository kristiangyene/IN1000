from barn import Barn
class Julekalender:
    def __init__(self, barna, gavefil):
        self._familie = []
        for e in barna:
            barn = Barn(e)
            self._familie.append(barn)
        self._oversikt = []
        self._gavefil = open(gavefil)
        self._dag = 0
        self._teller = 0
        self._lesGavefil()






    def nyDag(self):
        if self._teller > len(self._familie) - 1:
            self._teller = 0
        barnTur = self._familie[self._teller]
        barnTur.apneGave(self._oversikt[self._dag][0],self._oversikt[self._dag][1])
        self._dag += 1
        self._teller += 1




    def gaveOversikt(self):
        for e in self._familie:
            e.skrivBarn()



    def _lesGavefil(self):
        for linje in self._gavefil:
            linje = linje.strip()
            liste = []
            a, b = linje.split(",")
            liste.append(a)
            liste.append(int(b))
            self._oversikt.append(liste)



    def _kalender(self):
        pass



    def _apnere(self):
        barnTur = self._familie[self._teller]
        return barnTur



    def _nesteapner(self):
        pass



    def _dag(self):
        nesteDag = self._dag + 1
        return nesteDag
