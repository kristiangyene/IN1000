liste = []
tall = 0
while tall != 10:
    tall = int(input("Skriv et tall: "))
    liste.append(tall)

minSum = 0
for e in liste:
    minSum += e
print("Summen i listen:", minSum)
