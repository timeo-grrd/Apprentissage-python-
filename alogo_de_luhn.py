def luhn(numero):
    somme = 0
    n = len(numero)
    
    for i in range(n):
        chiffre = int(numero[n - 1 - i])
        if i % 2 == 1: 
            chiffre = chiffre * 2
            if chiffre >= 10:
                chiffre = chiffre - 9
        somme = somme + chiffre
    return somme % 10 == 0
print(luhn("79927398713"))