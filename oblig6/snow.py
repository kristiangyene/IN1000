class Snowboarder:

    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        self.triks = []

    def leggTilTriks(self, etTriks):
        self.triks.append(etTriks)

    def slettTriks(self, etTriks):
        self.triks.remove(etTriks)

    def skrivUt(self):
        print(self.navn, self.alder)
