import random

# print(help(dir(random)))

dice = random.randint(1,20)
print(dice)


A = 10 
B = 199
number = random.randint(A,B)
print(number)

options = ("Rock", "Paper", "Scissors")
print(random.choice(options))

cards = ["2", "3", "4", "5", "A", "Q", "K"]
random.shuffle(cards)
print(cards)