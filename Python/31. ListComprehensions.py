# List Comprehension - a concise way to create lists in python
# Compact and easier to read than traditional loops
# (Expression for value in iterable if condition)

doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

# Instead we use
doubles = [x * 2 for x in range(1, 11)]
print(doubles)

cubic = [x ^ 3 for x in range(1, 11)]
print(cubic)

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)

fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)

nums = [2, -3, 4, -5, -6, -1, -7, 12, 54, 23, 33, -81]
pos_nums = [x for x in nums if x >= 0]  # to print positive numbers from the list
print(pos_nums)
neg_nums = [num for num in nums if num < 0]  # to print negative numbers
print(neg_nums)

odd_nums = [num for num in nums if num % 2 != 0]
print(odd_nums)
