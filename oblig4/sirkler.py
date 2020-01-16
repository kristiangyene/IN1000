"""
Programmet skal lage en liten animasjon der det kommer ni sirkler
etter hverandre der de blir større fra venstre til høyre.
"""
from ezgraphics import GraphicsWindow
from time import sleep
win = GraphicsWindow()
can = win.canvas()

teller = 0
x_pos = 75
stoerrelse = 50
#Endrer størrelsen og posisjon for hver gang teller øker.
while teller < 9:
    can.drawOval(x_pos, 100, stoerrelse, stoerrelse)
    teller += 1
    stoerrelse += 5
    x_pos += 10
    #sleep(0.1) dersom jeg ønsker en animasjon.
win.wait()
