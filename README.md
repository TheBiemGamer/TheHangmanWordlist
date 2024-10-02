![Screenshot of code](https://raw.githubusercontent.com/TheBiemGamer/TheHangmanWordlist/refs/heads/main/assets/10015-io-code-screenshot.png)
[![PyPI version](https://badge.fury.io/py/the-hangman-wordlist.svg)](https://badge.fury.io/py/the-hangman-wordlist)
> [!NOTE]
> A simple [Python library](https://pypi.org/project/the-hangman-wordlist/) with a wordlist for use with hangman featuring easy, medium and hard words!

### Usage
First install the package:
```bash
$ pip install the-hangman-wordlist
```
or
```bash
$ pip3 install the-hangman-wordlist
```
Then you could use it like the following example code which generates words endlessly:
```py
from the_hangman_wordlist import HangmanWordlist

if __name__ == "__main__":
    wordlist = HangmanWordlist()

    difficulty = ""
    while difficulty not in {"easy", "medium", "hard", "random"}:
        difficulty = input("What difficulty do you want? (easy/medium/hard/random): ").lower()
        difficulty = {
            "e": "easy",
            "m": "medium",
            "h": "hard",
            "r": "random"
        }.get(difficulty, difficulty)

    script_version, wordlist_version = wordlist.version()
    print(f"Script v{script_version} and wordlist v{wordlist_version}.")

    while True:
        print(f"\n{difficulty.capitalize()} difficulty word: '{wordlist.pull_word(difficulty)}'\n")
        if input("Press Enter to generate a word or type 'exit' to quit... ").lower() == "exit":
            break
```

### Functions
```py
def __init__():
    # Loads when HangmanWordlist is imported, sets the variables and loads the wordlist with the load_wordlist() function.

def fetch_online_wordlist():
    # Fetches the wordlist online and returns it as json.

def load_wordlist():
    # Checks if the user has a copy of the wordlist.json and if it's up to date and then downloads it if necessary with the save_wordlist() function.

def save_wordlist(wordlist):
    # Saves the passed wordlist to wordlist.json

def pull_word(difficulty):
    # Checks if the difficulty passed is a correct option if not it chooses a random difficulty and then it returns a random word from the chosen difficulty.

def version():
    # Simply returns the current script version and wordlist version as a list like this:
    # ('script_version', 'wordlist_version')

```
Only the pull_word() and version() functions were made to be called by the user the different functions should be called automatically when the script is initialized.

### Credits
- [Jurriaaaantje](https://github.com/Jurriaaaantje) (Wordlist words and update wordlist functionality)
- [TheBiemGamer](https://github.com/TheBiemGamer) (Version check, json functionality and library)
