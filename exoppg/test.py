from ukedag import Ukedag
u = Ukedag("torsdag")


u.settInn("Svømming", 5)
u.settInn("Yoga", 6)
u.settInn("fotball", 7)
#print(u.antall())
print("Den tidligste aktiviteten er kl:", u.tidligste())
print("Den seneste aktiviteten er kl:", u.seneste())
print("antall aktiviteter:", u.antall())
u.settInnLedig("Håndball", 12, 20)
u.printAktiviteter()
