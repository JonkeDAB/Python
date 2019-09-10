print("Välkommen till mit program där du kan addera")

try:
    tal1 = int(input("mata in ett heltal: "))
except:
    print("Du måste skriva en siffra")
    tal1 = int(input("prova igen: "))

try:
    tal2 = int(input("mata in ett till heltal: "))
except:
    print("Du måste skriva en siffra")
    tal2 = int(input("Prova igen"))
    
summa = tal1 + tal2
print("Summan är: " + str(summa))