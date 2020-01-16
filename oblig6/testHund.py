"""
Programmet skal være en oversikt over vekten til en hund. Classen Hund blir
importert. Dersom hundens metthet er høy vil hunden legge på seg, og Dersom
hunden er metthet er lav vil den miste vekt. Den mister metthet av å løpe.
Jeg har kalt på 'spring()' såpass mange ganger så man ser at den mister vekt,
og deretter kalt på spising for å vis at vekten øker. Har også metoder som
returnerer navn og alder men dette brukes ikke i programmet. Kaller på
'hentvekt' etter hver gang hunden gjør noe for å se endringen.
"""


from hund import Hund

def hovedprogram():
    pluto = Hund("7","12", "10")
    print("Hundens vekt til å begynne med:",pluto.hentvekt())
    pluto.spring()
    print("Hundens vekt etter løping:", pluto.hentvekt())
    pluto.spring()
    print("Hundens vekt etter løping:", pluto.hentvekt())
    pluto.spring()
    print("Hundens vekt etter løping:", pluto.hentvekt())
    pluto.spring()
    print("Hundens vekt etter løping:", pluto.hentvekt())
    pluto.spring()
    print("Hundens vekt etter løping:", pluto.hentvekt())
    pluto.spring()
    print("Hundens vekt etter løping:", pluto.hentvekt())
    pluto.spis()
    print("Hundens vekt etter spising:", pluto.hentvekt())
    pluto.spis()
    print("Hundens vekt etter spising:", pluto.hentvekt())
    pluto.spis()
    print("Hundens vekt etter spising:", pluto.hentvekt())
    pluto.spis()
    print("Hundens vekt etter spising:", pluto.hentvekt())

hovedprogram()
