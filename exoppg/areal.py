def beregnAreal(lengde, bredde):
    areal = lengde * bredde
    if areal < 0:
        return -1
    return areal

print(beregnAreal(2, -6))
