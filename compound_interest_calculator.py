principle = 0 
rate = 0
time = 0


while principle <= 0 :
    principle = float(input("Entrez un nombre >0: "))
    if principle <= 0:
        print ("principle doit être supérieur ou égal à 0")

while rate <= 0 :
    rate = float(input("Entrez un intérêt >0: "))
    if rate <= 0:
        print ("rate doit être supérieur ou égal à 0")

while time <= 0 :
    time = int(input("Entrez un temps en année: "))
    if time <= 0:
        print ("time doit être supérieur ou égal à 0")


total = principle* pow((1+rate/100), time)
print(f"Balance after {time} year/s: {total:.2f}€")