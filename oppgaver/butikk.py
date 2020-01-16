broed = 20
melk = 15
ost = 40
youghurt = 12

print("Hei! Velkommen til ifi-butikken.")
antallBroed = int(input("Hvor mange broed vil du ha?\n>"))

antallMelk = int(input("Hvor mange melk vil du ha?\n>"))

antallOst = int(input("Hvor mange ost vil du ha?\n>"))

antallYoughurt = int(input("Hvor mange yoghurt vil du ha?\n>"))

totalt = antallYoughurt * int(broed) + antallOst * int(ost) + antallMelk * int(melk) + antallBroed * int(broed)

print("Du skal betale:", totalt, "kr")
