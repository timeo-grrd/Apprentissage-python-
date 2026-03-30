
import math 
num1 = float(input("Entrez une valeur: "))
num2 = float(input("Entrez une valeur: "))
operator = str(input ("Entrez un opérateur (+;-;*;/)"))
résultat=""

if operator == "+":
    résultat=round (num1+num2, 2)
    print(f"l'addition de {num1} et {num2} est égal à: {résultat}" )
elif operator == "-":
    résultat =round (num1-num2, 2)
    print(f"la soustraction de {num1} et {num2} est égal à {résultat}")
elif operator == "/":
    résultat= round(num1/num2, 2)
    print(f"le resultat de la division {num1} et {num2} est égal à {résultat}")
elif operator == "*":
    résultat = round (num1 * num2,2) 
    print(f"le résultat du produit de {num1} et {num2} est de{résultat}")
else:
    print("vérifie ce que tu as mis ")