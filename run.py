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


words = "basketball football baseball soccer tennis golf hockey \
        volleyball rugby badminton tabletennis swimming athletics \
        gymnastics wrestling boxing cycling skiing snowboarding \
        archery shooting fencing rowing kayaking canoeing diving \
        weightlifting powerlifting bodybuilding triathlon marathon \
        pentathlon decathlon surfing skateboarding rockclimbing \
        mountaineering fishing hunting horsebackriding \
        polo squash racquetball lacrosse ultimatefrisbee \
        kickboxing karate taekwondo judo aikido capoeira \
        jiu-jitsu muaythai crossfit parkour calisthenics bocce croquet \
        curling darts billiards bowling skating sledding \
        tobogganing bobsleigh luge snowmobiling \
        kiteboarding windsurfing parasailing".split()


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
        username = input("Welcome! Please enter your Name: \n")

        if username.isalnum() is not True:
            print("Error: Letters and numbers only.")

        print(f"Hi {username}, You have upto 6 guesses to guess the Word.")
        print()
        print("If you don't guess the word, the man is hung and you lose")
        print()
        print("Each secret word relates to a different sport.")
        print()
        input("When you are ready to play, Press the Enter key to start \n")
        return username


def get_random_word(word_list):
    """Return a random string from the passed list of strings."""
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


def display_board():
    """Display the current state of the game board."""
    print(HANGMAN_PICS[len(MISSED_LETTERS)])
    print()

    print('Missed letters:', end=' ')
    for char in MISSED_LETTERS:
        print(char, end=' ')
    print()

    blanks = '_' * len(SECRET_WORD)

    for i, char in enumerate(SECRET_WORD):
        # Replace blanks with correctly guessed letters
        if char in CORRECT_LETTERS:
            blanks = blanks[:i] + char + blanks[i+1:]

    for char in blanks:
        # Show the secret word with spaces in between each letter
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
            print('You have already guessed that letter. Choose again.')
        elif new_guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter.')
        else:
            return new_guess


show_intro()


# Runs main game
print('H A N G M A N')
MISSED_LETTERS = ''
CORRECT_LETTERS = ''
SECRET_WORD = get_random_word(words)
GAME_IS_DONE = False

while not GAME_IS_DONE:
    display_board()

    # Let the player enter a letter.
    guess = get_guess(MISSED_LETTERS + CORRECT_LETTERS)

    if guess in SECRET_WORD:
        CORRECT_LETTERS = CORRECT_LETTERS + guess

        # Check if the player has won.
        FOUND_ALL_LETTERS = True
        for j, letter in enumerate(SECRET_WORD):
            if SECRET_WORD[j] not in CORRECT_LETTERS:
                FOUND_ALL_LETTERS = False
                break
        if FOUND_ALL_LETTERS:
            print('Yes! The secret word is "' + SECRET_WORD +
                  '"! You have won!')
            GAME_IS_DONE = True
    else:
        MISSED_LETTERS = MISSED_LETTERS + guess

        # Check if player has guessed too many times and lost
        if len(MISSED_LETTERS) == len(HANGMAN_PICS) - 1:
            display_board()
            print(
                'You have run out of guesses!\nAfter '
                + str(len(MISSED_LETTERS)) +
                ' missed guesses and ' + str(len(CORRECT_LETTERS))
                + ' correct guesses, the word was "' + SECRET_WORD + '"')
            GAME_IS_DONE = True

    # Check if the player wants to play again
    if GAME_IS_DONE:
        PLAY_AGAIN_CHOICE = ''
        while PLAY_AGAIN_CHOICE not in ['yes', 'no']:
            PLAY_AGAIN_CHOICE = input(
                "Do you want to play again? (yes or no): "
            )
            if PLAY_AGAIN_CHOICE not in ['yes', 'no']:
                print("Invalid choice. Please select 'yes' or 'no'.")

        if PLAY_AGAIN_CHOICE == 'yes':
            MISSED_LETTERS = ''
            CORRECT_LETTERS = ''
            GAME_IS_DONE = False
            SECRET_WORD = get_random_word(words)
        else:
            print("Thanks for playing Hangman! Come back soon.")
            break
