# CodeAlpha Hangman Game

A simple text-based Hangman game built in Python as part of the **CodeAlpha Python Programming Internship (Task 1)**.

## 📖 About

The player guesses a hidden word one letter at a time. The game ends when:
- The player successfully guesses all letters in the word (**Win**), or
- The player makes 6 incorrect guesses (**Loss**)

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository:
```bash
   git clone https://github.com//tejaswiniv589-afk/CodeAlpha_HangmanGame.git
   cd CodeAlpha_HangmanGame
```
3. Run the script:
```bash
   python hangman.py
```

## 🎮 How to Play

- The program picks a random word from a predefined list.
- You'll see underscores representing each letter of the word.
- A clue is shown at the start of each round — type `hint` anytime to see it again.
- Enter one letter at a time to guess the word.
- You have 6 incorrect guesses before the game ends.
- After each round, you can choose to play again.

## 🛠 Concepts Used

- `random` module
- `while` loops
- `if-else` conditionals
- Strings and lists
- Functions
- Sets (for tracking guessed letters)

## 📌 Internship

This project was completed as part of the **Python Programming Internship** at [CodeAlpha](https://www.codealpha.tech).
