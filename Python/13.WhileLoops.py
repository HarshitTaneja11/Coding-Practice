name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") # there has to be a condition to exit out of the loop
print(f"Hello, {name}")

food = input("Enter a food you like to eat (Enter 'q' to quit): ")

while not food == "q":
    print(food)
    food = input("Enter a food you like to eat (Enter 'q' to quit): ")