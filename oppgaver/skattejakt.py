skattekart = []
stoerrelse = 5


for e in range(stoerrelse):
    a = []
    for e in range(stoerrelse):
        a.append("O")
    skattekart.append(a)

for e in skattekart:
    for f in e:
        print (f, end="")
    print("")

print("SPILLER 1: SETTE INN KOORDINATER TIL SKATTEN")


x = int(input("skriv inn x-koordinat(må være innefor 0-5):\n>"))
y = int(input("skriv inn y-koordinat(må være innefor 0-5):\n>"))
x -= 1
y -= 1

skattekart[x][y] = "X"

for e in skattekart:
    for f in e:
        print (f, end="")
    print("")

input("-Trykk enter for neste spiller-")

for e in range(100):
    print()

x1 = 10
y1 = 10
while x1 != x or y1 != y:
    x1 = int(input("skriv inn x-koordinat(må være innefor 0-5):\n>"))
    y1 = int(input("skriv inn y-koordinat(må være innefor 0-5):\n>"))
