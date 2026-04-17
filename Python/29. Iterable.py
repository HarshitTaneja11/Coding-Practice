# Iterable - an object/collection that can return its elements one at a time
#            allowing it to be iterated over in a loop

numbers = [1,2,3,4,5] #lists are iterable
numbers = (1,2,3,4,5) #tuples are iterable
numbers = {1,2,3,4,5} #sets are iterable but not reversable

for number in numbers:
    print(number)

# --------------------------------------------------------------------------------

name = "Harshit Taneja" # Strings are iterable
for ch in name:
    print(ch, end=" ")
print()

# --------------------------------------------------------------------------------

dictionary = {"A" : 11, "B" : 33, "C" : 44}
for key in dictionary:
    print(key)

for value in dictionary.values():
    print(value)

for key, value in dictionary.items():
    print(key, value)

# --------------------------------------------------------------------------------