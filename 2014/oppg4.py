def pris(gratis, alder):
    if gratis:
        return 0
    if(alder < 18):
        return 100
    return 200

#oppg5
def stigende(liste):
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            return False
    return True

#oppg6
def likeTall(liste):
    for i in range(len(liste) -1):
        if(liste[i] != liste[i+1]):
            return -1
    return liste[0]
