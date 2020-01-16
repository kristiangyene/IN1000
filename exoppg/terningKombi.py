#kaster 3 terninger
import time
terning1 = 1
terning2 = 1
terning3 = 0
ferdig = False
while not ferdig:
    if terning3 < 6:
        terning3 += 1
    elif terning3 == 6:
        terning3 = 1
        terning2 += 1
    if terning2 > 6:
        terning3 = 1
        terning2 = 1
        terning1 += 1
    elif terning1 == 6 and terning2 == 6 and terning3 == 6:
        ferdig = True
    print(terning1, terning2, terning3)
    time.sleep(0.01)
