# Tuples() = ordered and unchangeable. Duplicates are OK, Faster program

formula1 = ("RedBull", "Ferrari", "Haas", "Audi", "Cadillac", "Ferrari")

print(formula1)
print(len(formula1))
print("Haas" in formula1)
print(formula1.index("Audi"))  # to return the index of the entered element
print(formula1.count("Ferrari"))  # to count the number of same element occurring in the tuple
for teams in formula1:  # we can use loops to print each element
    print(teams)
