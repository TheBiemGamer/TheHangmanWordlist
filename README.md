![Screenshot of code](https://raw.githubusercontent.com/TheBiemGamer/TheHangmanWordlist/refs/heads/main/assets/10015-io-code-screenshot.png)
[![PyPI - Version](https://img.shields.io/pypi/v/the-hangman-wordlist?style=flat&logo=python)](https://pypi.org/project/the-hangman-wordlist/)

### Overview
**The Hangman Wordlist** is a Python package designed to provide a diverse selection of words for playing the classic game of Hangman. It features a robust word list that can be updated from an online source, allowing for fresh gameplay experiences. This package was created by Noah Bozkurt and Jurriaan Portier.

### Installation
You can install the package via pip:
```bash
pip install the-hangman-wordlist
```

### Features
- Word Retrieval: Fetches a word list from an online source to ensure it is up-to-date.
- Local Caching: Saves the word list locally to minimize download time and ensure availability offline.
- Difficulty Levels: Supports three levels of difficulty: easy, medium, and hard.
- Random Word Selection: Allows for random word selection across different difficulties.

### Usage
To use the Hangman Wordlist package, import it and create an instance of `HangmanWordlist`:
```python
from the_hangman_wordlist import HangmanWordlist

# Initialize the wordlist
wordlist = HangmanWordlist()
```

### Pulling a Word
To pull a word from the list, use the pull_word method. You can specify the difficulty level or let the package choose one at random:
```python
word = wordlist.pull_word(diff="easy")  # Pulls an easy word
```
If you want a random word regardless of difficulty:
```python
word = wordlist.pull_word()  # Pulls a word from any difficulty
```

### Getting Version Information
To retrieve the current package version and the word list version, use the version method:
```python
script_version, wordlist_version = wordlist.version()
print(f"Library v{script_version} and wordlist v{wordlist_version}.")
```

### Example Script
Here is a simple script demonstrating how to use the package:
```python
from the_hangman_wordlist import HangmanWordlist

if __name__ == "__main__":
    wordlist = HangmanWordlist()
    print("This is the example script for The Hangman Wordlist")
    
    difficulty = ""
    while difficulty not in {"easy", "medium", "hard", "random"}:
        difficulty = input("What difficulty do you want? (easy/medium/hard/random): ").lower()
        difficulty = {
            "e": "easy",
            "m": "medium",
            "h": "hard",
            "r": "random"
        }.get(difficulty, difficulty)Jurriaan

    script_version, wordlist_version = wordlist.version()
    print(f"Library v{script_version} and wordlist v{wordlist_version}.")

    while True:
        print(f"\n{difficulty.capitalize()} difficulty word: '{wordlist.pull_word(difficulty)}'\n")
        if input("Press Enter to generate a word or type 'exit' to quit... ").lower() == "exit":
            break
```

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.