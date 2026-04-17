# we use tuple -> ordered and unchangeable , to print number pad of telephone

num_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for row in num_pad:
    for val in row:
        print(val, end=" ")
    print()
