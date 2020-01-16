from annonse import Annonse
class Kategori:

    def __init__(self, katNavn):
        self._katNavn = katNavn
        self._annonser = []


    def nyAnnonse(self, annTekst):
        annonse = Annonse(annTekst)
        self._annonser.append(annonse)
        return annonse


    def hentAnnonser(self):
        return self._annonser
