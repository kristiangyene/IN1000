"""Oppretter en liste i konstruktoeren. Metoden settInn skal sette inn en node
i ett rack. Metoden getAntNoder skal finne ut hvor mange noder det er i racket.
Metoden antProsessorer legger hvert antall prosessorer til en node i racket i
en liste og summeren listen. noderMedNokMinne teller hvor mange noder som har
stoerre eller likt antall paakrevd minne."""

from node import Node

class Rack:
	#Oppretter et rack der det senere kan plasseres noder.
    def __init__(self):
        self._rack = []


	#Plasserer en ny node inn i racket med .append().
    def settInn(self, node):
        self._rack.append(node)


	#Henter antall noder i racket.
    def getAntNoder(self):
        return len(self._rack)


	#Beregner sammenlagt antall prosessorer i nodene i et rack.
    #bruk heller teller
    def antProsessorer(self):
        antall = []
        for e in self._rack:
            f = e.antProsessorer()
            antall.append(f)
        return sum(antall)


    #Beregner antall noder i racket med minne over gitt grense.
    def noderMedNokMinne(self, paakrevdMinne):
        noderNok = 0
        for e in self._rack:
            if e.nokMinne(paakrevdMinne) == True:
                noderNok += 1
        return noderNok
