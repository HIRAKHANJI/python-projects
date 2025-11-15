import random
import hangman_words
import hangman_art

lives = 6
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            print(f"{guess} is correct, keep going!")
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is wrong. -1 Life, try again!")
        if lives == 0:
            game_over = True
            print(f"\n***********************YOU LOSE**********************\n"
                  f"{chosen_word}, was the correct answer!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives]+"\n")
