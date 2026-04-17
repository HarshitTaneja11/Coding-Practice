# Hangman
import random

words = [
    "Max Verstappen",
    "Lewis Hamilton",
    "Pierre Gasly",
    "Ayrton Senna",
    "Sebastian Vettel",
    "Sergio Perez",
    "Charles Leclerc",
    "Alex Albon",
    "Fernando Alonso",
    "Micheal Schumacher",
    "Mick Schumacher",
    "Isack Hadjar",
]


# dictionary of key:()
hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\"),
}


def display_man(wrong_guesses):
    print("**************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(f"The answer was {answer}")


def main():
    answer = random.choice(words).lower()
    hint = [" " if ch == " " else "_" for ch in answer]
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("INVALID INPUT!!")
            continue

        if guess in guessed_letters:
            print(f"{guess} has already been guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False
        elif wrong_guesses >= (len(hangman_art) - 1):
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()
