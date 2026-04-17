# function is a block of reusable code
# place () after func name to invoke it

def bdaywish():
    print("Happy birthday to you!")
    print("God Bless you!!!")

bdaywish()
bdaywish()

# -------------------------------------------------------------------------

def bdaywish(name, age):
    print(f"Happy birthday {name}")
    print(f"You are {age} years old!")
    print("God Bless you")

bdaywish("Harshit", 21)

# -------------------------------------------------------------------------

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due on {due_date}")

display_invoice("Harshit Taneja", 123.15, "16/02/2026")

# -------------------------------------------------------------------------

def add(x,y):
    z = x+y
    return z

def divide(x,y):
    z = x/y
    return z

z = add(10,11)
print(z)

z = divide(10,11)
print(z)

