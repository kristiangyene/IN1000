def bokstavteller(ord):
    teller = 0
    for bokstav in ord:
        teller+= 1
    return teller

def ordOversikt(setning):
    ordbok = {}
    ordliste = setning.split(" ")
    for ord in ordliste:
        ordbok[ord] = ordbok.get(ord, 0) + 1
    return ordbok

def ordteller(setning):
    teller = 0;
    ordliste = setning.split(" ")
    for ord in ordliste:
        teller += 1
    return teller



def main():
    setning = input("Skriv en setning:\n>")
    ordbok = ordOversikt(setning)
    print("Det er" , ordteller(setning), "ord i setningen.")
    for key in ordbok:
        print("Ordet", key, "forekommer", ordbok[key],
        "gang(er) og har", bokstavteller(key), "bokstav(er).")

main()
