# List[] = ordered and changeable. Duplicates are allowed

fruits = ["Apple", "Mango", "Banana", "Watermelon"]

print(fruits)

print(fruits[0:3])

for fruit in fruits:
    print(fruit)

# List Functions
# print(help(dir(fruits)))
print(len(fruits))
print("Apple" in fruits)
print("Pineapple" in fruits)

fruits[0] = "Pineapple"
print("Pineapple" in fruits)

fruits.append("Guava")  # Adds element at end of the list
fruits.remove("Pineapple")  # To remove any element in list
fruits.insert(0, "Pineapple")  # inserts element at given index
fruits.sort()  # Sort in Alphabetical order
fruits.reverse()  # Elements are reversed in order that they are inserted
fruits.clear()  # to clear the list
fruits.index("Guava")  # To return index of any element in the list, error if element is not in list
fruits.count("Guava")  # to count how many times an elements occurs in the list