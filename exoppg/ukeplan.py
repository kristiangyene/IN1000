from aktivitet import Aktivitet
class Ukeplan:
    def __init__(self, hvem):
        self._navn = hvem
        self._dager = []


    def travleste(self):
        teller = 0
        for e in self._dager:
            for f in e:
                teller += 1
        return teller

    def skrivUt(self, dag):
        print(dag + ":", )
