from aktivitet import Aktivitet
class Ukedag:
    def __init__(self, dag):
        self._dag = dag
        self._aktiviteter = {}


    def settInn(self, hva, kl):
        if len(self._aktiviteter) == 0:
            self._aktiviteter[kl] = Aktivitet(hva, kl)
        elif kl not in self._aktiviteter:
            self._aktiviteter[kl] = Aktivitet(hva, kl)
        else:
            print("Opptatt klokkeslett")


    def tidligste(self):
        minst = 25
        for e in self._aktiviteter:
            if e < minst:
                minst = e
        if len(self._aktiviteter) == 0:
            return -1
        else:
            return minst


    def seneste(self):
        størst = -1
        for e in self._aktiviteter:
            if e > størst:
                størst = e
        if len(self._aktiviteter) == 0:
            return -1
        else:
            return størst


    def antall(self):
        return len(self._aktiviteter)


    def printAktiviteter(self):
        print(self._aktiviteter)


    def settInnLedig(self, hva, tidligst, senest):
        teller = 0
        for e in self._aktiviteter:
            teller += 1
        if teller >= 24:
            print("Det er fullt med aktiviteter")
        elif teller == 0:
            self._aktiviteter[kl] = Aktivitet(hva, 12)
            pass
