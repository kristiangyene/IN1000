from gave import Gave
class Barn:
    def __init__(self, navn):
        self._navn = navn
        self._gaver = []
        self._verdi = 0

    def retNavn(self):
        return self._navn

    def retVerdi(self):
        return self._verdi

    def apneGave(self, navn, verdi):
        self._gaver.append(Gave(navn, verdi))
        self._verdi += verdi

    def skrivBarn(self):
        print(self._navn)
        print("Alle gaver:")
        for e in self._gaver:
            i = e.retNavn()
            print(i)
        print("Total verdi av gaver", self._verdi)
        print()
