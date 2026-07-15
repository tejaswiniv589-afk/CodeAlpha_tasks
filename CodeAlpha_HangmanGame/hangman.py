"""
Hangman Game
CodeAlpha Python Programming Internship - Task 1

A simple text-based Hangman game where the player guesses a word
one letter at a time, with a limit of 6 incorrect guesses.
"""

import random

# A small list of predefined words, each with a clue to help the player
WORDS = {
    "python": "A popular programming language named after a snake.",
    "hangman": "The name of this very game.",
    "internship": "A temporary position to gain work experience.",
    "coding": "The act of writing instructions for a computer.",
    "developer": "A person who builds software or applications.",
}

MAX_ATTEMPTS = 6

# ASCII art stages for the hangman drawing, one for each wrong guess (0 to 6)
HANGMAN_STAGES = [
    """
   -----
   |   |
       |
       |
       |
       |
--------
""",
    """
   -----
   |   |
   O   |
       |
       |
       |
--------
""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
--------
""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
--------
""",
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
--------
""",
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
--------
""",
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
--------
""",
]


def choose_word():
    """Randomly select a word (with its clue) from the WORDS dictionary."""
    word = random.choice(list(WORDS.keys()))
    clue = WORDS[word]
    return word, clue


def display_word(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word, clue = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses allowed.")
    print(f"Clue: {clue}")
    print("(Type 'hint' anytime to see the clue again.)")
    print("=" * 40)

    while wrong_guesses < MAX_ATTEMPTS:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_ATTEMPTS}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower().strip()

        if guess == "hint":
            print(f"Clue: {clue}")
            continue

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter (or type 'hint').")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 40)
            print(f"Congratulations! You guessed the word: {word}")
            print("=" * 40)
            return

    # Loss condition
    print(HANGMAN_STAGES[wrong_guesses])
    print("\n" + "=" * 40)
    print("Game Over! You've run out of attempts.")
    print(f"The word was: {word}")
    print("=" * 40)


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("\nThanks for playing Hangman! Goodbye.")


if __name__ == "__main__":
    main()