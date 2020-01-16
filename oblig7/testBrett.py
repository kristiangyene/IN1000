from random import randint
from celle import Celle

def tegnBrett(self):
    for radene in self._rader:
        rader = []
        for kolonnene in self._rader:
            kolonnene = Celle()
            rader.append(kolonnene)
        self._rutenett.append(rader)
