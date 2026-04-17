# indexing = accessing elements of a sequence using [] (indexing operator)
# [start:end:stop]
# the index of a string starts with 0
# we can also use negative indexing

ID_Number = "1234-5678-9102"

print(ID_Number[0])
print(ID_Number[0:4])
print(ID_Number[:4])  # means that start to index 4
print(ID_Number[0:])  # prints from start to end
print(ID_Number[::2])  # prints from start to end with a step of 2
print(ID_Number[::4])  # prints from start to end with a step of 4

last_digits = ID_Number[-4:]  # using negative indexing to print last 4 digits
print(f"XXXX-XXXX-{last_digits}")

print(ID_Number[::-1])  # to reverse a string
