"""
Programmet skal importere​ ​modulen 'ezgraphics' og tegne en enkel​ ​rød​ ​sirkel.
"""
from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()
canvas.setOutline("red")
#canvas.setFill("red") for å fylle sirkelen med rødt.
canvas.drawOval(100, 100, 200, 200)

win.wait()
