"""Legger inn noderPerRack og en tok liste i konstruktoeren der jeg kan holde
styr på racks i RegneKlynge. Metoden settInnNode skal opprette et rack til aa
begynne med dersom antall racks er 0. Saa legger den inn en node i racket dersom
det er plass. Om ikke skal et nytt rack opprettes og noden skal legges inn der.
antProsessorer gaar igjennom alle racks og kaller paa en metode fra Rack. den
legger alle verdiene i en liste og summeren listen. Bruker samme maate paa
metoden noderMedNokMinne og antRacks, bare at i antRacks saa tar jeg lengden av
listen."""

from rack import Rack

class RegneKlynge:
	#Oppretter tom regneklynge for racks med oppgitt maxtall noder/ rack.
    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._racks = []


	#Plasserer en node inn i et rack med ledig plass, eller i et nytt.
    def settInnNode(self, node):
        if len(self._racks) == 0:
            self._racks.append(Rack())
        for e in self._racks:
            if e.getAntNoder() < self._noderPerRack:
                e.settInn(node)
            elif self._racks[-1].getAntNoder() == self._noderPerRack:
                self._racks.append(Rack())


    #Beregner totalt antall prosessorer i hele regneklyngen.
    def antProsessorer(self):
        totalt = []
        for e in self._racks:
            s = e.antProsessorer()
            totalt.append(s)
        return sum(totalt)


    #Beregner antall noder i regneklyngen med minne over angitt grense.
    def noderMedNokMinne(self, paakrevdMinne):
        liste = []
        for e in self._racks:
            liste.append(e.noderMedNokMinne(paakrevdMinne))
        return sum(liste)


    #Henter antall racks i regneklyngen.
    def antRacks(self):
        liste = []
        for e in self._racks:
            liste.append(e)
        return len(liste)
