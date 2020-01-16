def dupli(liste):
    nyListe = []
    for e in liste:
        if e not in nyListe:
            nyListe.append(e)
    return nyListe

print(dupli([1,2,2,"b",4,5,"b"]))

#eller

#def dupli(liste):
#    return list(set(liste))
