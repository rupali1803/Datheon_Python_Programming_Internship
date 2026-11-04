
import random

# Word list
words = ["PYTHON", "COMPUTER", "PROGRAM", "LAPTOP", "KEYBOARD"]

# Hangman stages
hangman_art = [
    """
     -----
     |   |
         |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]

def display_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    return result

def play_game():
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\nWelcome to Hangman Game!")
    
    while wrong_guesses < max_attempts:
        print(hangman_art[wrong_guesses])
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Wrong guesses:", wrong_guesses)
        print("Remaining attempts:", max_attempts - wrong_guesses)

        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet!")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You Win!")
            print("The word was:", secret_word)
            return

    print(hangman_art[wrong_guesses])
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

# Start the game
play_game()