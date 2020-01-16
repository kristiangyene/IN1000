import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

lengde = int(input("Hvor langt ønsker du at passordet skal være?"))

passordet = "".join(random.sample(s, lengde))

print(passordet)
