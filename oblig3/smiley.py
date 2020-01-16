"""
Oppgave: lag et program som lar brukeren velge størrelse på en smiley og
hvilken farge den skal ha. lag en liste med størrelser og kall den "hode". ​
Importer ​modulen EzGraphics og lag en smiley i disse tre størrelsene. Om
brukeren skriver inn noe annet skal programmet vise en error.

Programmet skal gi brukeren tre alternativer til hvor stor smiley man
vil ha, og hvilken farge man ønsker. Dersom man ikke inn noe programmet ikke
tillater vil det komme opp et vindu med error.
"""

print("Her kan du lage din eget smiley!")
print()
listSmiley = ["liten", "medium", "stor"]
print("Hvor stort skal fjeset være?")
hode = str(input("Skriv liten/medium/stor:\n>"))
farge = str(input("hvilken farge skal det være?\n>"))

from ezgraphics import GraphicsWindow
win = GraphicsWindow()
canvas = win.canvas()
ordbok = {"svart":"black", "rød":"red", "gul":"yellow", "grønn":"green",\
"blå":"blue", "gull":"gold" , "oransje":"orange", "rosa": "pink", \
"brun":"brown", "hvit":"white", "grå":"grey", "lilla":"purple"}
norsk = ordbok[farge]
if  hode == listSmiley[2]:
    canvas.setOutline(norsk)
    canvas.drawOval(1, 1, 395, 395)
    canvas.setOutline(norsk)
    canvas.drawOval(95, 75, 100, 100)
    canvas.setOutline(norsk)
    canvas.drawOval(205, 75, 100, 100)
    canvas.setOutline(norsk)
    canvas.setFill("black")
    canvas.drawOval(130, 110, 30, 30)
    canvas.setOutline(norsk)
    canvas.setFill("black")
    canvas.drawOval(240, 110, 30, 30)
    canvas.setOutline(norsk)
    canvas.drawLine(100 ,300 ,300 , 300)

elif hode == listSmiley[1]:
    canvas.setOutline(norsk)
    canvas.drawOval(1, 1, 300, 300)
    canvas.setOutline(norsk)
    canvas.drawOval(80, 75, 60, 60)
    canvas.setOutline(norsk)
    canvas.drawOval(170, 75, 60, 60)
    canvas.setOutline(norsk)
    canvas.setFill("black")
    canvas.drawOval(97, 95, 25, 25)
    canvas.setOutline(norsk)
    canvas.setFill("black")
    canvas.drawOval(187, 95, 25, 25)
    canvas.setOutline(norsk)
    canvas.drawLine(90 ,200 ,210, 200)

elif hode == listSmiley[0]:
    canvas.setOutline(norsk)
    canvas.drawOval(1, 1, 200, 200)
    canvas.setOutline(norsk)
    canvas.drawOval(40, 45, 50, 50)
    canvas.setOutline(norsk)
    canvas.drawOval(120, 45, 50, 50)
    canvas.setOutline(norsk)
    canvas.setFill("black")
    canvas.drawOval(57, 65, 17, 17)
    canvas.setOutline(norsk)
    canvas.setFill("black")
    canvas.drawOval(137, 65, 17, 17)
    canvas.setOutline(norsk)
    canvas.drawLine(55 ,140 ,150, 140)

else:
    canvas.drawRect(100, 100, 200, 200)
    canvas.setColor("red")
    canvas.drawText(103, 110, "ERROR!")
    canvas.drawText(103, 150, "Programmet støtter ikke det du skrev.")

win.wait()
