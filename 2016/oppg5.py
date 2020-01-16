def dobbelListe(liste):
    list = []
    for tall in liste:
        list.append(tall)
    while len(list) != (len(liste)*2):
        list.append(0)
    return list
