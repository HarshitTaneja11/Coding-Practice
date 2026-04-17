# *args - allows tou to pass multiple no-key(positional) arguments, tuple of arguments is recieved

#  * unpacking operator


def add(*numbers):
    # print(type(numbers))
    total = 0
    for num in numbers:
        total = total + num
    return total


print(add(1, 2, 3))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


display_name("Harshit", "Sandeep", "Taneja")

# --------------------------------------------------------------------------------

# **kwargs - allows you to pass multiple keyword - arguments, passed as dictionary


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print_address(
    street="2037 Vinings Circle", apt=308, city="Wellington", state="Florida", zip=33414
)


# --------------------------------------------------------------------------------

# Excercise


# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for values in kwargs.values():
#         print(values, end=" ")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "Floor" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('Floor')}")
    else:
        print(f"{kwargs.get('street')}")  
    print(f"{kwargs.get('city')}, {kwargs.get('state')}")
    print(f"{kwargs.get('pincode')}")


shipping_label(
    "Harshit",
    "Taneja",
    street="8/53 South Patel Nagar",
    Floor="1st floor",
    city="New Delhi",
    state="Delhi",
    pincode=110008,
)
