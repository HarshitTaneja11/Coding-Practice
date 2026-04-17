for x in range(3):
    for y in range(1, 11):
        print(y, end="->")  # to print 1 to 10 in the same line with '->' in between
    print()  # to print empty line

rows = int(input(print("Enter the number of Rows: ")))
columns = int(input(print("Enter the number of Columns: ")))

for r in range(rows):
    for c in range(columns):
        print("-", end= "")
    print()