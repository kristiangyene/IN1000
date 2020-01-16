class EspressoMaskin:
    def __init__(self):
        self._vanntank = 1000

    # Lag espresso dersom det er nok vann
    def lag_espresso(self):
        if self._vanntank >= 40:
            self._vanntank -= 40
        return "Her har du espressoen din"


    # Lag lungo dersom det er nok vann
    def lag_lungo(self):
        if self._vanntank >= 110:
            self._vanntank -= 110
        return "Her har du lungoen din"

    # Fyll paa et gitt antall milliliter vann, dersom det er plass
    def fyll_vann(self, ml):
        self._vanntank += ml

    # Les av maalestrekene på vanntanken og tilgjengelig vann i ml
    def hent_vannmengde(self):
        return self._vanntank


def hovedprogram():
    m = EspressoMaskin()
    print(m.lag_espresso())
    m.lag_espresso()
    m.lag_espresso()
    m.lag_espresso()
    m.lag_espresso()
    m.lag_lungo()
    m.lag_lungo()
    m.lag_lungo()
    m.lag_lungo()
    m.lag_lungo()
    m.lag_lungo()
    m.fyll_vann(4000)
    print(m.hent_vannmengde())

hovedprogram()
