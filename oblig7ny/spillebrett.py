from random import randint
from celle import Celle
class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generasjonsnummer = 0
        for rad in range(self._rader):
            liste = []
            for kolonne in range(self._kolonner):
                celle = Celle()
                liste.append(celle)
            self._rutenett.append(liste)
        self.generer()
        self.tegnBrett()




    def tegnBrett(self):
        for rad in self._rutenett:
            for celle in rad:
                print(celle.hentStatusTegn(), end="")
            print("")


    def oppdatering(self):
        pass


    def finnAntallLevende(self):
        pass


    def generer(self):
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                if randint(0,2) == 0:
                    self._rutenett[rad][kolonne].settLevende()


    def finnNabo(self, x, y):
        pass
