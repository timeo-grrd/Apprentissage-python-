with open("input_calorie.py", "r") as f:
    data = f.read()

max_calories = 0
max_calories2 = 0
max_calories3 = 0
somme_calorie = 0


for ligne in data.split("\n"):
    if ligne == "":
        if somme_calorie > max_calories:
            max_calories3 = max_calories2
            max_calories2 = max_calories
            max_calories = somme_calorie
        
        elif somme_calorie > max_calories2:
            max_calories3 = max_calories2
            max_calories2 = somme_calorie
        
        elif somme_calorie > max_calories3:
            max_calories3 = somme_calorie   
        somme_calorie = 0
    else:
        somme_calorie += int(ligne)

    
somme3lutin = max_calories + max_calories2 + max_calories3
print(somme3lutin)
print(max_calories)
print(max_calories2)
print(max_calories3)