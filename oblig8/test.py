from node import Node
from rack import Rack
from regneklynge import RegneKlynge
"""
e = Rack()

n = Node(32, 2)
f = Node(128, 4)
g = Node(32, 2)
d = Node(64, 3)
a = Node(54, 2)
e.settInn(n)
e.settInn(f)
e.settInn(g)
e.settInn(d)
e.settInn(a)

print(e.getAntNoder())
print(e.antProsessorer())
print(e.noderMedNokMinne(32))
"""

r = RegneKlynge(12)
n = Node(64, 1)
f = Node(1024, 2)
#g = Node(32, 2)
#d = Node(64, 3)
r.settInnNode(n)
#r.settInnNode(f)
#r.settInnNode(g)
#.settInnNode(d)



#print(r.antRacks())
