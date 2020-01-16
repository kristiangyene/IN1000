"""
Siden funksjonen ikke har definert a vil det komme opp en feilmelding. Dersom
man setter a = 0, vil funskjonen antageligvis fungere som den var ment. Først
defineres to funksjoner, minFunksjon() og hovedprogram(). Deretter kjøres
hovedprogram(). a defineres som 42, og b som 0. b printes ut så 0 kommer ut.
b defineres som a som er 42. Funksjonen minFunksjon() blir kalt på. Range(2)
gjør at den går igjennom funksjonen to ganger. c defineres som 2. c blir printet
og 2 kommer ut. c adderer seg selv med 1, c defineres som 3. b defineres som
10. b printes ut etter at den har addert seg med a, og det som printes ut
avhenger av hva a er definert som. Dersom man setter a = 0 så printes det ut 10.
Så går x til neste i range(2). c og b blir printet igjen(2 og 10 i terminal).
Return-verdien blir 10. Går tilbake til hovedprogram() og skriver ut a og b, 10
og 42. Merk: b hadde ikke hatt denne verdien om a hadde vært definert som
noe annet. Det var bare for å få en lettere forståelse.
"""

#a = 0
def minFunksjon(): #1, 9
    for x in range(2): #10, 17
        c = 2 #11, 18
        print(c) #12, 19
        c += 1 #13, 20
        b = 10 #14, 21
        b += a #15, 22
        print(b) #16, 23
    return(b) #24

def hovedprogram(): #2, 25
    a = 42 #4
    b = 0 #5
    print(b) #6
    b = a #7
    a = minFunksjon() #8
    print(b) #26
    print(a) #27

hovedprogram() #3
