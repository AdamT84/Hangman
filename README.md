# Welcome to Classic Hangman


## Introduction

Hangman is a game that originated in 17th century Europe and was played when a when a prisoner facing death demanded the “Rite of Words and Life.”

The prisoner was strung up over a 5–legged stand, then a blank word would be presented by the executioner. With each incorrect guess, a leg would be knocked away. If the word was guessed correctly, the prisoner would be set free, if not, once all 5 legs were chopped, he would hang. This “game” definitely had dark beginnings, but in time, has grown to a much more fun-loving game kids of all ages.

The purpose of this site is allow players of all ages to test their logic and guessing ability against the computer. With over 40 possible words that are selected at random the game can be played multiple times before the same word re-appears.

## User Experience Design

### User stories

#### First Time Player Goals

- As a first time player, I want to be able to easily find instructions about it.
- As a first time player, I want to know easily if I won or lost the round. 
- As a first time plater, I want to be told what the secret word was if I lost.

#### Frequent Player Goals

- As a frequent player I want to feel the game is random and I can both win and lose.
- As a frequent player I want to start the game quickly without having to look at instructions or rules.

## Design

As this game is desgined to run on a terminal based window ASCII art has been added to the intro screen to make it more visually appealing and ensure the text is well spaced to make it easier to read. 

## Existing Features

### Introduction 

- Once the game is run, the user will be presented with the introduction screen. This screen features some ASCII art spelling out hangman, and requests the users name. 

### Game Instructions

- Once the user has entered their name and pressed enter they will be presented with the game instructions, informing them of the number of guesses allowed and a hint as to what the words relate too.
- The player can then select enter to being the game when they are ready.

### Game Play

- Once the user is in the game they will be able to see the empty gallows and an instruction to guess a letter.

- If the letter they guess is correct then the gallows will remain empty and they will see that letter add in the relevant place on the board. 

- If the letter they guess is incorrect then the first part of the man will appear on the gallows and the letter will appear in the "wrong guesses" area. 

- This will repeat until the user correctly guesses the word or they hit 6 guesses filling the gallows and hanging the man. 

- Once the game is over if the user has lost, they will be told how many wrong and how many correct guess they made and what the word was. Winners will be told they have won

- The user will then be asked if they wish to play again with a yes or no response. 


### Future Features

- I would like to add a score capture option to the game. 


## Technologies Used

### Langages Used

- Python3

### Libraries, Frameworks & Programs used

- [Git](https://git-scm.com/)
    - Git was used for version control by using the terminal within GitPod to commit to Git and then push to GitHub.

- [GitHub](https://github.com/)
    - GitHub was used to store the project after performing a push from GitPod.

- [Heroku](https://www.heroku.com/home)
    - Heroku is used to build, run and scale applications in a similar manner across most languages.

- The Code Institute's GitHub full template for Python is used in order for the program to display properly in the deployed site on Heroku.


## Testing

Information on testing performed is located in a separate testing file 

## Bugs 

### Solved bugs

### Unfixed bugs

There are no unfixed bugs

## Deployment

### Deploy to Heroku

- Go to the Heroku Dashboard.
- Click New.
- Select to create a new app.
- Add Config Var's for Creds and Port
- Set the buildbacks to Python and NodeJS in that order.
- Link the Heroku app to the repository.
- Click on Deploy.

## Credits

### Content

I have listed below the main sites that have helped me complete this project. I spent time looking at tutorials and other games online on sites such as Stack Overflow and Slack and videos on YouTube for ideas and inspiration, but found the below resources extremely helpful. I would also like to thank my CI mentor Chris Quinn for his advice and motivation throughout this project. 

- This site was extremely helpful and showed me multpile options to code this game. [Invent with Python](https://inventwithpython.com).
- How to buid hangman tuitorial by Kite on [YouTube](https://www.youtube.com/watch?v=m4nEnsavl6w) was very helpful.
- My ASCII art was taken from KeoCode's GitHub repository [Keo Code](https://github.com/KeoCode/Hangman).


