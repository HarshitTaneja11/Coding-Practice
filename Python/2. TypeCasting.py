# Typecastint = process of converting one data type into another


name = "Harshit"
age = 20
gpa = 9.18
is_student = True

print(type(is_student)) #returns the data type of the variable
print(type(gpa))

gpa = int(gpa) # changes the data type of the variable
print(gpa)

age = str(age)
print(type(age))
age = age + "1"
print(age)

name = bool(name)
print(name)