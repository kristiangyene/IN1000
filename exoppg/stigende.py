def funk(liste):
    teller = liste[0] - 1
    rekkefolge = True
    for e in liste:
        if e > teller:
            rekkefolge = True
            teller = e
        elif e < teller:
            rekkefolge = False
            break
    return rekkefolge

print(funk([1,2,3,1]))
