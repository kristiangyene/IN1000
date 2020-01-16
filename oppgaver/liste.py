#lage liste med terningkast
terninger = []
terninger.append(int(input("terning1: ")))
terninger.append(int(input("terning2: ")))
terninger.append(int(input("terning3: ")))
terninger.append(int(input("terning4: ")))
terninger.append(int(input("terning5: ")))
print(terninger)

#hvor mange poeng?
poeng = terninger.count(4) *4
print(poeng)

#Har man fått yatsy?
ulike = set(terninger)
print(len(ulike) == 1)

#fire eller hus
ulike = set(terninger)
fire_eller_hus = len(ulike) == 2
en_av_terningene = terninger[0]
terninger.count(en_av_terningene)
hus = fire_eller_hus and (antall == 2 or antall == 3)
print(hus)
