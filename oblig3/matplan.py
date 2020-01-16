matplan = {}
matplan["Kristian"] = ["egg", "sandwich", "burger"]
matplan["Jørgen"] = ["ristet brød", "omelett", "pasta carbonara"]


def search():
    inp = input("Hvem sin matplan ønsker du å se?\n>")
    for key, value in matplan.items():
        if key == inp:
            print(value)
            return;
    print("Personen er ikke registrert.")
search()
