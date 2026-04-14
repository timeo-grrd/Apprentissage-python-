import time

my_time = int(input("Entrez le temps en seconde: "))


for i in reversed(range (1, my_time)):
    secondes= i % 60
    minutes = int(i /60) % 60
    heure = int(i / 3600)
    print(f"{heure:02}:{minutes:02}:{secondes:02}")
    time.sleep(1)
print("coucou niels")