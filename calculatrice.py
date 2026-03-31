text0 = input("Entrez uniquement un nombre entier et positif:")
text1 = input ("entrez soit +,-,/,*:")
text2 = input("Entrez uniquement un nombre entier et positif:")
nombre0 = int(text0)
nombre2 = int(text2)

if text1 == "+":
    print (nombre0 + nombre2)

elif text1 == "-": 
    print (nombre0 - nombre2)

elif text1 == "*":
    print (nombre0 * nombre2)

elif text1 == "/":
    print(nombre0 / nombre2)

