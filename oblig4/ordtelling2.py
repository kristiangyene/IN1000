def ordtelling(setning):
    ordbok = {}
    liste = setning.split()
    for i in liste:
        ordbok[i] = liste.count(i)
    return ordbok
a = ordtelling("Hei jeg liker sjoko jeg")
print(a)
