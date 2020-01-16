from time import sleep
a = 1
b = 1
c = 1
sant = True
while sant:
    if a == 6:
        b += 1
        a = 1
    if b == 7:
        c += 1
        b = 1
    a += 1
    if c == 6 and b == 6 and a == 6:
        sant = False
    tall = str(c) + " " + str(b) + " " + str(a)
    print(tall)
    sleep(0.01)
