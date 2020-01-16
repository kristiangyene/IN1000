class Aktivitet:
    #Klokken er et heltall 1-24
    def __init__(self, hva, kl):
        self._aktNavn = hva
        self._start = kl

    def hentKl(self):
        return self._start

class Ukedag:
    def __init__(self, dag):
        self._dag = dag

    def settInn(self, hva, kl):
        for aktivitet in self._dag:
            if kl == aktivitet.hentKl():
                print("Klokkeslettet er opptatt.")
        self._dag.append(Aktivitet(hva, kl))

    def tidligste(self):
        if len(self._dag) == 0:
            return -1
        tidligste = self._dag[0].hentKl()
        for aktivitet in self._dag:
            if tidligste > aktivitet.hentKl():
                tidligste = aktivitet.hentKl()
        return tidligste

    def seneste(self):
        if len(self._dag) == 0:
            return -1
            seneste = self._dag[0].hentKl()
            for aktivitet in self._dag:
                if seneste < aktivitet.hentKl():
                    seneste = aktivitet.hentKl()
            return seneste

    def antall(self):
        count = 0
        for aktivitet in self._dag:
            count+=1
        return count
