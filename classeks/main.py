from sykdomsKatalog import SykdomsKatalog
from pasient import Pasient

katalog = SykdomsKatalog("sykdommer_test.csv")
pasient = Pasient("Mutasjoner_test.txt")
for posisjon in pasient.alleMutasjoner():
    
