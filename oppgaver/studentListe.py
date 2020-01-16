class Student:
    def __init__(self, navn, brukernavn, telefonnr):
        self._navn = navn
        self._brukernavn = brukernavn
        self._telefonnr = int(telefonnr)

    def printInfo(self):
        print("Navn:", self._navn)
        print("Brukernavn:", self._brukernavn)
        print("Telefonnummer:", self._telefonnr)

    def navn(self):
        return self._navn


def testprogram():
    ordbok = {}
    k = Student("kristian", "kristsgy", 98486668)
    a = Student("Abenayan", "abenayak", 47586933)
    j = Student("Johan", "johanat", 98382912)
    ordbok[k.navn()] = k
    ordbok[a.navn()] = a
    ordbok[j.navn()] = j

    inp = input("skriv inn navn du ønsker å finne informasjon om:\n>").lower()
    if inp in ordbok:
        ordbok[inp].printInfo()
testprogram()
