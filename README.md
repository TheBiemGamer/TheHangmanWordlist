# The Hangman Wordlist
A simple json wordlist for use with hangman with easy, medium and hard words!

### Example usage in python (see [main.py](the_hangman_wordlist.py))
```py
from the_hangman_wordlist import HangmanWordlist

if __name__ == "__main__":
    wordlist = HangmanWordlist()
    difficulty = input("What difficulty do you want? (easy/medium/hard): ")
    word, version = wordlist.pull_word(difficulty)
    print(f"\nThe {difficulty} word is: '{word}'")
    print(f"Wordlist v{version}")
    input("\nPress Enter to exit...")
```

### Credits
- [Jurriaaaantje](https://github.com/Jurriaaaantje) (Wordlist words and update wordlist functionality)
- [TheBiemGamer](https://github.com/TheBiemGamer) (Version check and json functionality)
