import random

words = ["python", "apple", "mango", "laptop", "coding"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

display_word = "_" * len(secret_word)

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_attempts and "_" in display_word:

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter!")
        continue

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

if "_" not in display_word:
    print("\nCongratulations! You won!")
    print("The word was:", secret_word)
else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)