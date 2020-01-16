
from celle import Celle
from random import randint

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generasjonsnummer = -1
        self.lagBrett()


    def lagBrett(self):
        for r in range(self._rader):
            #Oppretter en liste for hver rad.
            liste = []
            for k in range(self._kolonner):
                #Legger til celler i hver rute i rutenettet.
                celler = Celle()
                liste.append(celler)
            self._rutenett.append(liste)


    def tegnBrett(self):
        #går igjennom hele rutenettet og printer ut alle celler.
        for rad in self._rutenett:
            for e in rad:
                print(e.hentStatusTegn(), end="t")
            print("t")



    def generer(self) :
        #ferdiglaget
        for i in range(self._rader):
            for j in range(self._kolonner):
                rand = randint(0, 1)
                if rand == 1:
                    self._rutenett[i][j].settLevende()




    def oppdatering(self):
        #Generasjonnummer legger på en for hver oppdatering.
        self._generasjonsnummer += 1
        #oppretter to lister.
        tilLevende = []
        tilDoede = []
        #Ser på hver enkelt celle.
        for i in range(self._rader):
            for j in range(self._kolonner):
                antallLevende = 0
                enkeltCelle = self._rutenett[i][j]
                statusCelle = enkeltCelle.erLevende()
                naboliste = self.finnNabo(j, i)
                #Ser etter hvor mange som lever av naboer til enkeltcellene.
                for e in naboliste:
                    if e.erLevende() == True:
                        antallLevende += 1
                #Regler med if-setninger.
                if statusCelle == True:
                    if antallLevende < 2 or antallLevende > 3:
                        tilDoede.append(enkeltCelle)
                else:
                    if antallLevende == 3:
                        tilLevende.append(enkeltCelle)
        #Går igjennom de listene med celler som skal leve/dø.
        for e in tilLevende:
            e.settLevende()
        for e in tilDoede:
            e.settDoed()
        #Returnerer generasjonnummer.
        return self._generasjonsnummer


    def finnAntallLevende(self):
        #Oppretter en teller og går gjennom hele rutenettet. Dersom cellen er
        #levende legger teller på 1. Returnerer teller for å bruke i main.
        teller = 0
        for rad in self._rutenett:
            for e in rad:
                if e.erLevende():
                    teller += 1
        return teller


    def finnNabo(self, x, y):
        #ferdiglaget.
        naboliste = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                naboX = x + i
                naboY = y + j
                if (naboX == x and naboY == y) != True:
                    if (naboX < 0 or naboY < 0 or naboX > self._kolonner-1 or naboY > self._rader-1) != True:
                        naboliste.append(self._rutenett[naboY][naboX])
        return naboliste
