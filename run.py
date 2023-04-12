"""
Import random to allow randon word selection
"""

import random

HANGMAN_PICS = [r'''
   +---+
   |   |
       |
       |
       |
       |
=========''', r'''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', r'''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''',  r'''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', r'''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', r'''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', r'''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']


words = ["Acura", "Alfa Romeo", "Aston Martin", "Audi", "Bentley", "BMW",
         "Bugatti", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Dodge",
         "Ferrari", "Fiat", "Ford", "GMC", "Honda", "Hyundai", "Infiniti",
         "Jaguar", "Jeep", "Kia", "Koenigsegg", "Lamborghini", "Land Rover",
         "Lexus", "Lincoln", "Lotus", "Maserati", "Mazda", "McLaren",
         "Mercedes-Benz", "Mini", "Mitsubishi", "Nissan", "Noble", "Pagani",
         "Polestar", "Porsche", "Ram", "Rimac", "Rolls-Royce", "Subaru",
         "Suzuki", "Tesla", "Toyota", "Volkswagen", "Volvo"]


def show_intro():
    """
    Welcome them to the game and get their username.
    let the press a key when they are ready to start playing
    """

    print("  /\\  /\\ __ _  _ __    __ _  _ __ ___    __ _  _ __ ")
    print(" / /_/ // _` || '_ \\  / _` || '_ ` _ \\  / _` || '_ \\ ")
    print("/ __  /| (_| || | | || (_| || | | | | || (_| || | | |")
    print("\\/ /_/  \\__,_||_| |_| \\__, ||_| |_| |_| \\__,_||_| |_|")
    print("                      |___/                          ")

    username = " "
    while True:
        username = input(
            "Welcome to Hangman! Please enter your name: \n"
            )
        print()

        if username.isalnum() is not True:
            print("Error: Letters and numbers only.")

        print(f"Hi {username}, You have upto 6 guesses to guess the Word.")
        print()
        print("If you don't guess the word, the man is hung and you lose")
        print()
        print("Each secret word relates to a different car manfacturer.")
        print()
        input("When you are ready to play, press the Enter key to start \n")
        return username


def get_random_word(word_list):
    """Return a random string from the passed list of strings."""
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


def game_board():
    """Display the current state of the game board."""
    print(HANGMAN_PICS[len(INCORRECT_LETTERS)])
    print()

    print('Wrong guesses:', end=' ')
    for char in INCORRECT_LETTERS:
        print(char, end=' ')
    print()

    blanks = '_' * len(HIDDEN_WORD)

    for i, char in enumerate(HIDDEN_WORD):
        # Replace blanks with correctly guessed letters
        if char in CORRECT_LETTERS:
            blanks = blanks[:i] + char + blanks[i+1:]

    for char in blanks:
        # Show the secret word
        print(char, end=' ')
    print()


def get_guess(already_guessed):
    """Get the letter the player entered."""
    while True:
        print('Guess a letter.')
        new_guess = input().lower()
        if len(new_guess) != 1:
            print('Please enter a single letter.')
        elif new_guess in already_guessed:
            print('Oops! You have already guessed that letter. Choose again.')
        elif new_guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter.')
        else:
            return new_guess


show_intro()


# Runs main game
print('H A N G M A N')
INCORRECT_LETTERS = ''
CORRECT_LETTERS = ''
HIDDEN_WORD = get_random_word(words)
GAME_OVER = False

while not GAME_OVER:
    game_board()

    # Let the player enter a letter.
    guess = get_guess(INCORRECT_LETTERS + CORRECT_LETTERS)

    if guess in HIDDEN_WORD:
        CORRECT_LETTERS = CORRECT_LETTERS + guess

        # Check if the player has won.
        FOUND_ALL_LETTERS = True
        for j, letter in enumerate(HIDDEN_WORD):
            if HIDDEN_WORD[j] not in CORRECT_LETTERS:
                FOUND_ALL_LETTERS = False
                break
        if FOUND_ALL_LETTERS:
            print('Woohoo! The secret word is "' + HIDDEN_WORD +
                  '"! You have won!')
            print()
            GAME_OVER = True
    else:
        INCORRECT_LETTERS = INCORRECT_LETTERS + guess

        # Check if player has guessed too many times and lost
        if len(INCORRECT_LETTERS) == len(HANGMAN_PICS) - 1:
            game_board()
            print(
                'You have run out of guesses!\nAfter '
                + str(len(INCORRECT_LETTERS)) +
                ' wrong guesses and ' + str(len(CORRECT_LETTERS))
                + ' correct guesses, the word was "' + HIDDEN_WORD + '"')
            print()
            GAME_OVER = True

    # Check if the player wants to play again
    if GAME_OVER:
        while True:
            PLAY_AGAIN = input(
                "Do you want to play again? (yes or no): "
            ).lower()
            if PLAY_AGAIN == 'yes':
                INCORRECT_LETTERS = ''
                CORRECT_LETTERS = ''
                GAME_OVER = False
                HIDDEN_WORD = get_random_word(words)
                break
            if PLAY_AGAIN == 'no':
                print()
                print("Thanks for playing Hangman! Come back soon.")
                break
            print("Invalid choice. Please select 'yes' or 'no'.")
            print()
