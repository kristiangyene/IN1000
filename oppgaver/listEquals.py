def equals(liste_en, liste_to):
    teller = 0
    for e in liste_en:
        assert liste_en[teller] == liste_to[teller]
        teller += 1


liste1 = [1,2,3,4,5]
liste2 = [1,2,3,4,5]
equals(liste1, liste2)
