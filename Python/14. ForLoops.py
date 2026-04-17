for x in range(1, 11):  # prints 1 to 10
    print(x)
print("------------------------------------------------------")



for x in reversed(range(1, 11)):  # to print 10 to 1
    print(x)
print("------------------------------------------------------")



for x in range(1, 11, 3):  # to print 1 to 10 in interval of 3
    print(x)
print("------------------------------------------------------")



for x in range(1, 21):
    if x == 13:
        continue  # to skip an iteration
    else:
        print(x)
print("------------------------------------------------------")



for x in range(1, 21):
    if x == 13:
        break # to break the loop at a specific point
    else:
        print(x)
print("------------------------------------------------------")
