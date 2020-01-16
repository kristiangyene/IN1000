import random

alt = ["stein", "saks", "papir"]
comp = ""
inp = ""
while comp == inp:
    inp = input("Stein, saks, papir?\n")
    comp = random.choice(alt)
    print()
    print(inp, "vs", comp)
    if comp == "stein" and inp == "saks":
        print("Du tapte.")
    elif comp == "stein" and inp == "papir":
        print("Du vant!")
    elif comp == "saks" and inp == "stein":
        print("Du vant!")
    elif comp == "saks" and inp == "papir":
        print("Du tapte.")
    elif comp == "papir" and inp == "stein":
        print("Du tapte.")
    elif comp == "papir" and inp == "saks":
        print("Du vant!")
