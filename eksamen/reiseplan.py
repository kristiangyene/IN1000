class Hytte:
    def __init__(self, navn, antSenger, prisSeng):
        self._navn = navn
        self._antSenger = antSenger
        self._prisSeng = prisSeng


    def hentNavn(self):
        return self._navn

    def totPris(self, antPersoner):
        totalt = self._prisSeng * antPersoner
        return totalt

    def skrivHytte(self):
        print(self._navn + ".", "Antall senger:", self._antSenger + ".", "Pris per seng:", self._prisSeng + ".")

    def sjekkPlass(self, antPersoner):
        if antPersoner <= self._antSenger:
            return True
        else:
            return False


class Tur:
    def __init__(self, hytter, tekst):
        self._hytter = hytter
        self._tekst = tekst


    def skrivTur(self):
        print("Beskrivelse av tur:")
        print(self._tekst)
        print("Hytter turen går innom:")
        for e in self._hytter:
            e.skrivHytte()

    def sjekkPrisPlass(self, antPersoner, maksBelop):
        pris = 0
        for e in self._hytter:
            plass = e.sjekkplass(antPersoner)
            pris += e.totPris(antPersoner)
        if plass == True and pris <= maksBelop:
            return True
        else:
            return False


class Turplanlegger:
    def __init__(self, hytteFil, turFil):
        self._hytter = self.hytterFraFil(hytteFil)
        self._turer = self.turerFraFil(turFil)


    def hytterFraFil(self, filnavn):
        hytter = {}
        fil = open(filnavn)
        for linjer in fil:
            linjer = linjer.strip()
            biter = linjer.split()
            hyttenavn = biter[0]
            senger = int(biter[1])
            pris = float(biter[2])
            hytter[hyttenavn] = Hytte(hyttenavn, senger, pris)
        return hytter

    def finnTurer(self, antPersoner, maxPris, maxDager):
        dager = 0
        while dager != maxdager:
            prisPlass = self._turer[dager].sjekkPrisPlass(antPersoner, maxPris)
            if prisPlass == True:
                self._turer[teller].skrivTur()
            dager += 1

def testprogram():
    plan = Planlegger("hytter.txt", "turer.txt")
    plan.finnTurer(7, 7000, 5)

testprogram()
