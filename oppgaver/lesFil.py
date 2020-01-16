fil = open("fil.txt")
liste = []
for navn in fil:
    navn = navn.strip("\n")
    liste.append(navn)

print(liste)
