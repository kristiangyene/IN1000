from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._genNr = -1
        self.tegnBrett()



    def lagBrett(self):
        for rad in range(self._rader):
            liste = []
            for kolonne in range(self._rader):
                liste.append(Celle())
            self._rutenett.append(liste)



    def tegnbrett(self):
        for rad in self._rutenett:
            for celle in rad:
                print(celle.hentStatusTegn(), end="")
            print("")



    def oppdatering(self):
        self._genNr += 1
        doede = []
        levende = []
        for rad in range(self._rader):
            for kolonne in range(self.kolonner):
                antLevende = 0
                celle = self._rutenett[rad][kolonne]
                celleStat = celle.erLevende()
                naboer = celle.finnNabo(rad, kolonne)
                for nabo in naboer:
                    if nabo.erLevende():
                        antLevende += 1
                if celleStat:
                    if antLevende < 2 or antLevende > 3:
                        doede.append(celle)
                else:
                    if antLevende == 3:
                        levende.append(celle)
        for e in doede:
            e.settDoed()
        for f in levende:
            f.settLevende()
        return self._genNr



    def finnAntallLevende(self):
        antLevende = 0
        for rad in self._rutenett:
            for celle in rad:
                if celle.erLevende():
                    antLevende += 1
        return antLevende



    def generer(self):
        for i in range (self._rader):
            for j in range (self._kolonner):
                rand = randint(0,3)
                if rand == 3 :
                    self._rutenett[i][j].settLevende()



    def finnNabo (self, rad, kolonne):
        naboliste = []
        for i in range (-1, 2):
            for j in range (-1, 2):
                naboRad = rad+i
                naboKolonne = kolonne+j
                if (naboRad == rad and naboKolonne == kolonne) != True :
                    if (naboRad < 0 or naboKolonne < 0 or naboRad > self._rader-1
                    or naboKolonne > self._kolonner-1) != True:
                        naboliste.append(self._rutenett[naboRad][naboKolonne])
        return naboliste
