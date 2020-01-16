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
treTerninger()
