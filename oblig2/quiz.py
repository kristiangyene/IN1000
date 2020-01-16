"""
I denne oppgaven har jeg laget en quiz der brukeren blir spurt om en rekke
morsomme spørsmål. Det er enkle ja/nei spørsmål og jeg har satt inn en score
som teller antall poeng der målet er å få 6/6 riktige.
"""

print("             \x1b[6;30;42m*****VELKOMMEN TIL QUIZ*****\x1b[0m\nHer får du en rekke med spørsmål du skal svare ja/nei på!")
print("                     LYKKE TIL:)")
print()
a = str(input("Er det tigre i Afrika?\n>"))
a = a.lower()
score = 0
if a == "ja" or a == "jepp" or a == "jupp":
    print("Du svarte feil..")
    score = score
    print("Score:", score)
elif a == "nei" or a == "nope" or a == "neias":
    print("Du svarte riktig!")
    score = score + 1
    print("Score:", score)

print()
b = str(input("Har vi over 200 bein i kroppen?\n>"))
b = b.lower()
if b == "ja" or b == "jepp" or b == "jupp":
    print("Du svarte riktig! Skjelettet består av 206 enkeltknokler.")
    score = score + 1
    print("Score:", score)

elif b == "nei" or b == "nope" or b == "neias":
    print("Du svarte feil.. Skjelettet består av 206 enkeltknokler.")
    score = score
    print("Score:", score)

print()
d = str(input("Er hvalen vår største fisk?\n>"))
d = d.lower()
if d == "ja" or d == "jepp" or d == "jupp":
    print("Du svarte feil.. Hvalen er ikke en fisk, men et pattedyr.")
    score = score
    print("Score:", score)

elif d == "nei" or d == "nope" or d == "neias":
    print("Du svarte riktig! Hvalen er ikke en fisk, men et pattedyr.")
    score = score + 1
    print("Score:", score)

print()
c = str(input("Bruker man salt i pannekakerøren?\n>"))
c = c.lower()
if c == "ja" or c == "jepp" or c == "jupp":
    print("Du svarte riktig! Ganske merkelig.")
    score = score + 1
    print("Score:", score)


elif c == "nei" or c == "nope" or c == "neias":
    print("Du svarte feil.. Ganske merkelig.")
    score = score
    print("Score:", score)

print()
e = str(input("Kan vann flyte på olje?\n>"))
e = e.lower()
if e == "ja" or e == "jepp" or e == "jupp":
    print("Du svarte feil.. Det er omvendt.")
    score = score
    print("Score:", score)

elif e == "nei" or e == "nope" or e == "neias":
    print("Du svarte riktig! Det er omvendt.")
    score = score + 1
    print("Score:", score)

print()
f = str(input("Hadde USA det første fartøyet som nådde månens overflate?\n>"))
f = f.lower()
if f == "ja" or f == "jepp" or f == "jupp":
    print("Du svarte feil.. Det var sovjet med Luna 2.")
    score = score
    print("Score:", score)

elif f == "nei" or f == "nope" or f == "neias":
    print("Du svarte riktig! Det var sovjet med Luna 2.")
    score = score + 1
    print("Score:", score)



print()
print("Du fikk", str(score) + "/6", "riktige svar.")
print("Tusen takk for at du deltok i denne quizen!\nHåper du har lært litt av den:)")
print()
print('\x1b[6;30;42m' + 'By Kristian Gyene' + '\x1b[0m')
