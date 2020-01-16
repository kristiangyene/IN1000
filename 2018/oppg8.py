def fyllTilTi(tallene):

    while len(tallene) != 10:
        tallene.append(0)
    return tallene

print(fyllTilTi([2,3,4]))
