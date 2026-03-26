#or
# temp = 25
# is_rainning = True

# if temp > 35 or temp < 0 or is_rainning:
#     print("the outdoor event is cancelled")
# else:
#     print("the outdoor event is still scheduled")

#and
temp = 0
is_sunny = False
if temp >= 28 and is_sunny:
    print("it is hot outside")
    print("it is sunny") 
elif temp <= 0 and is_sunny:
    print("it is cold outside")
    print("it is sunny")
elif temp < 28 and temp > 0 and is_sunny:
    print("it is warm outside")
    print("it is sunny")
elif temp >= 28 and not is_sunny:
    print("it is hot outside")
    print("it is cloudy") 
elif temp <= 0 and not is_sunny:
    print("it is cold outside")
    print("it is cloudy")
elif temp < 28 and temp > 0 and not is_sunny:
    print("it is warm outside")
    print("it is cloudy")



