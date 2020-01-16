#Bruker kommandoen print() slik at programmet skal skrive ut teksten
#"Hei Student!" til terminal, og deretter skrive ut hei etterfulgt av et
#navn du kan sette inn selv.
print("Hei Student!")

#Bruker kommandoen input() for at man skal kunne bytte ut
#variabelen "navn" med hva man vil(f.eks sitt eget navn).
#Terminalen vil altså vente til man har skrevet noe som skal
#erstatte variabelen så den kan fortsette programmet.
#Skriver man f.eks "Kristian", blir det "HeiKristian"
navn = input()
print("Hei" + navn)
