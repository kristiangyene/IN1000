from sokk import Sokk

class Skuff:
    def __init__(self):
        self._mineSokker = []

    def settInnSokken(self, sokken):
        self._mineSokker.append(Sokk(sokken))

    def sjekkStatus(self):
        tellerH = 0
        tellerV = 0
        for e in self._mineSokker:
            if e.hentSide() == "høyre":
                tellerH += 1
            elif e.hentSide() == "venstre":
                tellerV += 1

        if tellerV == tellerH:
            return "Alt i orden"
        else:
            return "Ulikt antall høyre- og venstresokker"
