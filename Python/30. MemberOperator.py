# membership operators - used to test whether a value or variable is found in a sequence
# (strin, list, tuple, set or dictionary)
#  1. in 2. not in

word = "formula1"

letter = input("Guess a letter in the secret word: ")
if letter in word:
    print(f"There is a {letter} in the word")
else:
    print(f"{letter} not found")

# --------------------------------------------------------------------------------

players = {"Kohli", "Pant", "Gill"}
guess = input("Enter surname of a cricket player: ")
if guess not in players:
    print("Player not found :(")
else:
    print("Player found!")

