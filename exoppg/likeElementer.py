def funk(liste):
    element = liste[0]
    for e in liste:
        if e == element:
            sant = True
        else:
            sant = False
            break
    return sant


print(funk([2,2,2,2]))
