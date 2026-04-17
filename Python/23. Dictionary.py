# A collection of {key:value} pairs
# ordered and changeable, no duplicates allowed

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "Brazil": "Brazilia",
    "England": "London",
    "Russia": "Moscow",
}

# print(help(dir(capitals)))

print(capitals.get("USA"))  # to get value of entered key
print(capitals.get("Japan"))  # if key is not in dictionary then we get "None"

capitals.update({"Japan": "Tokyo"})
capitals.update({"India": "Mumbai"})

capitals.pop("Brazil")

# capitals.clear()

keys = capitals.keys()  # "keys" is an object which resembles a list
print(keys)

for key in capitals.keys():  # to iterate over keys
    print(key)


values = capitals.values()  # "values" is an object which resembles a list
print(values)

items = capitals.items()  # A 2D object which resembles a 2D list of tuples
print(items)

for key, value in capitals.items():
    print(f"{key} : {value}")

print(capitals)
