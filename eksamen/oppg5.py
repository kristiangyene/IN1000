
"""b) Skriv en funksjon gyldig som tar inn en viderekoblingsliste og sjekker om det finnes mulighet for å havne
i en evig løkke av viderekobling i denne listen. Et eksempel er lista [1,-1, 3,4,2] hvor man ved å ringe ansatt 2 blir
viderekoblet til ansatt 3, videre til ansatt 4 og så tilbake igjen til ansatt 2 i en evig løkke.
Dersom det ikke finnes noen slik evig løkke av viderekobling i lista skal funksjonen returnere true.
Dersom det finnes minst én slik løkke av viderekobling skal den returnere False.
Altså skal kallet gyldig([2, -1, -1, 0]) returnere true, mens kallet gyldig([1,-1, 3,4,2]) skal returnere false."""

def ring(ansattnr, liste):
    if liste[ansattnr] == -1:
        return ansattnr
    else:
        return ring(liste[liste[ansattnr]], liste)

print(ring(3, [2, -1, -1, 0]))

def gyldig2(liste) :
    for i in range(len(liste)) :
        j = i
        sett = []
        while liste[j] != -1 :
            sett.append(j)
            j = liste[j]
            if j in sett :
                return False
    return True
