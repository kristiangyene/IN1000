class Motorsykkel:

    def __init__(self, merke, registreringsnummer, km) :
        self._merke = merke
        self._registreringsnummer = registreringsnummer
        self._km = int(km)

    def kjor(self, km) :
        self._km += km

    def hentKilometerstand(self) :
        return self._km


    def skrivUt(self) :
        print(self._merke, self._registreringsnummer, self._km)
