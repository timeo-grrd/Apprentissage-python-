import random

nbr_matrice = 1

utilisateur = int(input("Choissiez un nombre impair: "))

while utilisateur % 2 ==0:
    print("ATTENTION tu dois choisir un nombre impair: ")
    utilisateur = int(input("Choissiez un nombre impair: "))

l = random.randint(0, utilisateur - 1)
c = random.randint(0, utilisateur - 1)

somme_carre = ((utilisateur **2) *(utilisateur**2 +1))/(2*utilisateur)
matrice = []
for i in range(utilisateur):
    nouvelle_ligne= [0]*utilisateur
    matrice.append(nouvelle_ligne)    
for ligne in matrice:
    print()
    
matrice[l][c]=nbr_matrice
for i in range (nbr_matrice+1, utilisateur**2+1):
    if matrice[(l+2)% utilisateur][(c+1)%utilisateur] != 0:
        matrice[(l+1) %utilisateur][c %utilisateur]=i
        l = (l+1) %utilisateur
        
    else:
        matrice[(l+2) %utilisateur][(c+1)%utilisateur]=i
        l = (l+2) %utilisateur
        c = (c +1) %utilisateur
    # print(l,c)

print(f"\n-----------------------------Voici le carré magique que l'on obtient avec une matrice d'ordre {utilisateur}---------------------------------\n")


for matrices in matrice:
    print(matrices)

# for i in range (2, utilisateur-1):
#     matrice[+1][+2]+=1

print()
print(f"La somme de chaques lignes et chaques colonne est de: {somme_carre}")










# carre = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]

# for carree in carre:
#     print() 
#     print(carree, end=" ")

# print()
# print("---------Sommes des lignes -----------")

# somme_l1 = carre[0][0]+carre[0][1]+carre[0][2]
# somme_l2 = carre[1][0]+carre[1][1]+carre[1][2]
# somme_l3 = carre[2][0]+carre[2][1]+carre[2][2]
# print(somme_l1)
# print(somme_l2)
# print(somme_l3)


# print("---------Sommes des colonnes -----------")

# somme_c1 = carre[0][0]+carre[1][0]+carre[2][0]
# somme_c2 = carre[0][1]+carre[1][1]+carre[2][1]
# somme_c3 = carre[0][2]+carre[1][2]+carre[2][2]
# print(somme_c1)
# print(somme_c2)
# print(somme_c3)