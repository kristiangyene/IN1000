barn = {"Halfdan":"Harald", "Christian":"Hans", "Harald":"Eirik", "Eirik":"Danny"}
def arverekker(forfader, etterkommer, forstefodte):
    liste = []
    eldst = forfader
    liste.append(eldst)
    while eldst != etterkommer:
        eldst = forstefodte[eldst]
        liste.append(eldst)
    return liste

personer = arverekker("Halfdan", "Danny", barn)
print(personer)
