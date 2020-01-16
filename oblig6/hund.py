class Hund:
    def __init__(self, alder, vekt, metthet):
        self._alder = int(alder)
        self._vekt = int(vekt)
        self._metthet = 10

    def hentAlder(self):
        return self._alder

    def hentvekt(self):
        return self._vekt

    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1

    def spis(self):
        mat = 3
        self._metthet = mat + self._metthet
        if self._metthet > 7:
            self._vekt += 1
