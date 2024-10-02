"""
The Hangman Wordlist v0.6.1
By Noah Bozkurt and Jurriaan Portier

Example usage:
from the_hangman_wordlist import HangmanWordlist

if __name__ == "__main__":
    wordlist = HangmanWordlist()
    difficulty = input("What difficulty do you want? (easy/medium/hard): ")
    word, version = wordlist.pull_word(difficulty)
    print(f"\nThe {difficulty} word is: '{word}'")
    print(f"Wordlist v{version}")
    input("\nPress Enter to exit...")
"""

import requests
import json
import random
import os

class HangmanWordlist:
    def __init__(self):
        self.online_list = "https://raw.githubusercontent.com/TheBiemGamer/TheHangmanWordlist/refs/heads/main/src/the_hangman_wordlist/wordlist.json"
        self.local_file = "wordlist.json"
        self.wordlist = self.load_wordlist()

    def fetch_online_wordlist(self):
        response = requests.get(self.online_list)
        return response.json()

    def load_wordlist(self):
        if os.path.exists(self.local_file):
            with open(self.local_file, "r") as local_file:
                local_wordlist = json.load(local_file)
            online_wordlist = self.fetch_online_wordlist()
            if float(online_wordlist["version"]) > float(local_wordlist["version"]):
                self.save_wordlist(online_wordlist)
                print("Updated wordlist")
                return online_wordlist
            else:
                return local_wordlist
        else:
            wordlist = self.fetch_online_wordlist()
            self.save_wordlist(wordlist)
            print("Downloaded and saved new wordlist")
            return wordlist

    def save_wordlist(self, wordlist):
        with open(self.local_file, "w") as output_file:
            json.dump(wordlist, output_file, indent=4)

    def pull_word(self, diff):
        word = random.choice(self.wordlist[diff])
        return word, self.wordlist["version"]