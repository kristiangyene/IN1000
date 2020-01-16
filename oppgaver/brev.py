import time
class Brev:
    def __init__(self, sender, mottaker):
        self._sender = sender
        self._mottaker = mottaker
        self._liste = []


    def skrivLinje(self, tekststreng):
        self._liste.append(tekststreng)


    def lesBrev(self):
        print("Hei,", self._mottaker + "!")
        time.sleep(1)
        for e in self._liste:
            print(e)
            time.sleep(1)
        print("Hilsen fra,\n" + self._sender)


b = Brev("Kristian", "Anine")
b.skrivLinje("Du betyr")
b.skrivLinje("alt for meg.")
b.lesBrev()
