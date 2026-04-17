questions = (
    "Who is the youngest-ever Formula 1 World Champion?",
    "Which circuit is located in the heart of the Austrian countryside and is known for its picturesque scenery and challenging corners?",
    "Which F1 constructor is based in Maranello, Italy and has won 16 Drivers' Championships and 15 Constructors' Championships?",
    "What is the name of the F1 car's protective structure that is designed to protect the driver's head in the event of an accident?",
)

options = (
    ("A. Vettel ", "B. Verstappen", "C. Hamilton ", "D. Senna"),
    ("A. Red Bull Ring", "B. Jeddah", "C. Baku", "D. COTA"),
    ("A. McLaren", "B. Ferrari", "C. Alfa Romeo", "D. Mercedes"),
    ("A. DRS", "B. ERS", "C. HALO", "D. WING"),
)


answers = ("A", "A", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!")
    else:
        print("WRONG :(")
        print(f"{answers[question_num]} is the correct answer")
    question_num = question_num + 1

print(f"Your total Score is {score} out of 4 ")
