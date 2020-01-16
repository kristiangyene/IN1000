class Person:
    def __init__(self, navn):
        self._navn = navn

    def hentNavn(self):
        return self._navn


class Personsystem:
    def __init__(self):
        self._personer = []

    def leggTilPerson(self, person):
        self._personer.append(person)

    def finnPerson(self, person):
        for e in self._personer:
            if e == person:
                k = e.hentNavn()
            return k

    def printListe(self):
        for e in self._personer:
            e = e.hentNavn()
            print(e)



def hovedprogram():
    sys = Personsystem()
    p = Person("kristian")
    a = Person("abe")
    j = Person("johan")
    n = Person("ano")
    m = Person("markus")
    sys.leggTilPerson(p)
    sys.leggTilPerson(a)
    sys.leggTilPerson(j)
    sys.leggTilPerson(n)
    sys.leggTilPerson(m)
    sys.printListe()
    print(sys.finnPerson("abe"))

hovedprogram()
