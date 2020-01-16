print("Velkommen til hangman!")

inp1 = input("Skriv inn ordet du ønsker\n>")
ordet = list(inp1)
if " " in ordet:
    ordet.remove(" ")
bokstaver = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
"q","r","s","t","u","v","w","x","y","z","æ","ø","å"]
print("Du kan ha 12 mulige feil")
muligeFeil = 0
while muligeFeil != 12:
    inp2 = input("Velg en bokstav\n>")
    if inp2 in bokstaver:
        if inp2 in ordet:
            print("Bokstaven var i ordet!")
            bokstaver.remove(inp2)
            ordet.remove(inp2)
    else:
        print("Dessverre.. bokstaven er ikke i ordet.")
        muligeFeil += 1
    print()
