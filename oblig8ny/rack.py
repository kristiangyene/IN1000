from node import Node
## Klasse for representasjon av racks i en regneklynge.
#
class Rack:
	## oppretter et rack der det senere kan plasseres noder
	#
	def __init__(self):
		self.rack = []

	## Plasserer en ny node inn i racket
	#  @param node noden som skal plasseres inn
	def settInn(self, node):
		self.rack.add(node)

	## Henter antall noder i racket
	# @return antall noder
	def getAntNoder(self):
		return len(self.rack)

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
	def antProsessorer(self):
		count = 0
        for node in self.rack:
            count += node.antProsessorer()
        return count

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		count = 0
        for node in self.rack:
            if node.nokMinne(paakrevdMinne):
                count++
        return count
