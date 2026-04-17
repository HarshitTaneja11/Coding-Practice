# Exception = An event thata interrupta the flow of a progra,
#             (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2. except, 3. finally

# int("Pizza") # will cause error

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You cannot divide by zero IDIOT!")
except ValueError:
    print("Enter numbers only please!")
except Exception:
    print("Something went wrong!")
finally:  # Always Executes
    print("Do some cleanup")


