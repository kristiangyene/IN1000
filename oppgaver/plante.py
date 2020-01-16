class Plante:
    def __init__(self, maksgrenseVann):
        self._vannbeholder = 0
        self._maksgrenseVann = maksgrenseVann
        self._levende = True

    def vannPlante(self, vannCl):
        self._vannbeholder += vannCl

    def nyDag(self):
        self._vannbeholder -= 20

    def levende(self):
        if self._vannbeholder > self._maksgrenseVann:
            self._levende = False
        elif self._vannbeholder < 0:
            self._levende = False
        else:
            self._levende = True
        return self._levende

    def skrivUt(self):
        print(self._vannbeholder)
        print(self._maksgrenseVann)

p1 = Plante(40)
p2 = Plante(90)
p1.vannPlante(10)
p2.vannPlante(100)
p1.nyDag()
p1.nyDag()
p2.nyDag()
p2.nyDag()
print(p1.levende())
print(p2.levende())
p1.skrivUt()
p2.skrivUt()
