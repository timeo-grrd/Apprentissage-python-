capitales = {"France": "Paris",
             "Espagne" : "Madrid",
             "Italie" : "Rome",
             "Russie" : "Moscou"}

# print(capitales.get("France"))

# if capitales.get("Japon"):
#     print("Cette capitale existe")
# else:
#     print("Cette capitale n'existe pas")

# capitales.update({"Allemagne" : "Berlin"})
# capitales.update({"France" : "Nantes"})
# # capitales.pop("Espagne")
# capitales.popitem()
# capitales.clear()
# print(capitales)

# keys = capitales.keys()
# # print(keys)

# for key in capitales.keys():
#     print (key)


# values = capitales.values()
# print(values)

# for values in capitales.values():
#     print (values)

# items = capitales.items()
# print(items)
# print(capitales)

for key, value in capitales.items():
    print(f"{key}: {value}")