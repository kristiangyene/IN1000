from gjest import Gjest
from rorbu import Rorbu
def Hovedprogram():
    r1 = Rorbu()
    r2 = Rorbu()
    r1 = r2
    for e in range(50):
        e = Gjest()
        r1.nyGjest(e)

    for e in range(75):
        e = Gjest()
        r2.nyGjest(e)
    print(r1.antallGjester())




Hovedprogram()
