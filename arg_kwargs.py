# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("non","peut être", "ouui")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}") 

# print_address(street="123 Fake St.",
#                apt="100",
#                state="MI", 
#                zip="12345")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs :
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")

    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongeboob", "Squarepants",
               street="123 Fake St.",
               apt="#122",
               city="Detroit",
               state="MI",
               zip="541354")

# print(shipping_label)