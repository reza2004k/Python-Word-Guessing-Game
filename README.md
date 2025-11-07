# 🐍 Python Console Word Guessing Game

This project is a simple, command-line implementation of a word guessing game. It is designed to be highly customizable by using an external file to store the list of words.

## ✨ Features

* **File-Based Word List:** Reads a word list from a separate file (`word.txt`), making it easy to change the lexicon.
* **Random Selection:** Selects a random word from the list for the player to guess.
* **Limited Attempts:** The player has a fixed number of chances (5, based on the code snippet) to guess the word correctly.
* **Immediate Feedback:** Provides feedback on whether the guessed letter is correct or incorrect.
* **Console Interface:** Simple text-based interface for easy playing and debugging.

## 🛠️ Technologies Used

* **Language:** Python 3
* **Libraries:** `random` (for word selection), `sys` (for exiting the program)
* **Interface:** Command Line / Terminal

## 🚀 Getting Started

To run the game successfully, you must ensure both the Python script and the word list file are correctly placed.

### Prerequisites

* Python 3 installed on your system.
* A text file named **`word.txt`** containing the list of words for the game.

### Setup and Running

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Python-Word-Guessing-Game.git](https://github.com/YOUR_USERNAME/Python-Word-Guessing-Game.git)
    cd Python-Word-Guessing-Game
    ```
2.  **Create the Word List:**
    In the root directory of the project, create a file named **`word.txt`**. Each word should be on a **separate line**.
    
    *Example `word.txt` content:*
    ```
    apple
    banana
    orange
    grape
    python
    ```

3.  **Run the Game:**
    Execute the Python script from your terminal:
    ```bash
    python guess_word.py
    ```

### How to Play

1.  The program will display a set of dashes (`-`), one for each letter in the secret word.
2.  You will be prompted to guess a single letter.
3.  If the letter is in the word, it will be revealed in all its correct positions.
4.  If the letter is not in the word, you lose one chance.
5.  Continue guessing until you either reveal the entire word (You Win!) or run out of chances (You Lose!).

---
