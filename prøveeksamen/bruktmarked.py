from kategori import Kategori
class Bruktmarked:

    def __init__(self):
        self._dict = {}


    def nyKategori(self, katNavn):
        if katNavn in self._dict:
            return None
        else:
            kategori = Kategori(katNavn)
            self._dict[katNavn] = kategori
            return kategori


    def finnKategori(self, katNavn):
        if katNavn in self._dict:
            return self._dict[katNavn]
        else:
            return None

    def tellLaveBud(self):
        teller = 0
        for e in self._dict:
            for f in e.hentAnnonser:
                for t in f.hentBudStr:
                    teller += 1
