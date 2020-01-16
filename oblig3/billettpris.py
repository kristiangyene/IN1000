"""
Programmet skal ta inn alderen til brukeren for å finne ut hvor mye brukeren må
betale for billett.
"""


def billettProsedyre():
    alder = int(input("Skriv inn alderen din her:\n>"))
    pris = 0
    if alder <= 17:
        pris = 30
    elif alder > 17:#and alder < 65:
        pris = 50
    elif alder > 65:
        pris = 35
    print("billett koster:", str(pris) + "kr")

"""
Problemet med denne prosedyren er at om brukeren er eldre enn 65 så er brukeren
også eldre enn 17. Det som kommer ut i terminalen vil uansett bli 50. Dersom
programmet skal fungere optimalt må man legge til "and alder < 65".
"""
billettProsedyre()
billettProsedyre()
billettProsedyre()
billettProsedyre()
