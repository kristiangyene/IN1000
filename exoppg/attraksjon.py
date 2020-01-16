class Attraksjon:

    def __init__(self, navn, barn, fra, til):
    self._navn = navn
    self._fra = fra
    self._til = til

    def skrivAttr(self):
        print("attraksjon:", self._navn)

    def forBarn(self):
        return True

    def aapenIPeriode(self, fra, til):
        if self._fra
