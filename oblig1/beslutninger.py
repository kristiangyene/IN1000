#Poenget er at brukeren skal kunne svare på et enkelt
#ja/nei-spørsmål.
#Programmet stiller først brukere et spørsmål som blir printet ut:
print("Vil du ha en brus? (ja/nei)")

c=input()
#Definerer svaret(som kan være hva som helst) som c.
#Dersom man svarer "ja" så vil "ja"=c=input() så printes ut
#"Her har du en brus!".
if c=="ja" or c=="JA":
    print("Her har du en brus!")
#Dersom man svarer "nei" så vil "nei"=c=input() så printes ut
#"Den er grei".
elif c=="nei" or c=="NEI":
    print("Den er grei.")

#For at vi skal få denne responsen på et svar som kan være
#hva som helst unntatt de svarene jeg har lagt inn, må jeg
#bruke else.
else:
    print("Det forstod jeg ikke helt.")
#Denne oppgaven fant jeg ut kan løses på flere måter. Jeg la
#også til et par svar til "JA" og "NEI" for å gjøre den litt
#mer interessant. Da brukte jeg kommandoen or.
