from gjest import Gjest
from rorbu import Rorbu
def Hovedprogram():
    rorbu = Rorbu()
    for e in range(100):
        e = Gjest()
        rorbu.nyGjest(e)
    rorbu.fortellVits(200)
    print(rorbu.kommentarer())
    rorbu.fortellVits(1000)
    print(rorbu.kommentarer())

Hovedprogram()
