"""
Lag et program som holder styr på bursdager ved hjelp av løkker. Programmet
skal kunne gi brukeren mulighet til å legge til og slette kontakter. I tilleg
skal man kunne få en liste over hvilke navn og dag personen har bursdag på.
"""
import time
import sys

ordbok = {"kristian":"20.mars", "silje":"13.april", "john":"21.desember",\
 "david":"01.juni"}
name = ["kristian", "silje", "john", "david"]
day = [ordbok["kristian"], ordbok["silje"], ordbok["john"], ordbok["david"]]
name.sort()
day.sort()
#Lager en startside.
def lobby():
    print()
    start = input(">Hva ønsker du å gjøre?<\n " "\
    \nLegge til bursdag: tast L\
    \nSøke etter navn for å finne bursdag: S\
    \nSe bursdagsliste: tast B\
    \nSe alle navn som er lagt inn: tast N\
    \nSe alle datoer som er lagt inn: tast D\
    \nSlette bursdag: tast R\
    \nAvslutte programmet: tast Q\
    \n>")
    start = start.upper()
    if start == "L":
        setNavn()
    elif start == "B":
        bokList()
    elif start == "S":
        soekNavn()
    elif start == "Q":
        exit()
    elif start == "N":
        listNavn()
    elif start == "D":
        listDato()
    elif start == "R":
        delNavn()

    else:
        print("Programmet støtter ikke det du skrev.")
        print("Du går tilbake til lobby.")
        time.sleep(1)
        lobby()

def bokList():
    print("(Trykk enter for å gå tilbake til lobby)")
    while True:
        print(ordbok)
        b = input(">")
        if b == "":
            print("Du går tilbake til lobby.")
            time.sleep(1)
            lobby()

def setNavn():
    print("(Trykk enter for å gå tilbake til lobby)")
    while True:
        inp_navn = input("Skriv inn navn:\n>")
        inp_navn.lower()
        if inp_navn == "":
            print("Du går tilbake til lobby.")
            time.sleep(1)
            lobby()
            break
        inp_dag = input("Skriv inn bursdag:\n>")
        inp_dag.lower()
        name.append(inp_navn)
        day.append(inp_dag)
        ordbok[inp_navn] = inp_dag

def soekNavn():
    print("(Trykk enter for å gå tilbake til lobby)")
    while True:
        søk = input("Søk etter person du vil finne bursdagen til:\n>")
        søk.lower()
        if søk == "":
            print("Du går tilbake til lobby.")
            time.sleep(1)
            lobby()
            break
        print("Bursdagen til", søk, "er", ordbok[søk] + ".")

def delNavn():
    print("(Trykk enter for å gå tilbake til lobby)")
    while True:
        a = (input("skriv inn navn du ønsker å slette\n>"))
        a.lower()
        if a == "":
            print("Du går tilbake til lobby.")
            time.sleep(1)
            lobby()
            break
        name.remove(a)
        day.remove(ordbok[a])
        ordbok.pop(a)

def listNavn():
    print("(Trykk enter for å gå tilbake til lobby)")
    while True:
        print(name)
        s = input(">")
        if s == "":
            print("Du går tilbake til lobby.")
            time.sleep(1)
            lobby()

def listDato():
    print("(Trykk enter for å gå tilbake til lobby)")
    while True:
        print(day)
        i = input(">")
        if i == "":
            print("Du går tilbake til lobby.")
            time.sleep(1)
            lobby()

def exit():
    print("Programmet avsluttes.")
    time.sleep(1)
    sys.exit()

lobby()
