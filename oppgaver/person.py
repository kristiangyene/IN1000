class Person:
    def __init__(self, navn):
        self._navn = navn
        self._gift = None

    def minStatus(self):
        if self._gift == None:
            print("Jeg er på sjekker'n")
        else:
            print("Beklager, jeg er alt gift med", self._gift)


    def bryllup(self, annenPerson):
        self._gift = annenPerson.hentNavn()

    def hentNavn(self):
        return self._navn
