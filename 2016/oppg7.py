class Gave:
    def __init__(self, navn, pris):
        self._navn = navn
        self._pris = pris

    def hentPris(self):
        return self._pris

    def hentNavn(self):
        return self._navn

    def __str__(self):
        return "Navn: " + self._navn + ". Pris: " + str(self._pris) + "."

class Barn:
    def __init__(self, navn):
        self._navn = navn
        self._gaverAapnet = []
        self._totPris = 0

    def hentNavn(self):
        return self._navn

    def totPris(self):
        return self._totPris

    def aapneGave(self, gave):
        self._gaverAapnet.append(gave)
        self._totPris += gave.hentPris

    def skrivBarn(self):
        print("Barnets navn: " + self._navn + "\nGaver aapnet:")
        for gave in self._gaverAapnet:
            gave.__str__()
        print("Totalverdi: " + self._totPris)

class Julekalender:
    def __init__(self, apnereNavn, gaveFil):
        self._historikk = {}
        self._lesHistorikk("Historikk.txt")
        self._apnere = []
        self._kalender = []
        for navn in apnereNavn:
            self._apnere.append(Barn(navn))
        self._lesGavefil()
        self.dag = 1 #Antar at kalenderen starter på dag 1.
        self._nesteApner = self._apnere[0]


    def nyDag(self):
        self._nesteApner.aapneGave(self._kalender[self.dag-1])
        self.dag+=1
        self._apnere.insert(len(self._apnere), self._nesteApner)
        self._apnere.pop(0)
        self._nesteApner = self._apnere[0]

    def gaveOversikt(self):
        for barn in self._apnere:
            barn.skrivBarn()

    def _lesGavefil(self, gaveFil):
        for line in open(gaveFil):
            gaveNavn, gavePris = line.split(",")
            self._kalender.append(Gave(gavePris, gaveNavn))

    def _lesHistorikk(self, histfilnavn):
        #Antar at absolutt alle gaver for hvert barn er i kun en linje.
        for line in open(histfilnavn):
            gaveListe = line.split(" ")
            barnNavn = gaveListe.pop(0)
            self._historikk[barnNavn] = gaveListe


    def avvergetLike(self):
        counter = 0
        while self._kalender[self.dag-1] in self._historikk.get(self._nesteApner) and counter != 24-self.dag:
            self._kalender.append(self._kalender.pop(self.dag-1))
            return False
        return True
