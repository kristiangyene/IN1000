#Først velger jeg to verdier som variabler og bruker print() for å skrive
#dem ut på hver sin linje i terminal. Jeg setter opp en variabel som er
#summen av de første variablene. Programmet skriver ut summen i terminal.

tall1 = 5
tall2 = 12
print(tall1)
print(tall2)

#Terminalen vil vise "sum:17"
#Bruker + for å summere og kommandoen str() for å vise at jeg mener
#tallverdiene.
tallsum = tall1 + tall2
print("Sum:" + str(tallsum))

#Terminalen vil vise først "velkommen" og "etter" etterfulgt av
# "velkommenetter".
#(Kan også sette inn mellomrom i en av strengene for å få resultatet som
#på neste deloppgave).
tekst1 = "velkommen"
Tekst2 = "etter"
print(tekst1)
print(Tekst2)
sammen = tekst1 + Tekst2
print(sammen)

#Nå vil terminalen vise det samme på en linje bare med et mellomrom
#i mellom. Brukte to anførseltegn og mellomrom i mellom. Dette funket for
#meg, men det er sikkert andre måter å gjøre det på.
sammen = tekst1 + " " + Tekst2
print(sammen)
