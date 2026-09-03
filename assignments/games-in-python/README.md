
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Set up the initial state for the Hangman game by selecting a secret word and preparing the variables needed to track the player's progress.

#### Requirements
Completed program should:

- Randomly select a word from the `words` list using the `random` module
- Initialize a variable to track the letters guessed so far
- Initialize a counter for incorrect guesses
- Define the maximum number of incorrect guesses allowed

### 🛠️ Implement the Game Loop

#### Description
Write the main game loop that lets the player guess letters, tracks their progress, and ends the game with a win or lose message.

#### Requirements
Completed program should:

- Display the current progress of the word using an underscore (`_`) for each unguessed letter, for example: `_ _ t h _ n`
- Accept a letter guess from the player using `input()`
- Update the guessed letters and incorrect guess count based on the input
- End the game when the word is fully guessed or the maximum incorrect guesses is reached
- Print a win message if the word is guessed, or a lose message revealing the word if attempts run out
