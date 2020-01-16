def besteHus(t):
    antallFemmere = 0
    antallSeksere = 0
    for tall in t:
        if tall == 5:
            antallFemmere += 1
        elif tall == 6:
            antallSeksere += 1
    if antallFemmere == 2 and antallSeksere == 3:
        return True
    return False


def hus(t):
    kast = [0, 0, 0, 0, 0, 0]
    for tall in t:
        kast[tall-1] +=1

    if 2 in kast and 3 in kast:
        return kast
    return kast

print(hus([3,4,3,2,2]))
