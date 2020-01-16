class Stasjon:
    def __init__(self, stasjonsnavn):
        self._navn = stasjonsnavn.strip()
        self._nabo = None

    def legg_til_nabo(self, nabo_stasjon):
        self._nabo = nabo_stasjon

    def hent_nabo(self):
        return self._nabo

    def hent_navn(self):
        return self._navn


def hovedprogram():
    trikke_stall =  Stasjon("Trikkestallen")
    forrige = trikke_stall
    for line in open("trase.txt"):
        denne = Stasjon(line)
        forrige.legg_til_nabo(denne)
        forrige = denne

    maal = input("Hvor vil du reise?:\n>")
    her = trikke_stall
    while her != maal:
        her = her.hent_nabo()
        print(her.hent_navn())
    print("Du klarte det!")

hovedprogram()
