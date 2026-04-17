fruits = ["Apple", "Orange", "Banana", "Pineapples"]
vegetables = ["Celery", "Carrots", "Tomatos"]
meats = ["Chicken", "Fish", "Mutton"]

groceries = [fruits, vegetables, meats]

print(groceries[0][1])  # [row][column]
print(groceries[0][0])  # [row][column]
print(groceries[2][2])  # [row][column]

for row in groceries:
    for column in row:
        print(column, end=" ")
    print()


# we can also create a list of tuples
# a tuple of tuples
# a set of sets
# a tuple of sets
