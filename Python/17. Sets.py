# Set{} = unordered and immutable, but add/remove is allowed. No duplicates

cars = {"Audi", "BMW", "Maruti", "McLaren", "Ferrari"}

# print(dir(cars)) --> to display attributes and methods
# print(help(dir(cars)))

print(len(cars))
print("Audi" in cars)
cars.add("Honda")  # To add element
cars.remove("Maruti")  # To remove element
cars.pop()  # Removes random element
cars.clear()
cars.add("BMW")  # No duplicates are allowed
