import random

HANGMAN_PICS = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
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


# Runs main game
print('H A N G M A N')
MISSED_LETTERS = ''
CORRECT_LETTERS = ''
SECRET_WORD = get_random_word(words)
GAME_IS_DONE = False
PLAY_AGAIN_CHOICE = ''

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


