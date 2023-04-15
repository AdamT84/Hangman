# Welcome to Classic Hangman - Testing

[Main README.md file](/README.md)  

[View Live site](https://hangman-classic.herokuapp.com/)

[View GitHub repository](https://github.com/AdamT84/Hangman)

## Testing

### Testing user stories. 

#### First Time Player. 

1. As a first time player, I want to be able to easily find instructions about it.
    - The start screen tells the user the name of the game.
    - The rules are clearly stated on the game instructions section.
    - On the main game screen the user is told how to start the game.

2. As a first time player, I want to know easily if I won or lost. 
    - The progressive gallows and game over message clearly tell the user if they have won or lost.

3. As a first time plater, I want to be told what the secret word was if I lost.
    - Both winners and losers are told the secret word

#### Frequent Player

1. As a frequent player, I want to feel the game is random and I can both win and lose.
   - The game is truly random as the computer player is programmed to select a random choice each time. There are no patterns or preferences to pick a certain option.

2. As a frequent player, I want to start the game quickly without having to look at instructions or rules.
    

### Manual Testing
 
#### App Load

- Ensure the app loads correctly.

![App load](/screenshots/gifs/app_load.gif)

#### Introduction Data Validation

- Ensure the user can only enter numbers and letters for their username.
- Ensure that once the username is entered and user pressed enter the screen moved to game info.

![Introduction Validation](/screenshots/gifs/enter_name_validation.gif)

#### Game Play

- Ensure that the main game screen loads when user presses enter to start the game.

![Game start](/screenshots/gifs/game_start.gif)

- Ensure that the users guesses are displayed correctly for correct and incorrect guesses.

- Ensure gallows progresses for incorrect answers.

- Ensure terminal clears after each guess.

![Game play](/screenshots/gifs/letters.gif)

- Ensure that only single letters can be entered for a guess.

![Letters only](/screenshots/gifs/guess_validation.gif)

![Multiple letters](/screenshots/gifs/multiple_letters.gif)

- Ensure user is informed if they select a letter they have already chosen.

![Duplicate guess](/screenshots/gifs/duplicate_choice.gif)

- Ensure the win message is displayed when user wins.

- Ensure the user is asked to play again after a win.

![Game win](/screenshots/gifs/game_win.gif)

- Ensure the lose message is displayed when the user loses.

- Ensure the user is asked to play again after a loss.

- Ensure user gets goodbye message if they select no to play again.

![Game loss](/screenshots/gifs/play_again_no.gif)

- Ensure the game reloads correctly if user selects yes to play again.

![Game restart](/screenshots/gifs/play_again_yes.gif)

- Ensure the user must choose yes or no in response to play again.

![Play again validation](/screenshots/gifs/play_again_validation.gif)


### Code Validation

- The python code was passed through the [CI Python Linter](https://pep8ci.herokuapp.com/) without any errors.

![Python CI Linter](/screenshots/ci_linter.png)

[Main README.md file](/README.md)