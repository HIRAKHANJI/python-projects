import art
import random


def intro_func():
    print(art.logo)
    print("Welcome to the number guess.")

def chance_selector(option_selected):
    modes_options = {"easy": 10, "hard": 5}
    return modes_options[option_selected]


intro_func()
choice_made = input("Choose easy(10 tries) or hard(5 tries) mode: ")
chances_total = chance_selector(choice_made)
guessed = False
selected_word = random.randint(1, 100)

while not guessed and chances_total > 0:
    answer = int(input("What's your guess? "))

    if answer == selected_word:
        print(f"Correct, {selected_word}")
        guessed = True
    elif answer > selected_word:
        chances_total -= 1
        print(f"Too high, {chances_total} left")
    elif answer < selected_word:
        chances_total -= 1
        print(f"Too low, {chances_total} left")

if guessed:
    # They won (guessed = True broke the loop)
    # Already printed win message, nothing to do
    pass
else:
    # They lost (chances_total hit 0)
    print(f"You've run out of guesses. The answer was {selected_word}")


