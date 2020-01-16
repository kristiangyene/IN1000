from rack import Rack
## Klasse for representasjon av regneklynge med racks og noder
#  MERK to alternative konstruktorer, avhengig av om oppgave d) loeses
class Regneklynge:
	## Oppretter tom regneklynge for racks med oppgitt maxtall noder/ rack
	# @param noderPerRack max antall noder som kan plasseres i et rack
	def __init__(self, noderPerRack):
		self.racks = []

	## Alternativ konstruktor for de som loser oppgave d). Kan ellers ignoreres
	## Leser data om regneklynge fra fil, bygger datastrukturen.
	# @param filnavn filene der dataene for regneklyngen ligger
#	def __init__(self, filnavn):
#		pass

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
	def settInnNode(self, node):
	    if len(self._racks) == 0:
            self._racks.append(Rack())
        for e in self._racks:
            if e.getAntNoder() < self._noderPerRack:
                e.settInn(node)
            elif self._racks[-1].getAntNoder() == self._noderPerRack:
                self._racks.append(Rack())

	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer
	def antProsessorer(self):
        count = 0
		for rack in self.racks:
            count += rack.antProsessorer()
        return count

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		count = 0
        for rack in self.racks:
            count += rack.noderMedNokMinne
        return count

	## Henter antall racks i regneklyngen
	# @return antall racks
	def antRacks(self):
		return len(self.racks)
