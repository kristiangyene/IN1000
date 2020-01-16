from kategori import Kategori
from bruktmarked import Bruktmarked
from bud import Bud
from annonse import Annonse
def hovedprogram():
    bruktmarked = Bruktmarked()
    kategori = bruktmarked.nyKategori("Sykkellykt")
    annonse = kategori.nyAnnonse("New Yorker sykkellykt")
    annonse.giBud("Peter", 42)
    annonse.giBud("Ann", 0)
    annonse.kraftBud("Mary", 40, 50)
    print(annonse.hoyesteBud())
    

hovedprogram()
