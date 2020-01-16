"""I hovedprogram oppretter jeg et RegneKlynge-objekt, abel. Oppretter to typer
Node-objekter, og bruker to for-loekker for aa faa det antallet noder jeg trenger.
Til slutt printer jeg ut det jeg trenger og kaller paa metoden noderMedNokMinne()
for aa telle opp.
"""

from node import Node
from regneklynge import RegneKlynge

def hovedprogram():
    #Oppretter RegneKlynge og noder.
    abel = RegneKlynge(12)
    for e in range(650):
        abel.settInnNode(Node(64, 1))
    for i in range(16):
        abel.settInnNode(Node(1024, 2))
    #Printer ut kriteriene.
    print("Noder med minst 32 GB:", abel.noderMedNokMinne(32))
    print("Noder med minst 64 GB:", abel.noderMedNokMinne(64))
    print("Noder med minst 128 GB:", abel.noderMedNokMinne(128))
    print("Antall prosessorer:", abel.antProsessorer())
    print("Antall rack:", abel.antRacks())



hovedprogram()
