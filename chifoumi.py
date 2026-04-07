import random

options = ("pierre", "feuille" , "ciseaux")


running = True


while running :
    player = None
    computer = random.choice(options)
    while player not in options:
        player= input("choisissez enter (pierre, feuille, ciseaux): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player  == computer : 
        print("égalité")
    elif player == "pierre" and computer =="ciseaux":
        print("victoire")
    elif player == "feuille" and computer == "pierre":
        print("victoire")
    elif player == "ciseaux" and computer == "feuille":
        print("victoire")
    else:
        print("défaite")
    play_again = input("play again ? (y/n): ").lower()
    if not play_again == "y":
        running = False
print("merci d'avoir joué")