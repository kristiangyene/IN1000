beholdning = {}
print("Tast 'enter' når du er ferdig")
inp = input("Skriv inn grønnsak:\n>")
inp2 = int(input("Skriv inn antall:\n>"))
while inp != "":
    beholdning[inp] = inp2
    inp = input("Skriv inn grønnsak:\n>")
    if inp != "":
        inp2 = int(input("Skriv inn antall:\n>"))

#for e, f in beholdning.items():
#    print("grønnsak:", e, "Antall:", f)

for e in beholdning:
    print("grønnsak:", e, "antall:", beholdning[e])
