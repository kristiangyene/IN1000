fn_peter = "Peter.txt"
tot_peter=0
for line in open(fn_peter):
    utgift_peter = int(line)
    tot_peter += utgift_peter
print("Peter har brukt: ", tot_peter)
fn_paul = "Paul.txt"
tot_paul=0
for line in open(fn_paul):
    utgift_paul = int(line)
    tot_paul += utgift_paul
print("Paul har brukt: ", tot_paul)

---------------------------------------------

def totUtgifter(navn, file):
    counter = 0;
    for line in open(file):
        counter += int(line)
    print(navn + " har brukt: " + counter)

def main():
    totUtgifter(Peter, "Peter.txt")
    totUtgifter(Paul, "Paul.txt")
