"""
The Hangman Wordlist v0.4
By Noah Bozkurt and Jurriaan Portier
"""
from the_hangman_wordlist import HangmanWordlist

if __name__ == "__main__":
    wordlist = HangmanWordlist()
    difficulty = input("What difficulty do you want? (easy/medium/hard): ")
    word, version = wordlist.pull_word(difficulty)
    print(f"\nThe {difficulty} word is: '{word}'")
    print(f"Wordlist v{version}")
    input("\nPress Enter to exit...")