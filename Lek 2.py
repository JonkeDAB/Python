# variabler för att komma ihåg namn och ålder

# Läsa in namn
name = input("Skriv ditt namn här: ")
# Läsa in ålder
age = int(input("Skriv din ålder: "))

# skriva ut om du är 18 eller inte
if age > 17:
    print("Hej", name , "du är", age ,"år")
else:
    print ("du har inte fyllt 18 än")