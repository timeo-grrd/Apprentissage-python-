fruits = ["pomme", "orange", "banane", "ananas"]
legumes = ["haricot", "carotte", "bettrave"]
viandes =["poulet", "cheval", "porc"]

# liste_course = [fruits, legumes, viandes]
liste_course = [["pomme", "orange", "banane", "ananas"],
                ["haricot", "carotte", "bettrave"],
                 ["poulet", "cheval", "porc"]]


# 
#  
# print(liste_course[2])
# print(liste_course[1][1])

for liste_courses in liste_course :
    for nourriture in liste_courses : 
        print (nourriture, end=" ")
    print() 

