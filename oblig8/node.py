"""Oppretter en klasse Node. Legger minne og antall prosessorer i
konstruktoeren. Metoden antProsessorer skal kun returnere antall prosessorer.
Metoden nokMinne skal returnere True hvis minnet er stoerre eller likt et
paakrevd minne."""

class Node:
	#Oppretter en node med gitt minne-storrelse og antall prosessorer.
	def __init__(self, minne, antPros):
		self._minne = minne
		self._antPros = antPros

	#Henter antall prosessorer i noden.
	def antProsessorer(self):
		return self._antPros

	#Sjekker om noden har tilstrekkelig minne for et program.
	def nokMinne(self, paakrevdMinne):
		if self._minne >= paakrevdMinne:
			return True
