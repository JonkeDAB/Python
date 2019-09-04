firstName = "Jonas"
middleName = "Daniel"
lastName = "Wirth"
nickName = "JonkeDAB"
domän = "ntig"

#förnamn.efternamn
#Jonas.Wirth
#firstName[3].lastName[3]

#print(firstName[0:3].lower() + "" + lastName[0:3].lower() + "19")
#userName = "firstName[0:3].lower()lastName[0:3].lower()19"
userName = firstName[0:3].lower()
userName += lastName[0:3].lower()
userName += "19"
#print(userName)

#skolmail jonas.wirth@elev.ga.ntig.se

skolmail = firstName.lower()
skolmail += "."
skolmail += lastName.lower()
skolmail += "@elev.ga."
skolmail += domän.lower()
skolmail += ".se"

print(skolmail)



#print(lastName)

tecken = """() parenteser
[] hakparenteser  
{} måsvingar 
: kolon 
; semikolon 
, komma 
\" dubbelfnutt 
\' enkelfnutt"""

#print(tecken)