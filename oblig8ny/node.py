## Klasse for representasjon av noder i en regneklynge
#
class Node:
	## Oppretter en node med gitt minne-storrelse og antall prosessorer
	#  @param minne GB minne i den nye noden
	#  @param antPros antall prosessorer i den nye noden
    def __init__(minne, antpros):
        self.minne = minne
        self.antPros = antPros

	## Henter antall prosessorer i noden
	#  @return antall prosessorer i noden
    def antProsessorer():
        return self.antPros

	## Sjekker om noden har tilstrekkelig minne for et program
	#  @param paakrevdMinne GB minne som kreves for programmet
	#  @return True hvis noden har minst saa mye minne
	def nokMinne(self, paakrevdMinne):
		if self.minne >= paakrevdMinne:
            return True
        return False
