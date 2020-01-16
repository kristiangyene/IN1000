from gjest import Gjest
class Rorbu:
    def __init__(self):
        self._gjester = []

    def nyGjest(self, gjest):
        self._gjester.append(gjest)
        for e in self._gjester:
            e.underhold(1)

    def fortellVits(self, heltall):
        for e in self._gjester:
            e.underhold(heltall)

    def hvorMorsomtHarViDet(self):
        teller = 0
        for e in self._gjester:
            teller += e.hentUnderholdningsverdi()
            gjennomsnitt = teller / len(self._gjester)
        return gjennomsnitt

    def kommentarer(self):
        gradMorsomt = self.hvorMorsomtHarViDet()
        if gradMorsomt < 200:
            return "Kjedelig kveld"

        elif gradMorsomt >= 200 and gradMorsomt < 400:
            return "Dette var jo litt gøy"

        elif gradMorsomt >= 400 and gradMorsomt < 600:
            return "Dette var artig!"
        elif gradMorsomt >= 600:
                return "Dra på Lopphavet - bi dæ godtar no så gyt e!"

    def underholdningsverdi(self):
        teller = 0
        for e in self._gjester:
            teller += e.hentUnderholdningsverdi()
        return teller

    def antallGjester(self):
        return len(self._gjester)
