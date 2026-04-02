operant1 = float(input("rentrez un chiffre:"))
operant2 = input("rentrez soit +,-,*,/:")
operant3 = float(input("rentrez un chiffre:"))

if operant2 != "+"and operant2 !="-" and operant2!="/"and operant2!= "*":
    print("erreur")
if  operant2== "+":
    print(operant1 + operant3)

elif operant2 == "-":
    print(operant1-operant3)

elif operant2 == "*":
    print(operant1*operant3)
elif operant2== "/":
    print(operant1/operant3)





