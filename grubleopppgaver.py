#Terningkast hus.
def hus(t):
    kast = [0, 0, 0, 0, 0, 0]
    for tall in t:
        kast[tall-1] +=1

    if 2 in kast and 3 in kast:
        return kast
    return kast
print(hus([3,4,3,2,2]))

---------------------------------------------
#Sjekk stigende.
def stigende(liste):
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            return False
    return True

#Sjekk like.
def likeTall(liste):
    for i in range(len(liste) -1):
        if(liste[i] != liste[i+1]):
            return -1
    return liste[0]

---------------------------------------------
#Les fra fil.
def nyDestFraFil(self, destNavn, filnavn):
    if destNavn not in self._destKatalog:
        self._destKatalog[destNavn] = Destinasjon(destNavn, [])
    fil = open(filnavn)
    attrNavn = fil.readline().rstrip()
    while attrNavn != "":
        hvem = fil.readline().rstrip()
        if hvem == "VOKSNE":
            forBarn = False
        else:
            forBarn = True
        fraDato = int(fil.readline().rstrip())
        tilDato = int(fil.readline().rstrip())
        self.nyAttr(destNavn, attrNavn, forBarn, fraDato, tilDato)
        attrNavn = fil.readline().rstrip()

def _lesGavefil(self, gaveFil):
    for line in open(gaveFil):
        gaveNavn, gavePris = line.split(",")
        self._kalender.append(Gave(gavePris, gaveNavn))

---------------------------------------------
#Fjerner 0 begge sider.
def trimZeros(a):
    while(a[0] == 0):
        a.pop(0)
    while(a[-1] == 0):
        a.pop(-1)
    return a
print(trimZeros([0,0,8,0,1,2,0,3,0,0,4,0,0]))

#Teller antall bokstaver.
def telling(string):
    list = []
    for bokstav in string:
        if bokstav not in list:
            list.append(bokstav)
    return len(list)
print(telling("accag"))

--------------------------------------------
#Tre terninger
def treTerninger():
    toLike = []
    counter = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for f in range(1, 7):
                #Print(i, j ,f)
                if i == j or j == f or i == f:
                    list = [i, j, f]
                    toLike.append(list)
    return toLike

-------------------------------------------
#Viderekoblingsoppgavene
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
print(gyldig2([1,-1, 3,4,2]]))#False
